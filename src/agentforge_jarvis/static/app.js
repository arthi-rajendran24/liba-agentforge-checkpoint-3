'use strict';
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const human = s => String(s).replaceAll('_', ' ').replaceAll('-', ' ');
const money = n => '₹' + Number(n).toLocaleString('en-IN', {maximumFractionDigits:0});
const fmt = value => typeof value === 'number' ? value.toLocaleString('en-IN', {maximumFractionDigits:2}) : String(value);
let state = {team: localStorage.getItem('agentforge-team') || 'liba-team-01', agents:[], scenario:null, challenge:'baseline', run:null, runs:[], notes:[], active:false, events:[], stream:null, statuses:{}, view:'command', chatBusy:false};
let toastTimer, runTimer, startedAt, inspectorAgent;

async function api(path, options={}) {
  const response = await fetch(path, {...options, headers:{'Content-Type':'application/json', ...options.headers}});
  if (!response.ok) {
    let error; try { error = await response.json(); } catch { error = {detail:response.statusText}; }
    if(response.status===401 && path!=='/api/auth/login') openDialog('login-dialog');
    throw new Error(Array.isArray(error.detail) ? error.detail.map(x => `${x.loc.slice(1).join('.')}: ${x.msg}`).join('; ') : error.detail || 'Request failed');
  }
  return response.json();
}
const teamQuery = () => 'team=' + encodeURIComponent(state.team);
const requestBody = (domain=null) => ({team:state.team,scenario:state.scenario,challenge:state.challenge,domain});
function toast(message, error=false) { clearTimeout(toastTimer); $('toast').textContent=message; $('toast').className='toast'+(error?' error':''); toastTimer=setTimeout(()=>$('toast').classList.add('hidden'),error?10000:4500); }
function openDialog(id) { $(id).showModal(); }
function navigate(view) { state.view=view; document.querySelectorAll('.view').forEach(x=>x.classList.toggle('hidden',x.id!=='view-'+view)); document.querySelectorAll('[data-view]').forEach(x=>x.classList.toggle('active',x.dataset.view===view)); if(view==='archive') renderArchive(); if(view==='workshop') renderWorkshop(); }
function guardBusy() { if(state.active || state.chatBusy) { toast('Wait for the current run or conversation to finish before changing the workspace.',true); return true; } return false; }
function clearCurrent() { state.run=null; state.statuses={}; renderNetwork(); renderReports(); renderWorkshop(); }

async function bootstrap() {
  try {
    const auth=await api('/api/auth/status');
    if(auth.required && !auth.team) { openDialog('login-dialog'); return; }
    if(auth.required) state.team=auth.team;
    $('team').disabled=auth.required;
    $('team-form').querySelector('button').disabled=auth.required;
    $('sign-out').classList.toggle('hidden',!auth.required);
    if(!/^[a-zA-Z0-9_-]{1,48}$/.test(state.team)) state.team='liba-team-01';
    $('team').value=state.team;
    const data=await api('/api/bootstrap?'+teamQuery());
    Object.assign(state,{agents:data.agents,settings:data.settings,scenario:data.scenario,challenges:data.challenges,rubric:data.rubric,runs:data.runs,notes:data.notes,run:null,statuses:{},events:[],challenge:'baseline'});
    const saved=localStorage.getItem('agentforge-scenario-'+state.team);
    if(saved) { try { const validated=await api('/api/scenario/validate',{method:'POST',body:saved}); state.scenario=validated; } catch { localStorage.removeItem('agentforge-scenario-'+state.team); } }
    $('chat-agent').innerHTML='<option value="">JARVIS · command interface</option>'+state.agents.map(a=>`<option value="${a.id}">${esc(a.name)} · ${esc(a.label)}</option>`).join('');
    $('provider').textContent=state.settings.provider==='rehearsal'?'◌ REHEARSAL MODE':state.settings.provider.toUpperCase()+' · '+(state.settings.live_verified?'LIVE VERIFIED':state.settings.configured?'READY TO TEST':'SETUP NEEDED');
    $('chat-mode').textContent=state.settings.provider==='rehearsal'?'REHEARSAL · SCRIPTED RESPONSES':'LIVE MODEL · '+state.settings.provider.toUpperCase();
    $('mode-explainer').textContent=state.settings.provider==='rehearsal'?'Rehearsal uses scripted responses with real LangChain tool execution.':'Live '+state.settings.provider+' model · calculated facts stay in domain tools.';
    $('settings-info').innerHTML=`<div class="info-bar">${esc(state.settings.provider)} / ${esc(state.settings.model)}<br>${esc(state.settings.last_provider_error||state.settings.error||(state.settings.live_verified?'Live response verified at '+state.settings.live_verified_at:'Configuration loaded. Run an agent to verify live connectivity.'))}</div>`;
    renderNetwork(); renderScenario(); renderReports(); renderNotes(); renderArchive(); renderWorkshop(); renderMessages(data.messages);
    $('telemetry').innerHTML='<p class="muted">Tool calls and agent hand-offs appear here as they happen.</p>'; $('event-count').textContent='00';
    const pending=state.runs.find(r=>['queued','running'].includes(r.status));
    if(pending) { state.scenario=pending.base_scenario; state.challenge=pending.challenge; renderScenario(); watchRun(pending); }
  } catch(error) { toast('Could not load the command center: '+error.message,true); }
}

function renderNetwork() {
  $('roster').innerHTML=state.agents.map(a=>`<button class="agent-card ${esc(state.statuses[a.id]||'')}" data-agent="${a.id}" style="--agent-color:${a.color}"><span class="agent-avatar">${a.symbol}</span><span><strong>${a.name}</strong><small>${a.label}</small></span><i class="agent-led"></i></button>`).join('');
  $('orbit-agents').innerHTML=state.agents.map(a=>`<button class="orbit-agent ${esc(state.statuses[a.id]||'')}" data-agent="${a.id}" style="--agent-color:${a.color}"><span class="symbol">${a.symbol}</span><span><strong>${a.name}</strong><small>${esc(state.statuses[a.id] ? human(state.statuses[a.id]).toUpperCase() : a.id==='general-management'?'STRATEGY':a.label.toUpperCase())}</small></span></button>`).join('');
  const completed=Object.values(state.statuses).filter(x=>['completed','hold'].includes(x)).length;
  $('completed-count').textContent=completed+' / 6 COMPLETE';
}
function effectiveScenario() { const s={...state.scenario}; if(state.challenge==='budget-cut')s.budget*=.75; if(state.challenge==='demand-surge')s.units=Math.round(s.units*1.4); if(state.challenge==='supply-delay')s.lead_days+=14; return s; }
function renderScenario() {
  const s=effectiveScenario();
  $('scenario-name').textContent=s.name; $('scenario-company').textContent=s.company;
  $('budget-value').textContent=money(s.budget); $('units-value').textContent=fmt(s.units)+' units'; $('days-value').textContent=s.launch_days+' days';
  $('challenges').innerHTML=state.challenges.map(c=>`<button data-challenge="${c.id}" title="${esc(c.description)}" class="${state.challenge===c.id?'active':''}">${esc(c.name)}</button>`).join('');
}
function renderReports() {
  const run=state.run, reports=run?.reports||{}, gm=reports['general-management'];
  $('exports').classList.toggle('hidden',run?.status!=='completed');
  if(gm) {
    $('decision').className='decision '+gm.status;
    $('decision').innerHTML=`<span class="decision-icon">${gm.status==='hold'?'!':'✧'}</span><div><div class="decision-status">${esc(gm.metrics.decision)} / ${esc(run.challenge).toUpperCase()} / ${esc(run.provider).toUpperCase()} / ${run.id.slice(0,8)}</div><h3>${esc(gm.recommendation)}</h3><p>${esc(gm.risks[0]||'Review specialist findings before approving the launch.')}</p><button data-agent="general-management">Inspect decision &amp; owners ↗</button></div>`;
  } else {
    $('decision').className='decision empty';
    $('decision').innerHTML=`<span class="decision-icon">✧</span><div><h3>${run?.status==='completed'?'Specialist run complete.':'Your next move starts here.'}</h3><p>${run?.error?esc(run.error):run?.status==='completed'?'Inspect the specialist findings below. Run the full swarm for an executive decision.':'Run the team to receive a launch recommendation, evidence, risks, and named owners.'}</p></div>`;
  }
  $('report-grid').innerHTML=state.agents.map(a=>{ const r=reports[a.id]; return `<button class="report-card" data-agent="${a.id}" style="--agent-color:${a.color}"><span class="micro">${a.symbol} ${a.name} / ${a.label.toUpperCase()}</span><h3>${esc(r?.headline||a.role)}</h3>${r?`<span class="badge ${r.status}">${r.status.toUpperCase()} · ${r.tools_called.length} TOOL CALLS</span>`:'<p>Open blueprint &amp; capabilities ↗</p>'}</button>`; }).join('');
}
function addEvent(event) {
  state.events.push(event); if(state.events.length===1)$('telemetry').innerHTML='';
  $('event-count').textContent=String(state.events.length).padStart(2,'0');
  const a=state.agents.find(x=>x.id===event.domain);
  const time=event.time?new Date(event.time).toLocaleTimeString('en-GB',{hour12:false}):'';
  const verb=event.kind==='tool_started'?'↳ call ':event.kind==='tool_completed'?'✓ result ':event.kind==='agent_started'?'activate ':event.kind==='agent_completed'?'complete ':'';
  const row=document.createElement('div'); row.innerHTML=`<time>${esc(time)}</time><span class="event-domain">${esc(a?.name||'SYSTEM')}</span><br>${esc(verb+(event.tool||event.headline||event.message||human(event.kind)))}`;
  $('telemetry').appendChild(row); $('telemetry').scrollTop=$('telemetry').scrollHeight;
  if(event.kind==='agent_started') { state.statuses[event.domain]='running'; $('core-state').textContent=(a?.name||'AGENT')+' PROCESSING'; }
  if(event.kind==='agent_completed')state.statuses[event.domain]=event.status==='hold'?'hold':'completed';
  renderNetwork();
}
async function startRun(domain=null) {
  if(guardBusy())return;
  try { const run=await api('/api/runs',{method:'POST',body:JSON.stringify(requestBody(domain))}); state.run=null; state.statuses={}; renderReports(); watchRun(run); navigate('command'); }
  catch(error){toast(error.message,true);}
}
function watchRun(run) {
  if(state.stream)state.stream.close();
  state.active=true; state.run=run; state.events=[]; state.statuses={};
  $('run-swarm').disabled=true; $('cancel-run').classList.remove('hidden');
  $('reactor-stage').classList.add('running'); $('swarm-state').textContent='SWARM EXECUTING';
  $('core-state').textContent='CONNECTING SPECIALISTS'; $('telemetry').innerHTML='';
  startedAt=Date.now(); clearInterval(runTimer);
  runTimer=setInterval(()=>$('elapsed').textContent=((Date.now()-startedAt)/1000).toFixed(1)+'s ELAPSED',100);
  const source=new EventSource(`/api/runs/${run.id}/events?${teamQuery()}`); state.stream=source;
  source.onmessage=e=>addEvent(JSON.parse(e.data));
  source.addEventListener('done',async()=>{source.close(); await finishRun(run.id);});
  source.onerror=async()=>{
    try { const current=await api(`/api/runs/${run.id}?${teamQuery()}`); if(!['queued','running'].includes(current.status)){source.close();await finishRun(run.id);} }
    catch { $('swarm-state').textContent='CONNECTION LOST · RECONNECTING'; }
  };
}
async function finishRun(id) {
  clearInterval(runTimer); state.active=false; state.stream=null;
  $('run-swarm').disabled=false; $('cancel-run').classList.add('hidden'); $('reactor-stage').classList.remove('running');
  try {
    state.run=await api(`/api/runs/${id}?${teamQuery()}`); state.runs=await api('/api/runs?'+teamQuery());
    for(const [d,r] of Object.entries(state.run.reports))state.statuses[d]=r.status==='hold'?'hold':'completed';
    if(state.run.status!=='completed') Object.keys(state.statuses).forEach(d=>{if(state.statuses[d]==='running')state.statuses[d]='';});
    $('swarm-state').textContent=state.run.status==='completed'?'SWARM COMPLETE':state.run.status.toUpperCase();
    $('core-state').textContent=state.run.status==='completed'?'AWAITING HUMAN REVIEW':'READY TO RETRY';
    $('elapsed').textContent=state.run.duration_seconds+'s / '+state.run.provider.toUpperCase();
    renderNetwork(); renderReports(); renderArchive(); renderWorkshop();
    refreshProvider();
    toast(state.run.status==='completed'?'Decision package saved to '+state.team+'.':state.run.error,state.run.status!=='completed');
  } catch(error){toast(error.message,true);}
}

function metricValue(k,v) { return k.endsWith('_inr')?money(v):fmt(v); }
function list(items) { return '<ul>'+items.map(x=>`<li>${esc(x)}</li>`).join('')+'</ul>'; }
function table(rows) { if(!rows?.length)return ''; const keys=Object.keys(rows[0]); return `<div class="table-wrap"><table><thead><tr>${keys.map(k=>`<th>${esc(human(k))}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${keys.map(k=>`<td>${esc(metricValue(k,row[k]))}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`; }
function inspect(domain, tab='report') {
  const a=state.agents.find(x=>x.id===domain); if(!a)return; inspectorAgent=domain;
  const r=state.run?.reports?.[domain]; if(!r)tab='blueprint';
  $('inspector-kicker').textContent=a.name+' / '+a.label.toUpperCase();
  $('inspector-body').innerHTML=`<h2>${esc(a.role)}</h2><p>${esc(a.goal)}</p><div class="inspector-tabs"><button data-inspector-tab="report" class="${tab==='report'?'active':''}" ${!r?'disabled':''}>Report &amp; evidence</button><button data-inspector-tab="blueprint" class="${tab==='blueprint'?'active':''}">Agent blueprint</button></div>`;
  if(tab==='report') {
    $('inspector-body').innerHTML+=`<span class="badge ${r.status}">${r.status.toUpperCase()} / ${esc(state.run.provider).toUpperCase()} / ${state.run.id.slice(0,8)}</span><h3>${esc(r.headline)}</h3><p>${esc(r.recommendation)}</p><div class="metric-grid">${Object.entries(r.metrics).map(([k,v])=>`<div class="metric"><small>${esc(human(k)).toUpperCase()}</small><strong>${esc(metricValue(k,v))}</strong></div>`).join('')}</div><h3>Detail worksheet</h3>${table(r.details)}<h3>Source evidence</h3>${list(r.evidence)}<h3>Assumptions</h3>${list(r.assumptions)}<h3>Risks &amp; open questions</h3>${list(r.risks)}<h3>Accountable actions</h3>${table(r.actions)}<h3>Agent commentary <span class="micro">MODEL OUTPUT · REVIEW AGAINST TOOL EVIDENCE</span></h3><pre>${esc(r.narrative)}</pre><h3>Executed tools</h3><p>${esc(r.tools_called.join(' → '))}</p>`;
  } else {
    $('inspector-body').innerHTML+=`<h3>Inputs</h3><p>${esc(a.inputs.join(' · '))}</p><h3>Tools &amp; hand-offs</h3><p>read_brief → ${esc(a.tool)} → search_memory</p><p>Depends on: ${esc(a.dependencies.map(d=>state.agents.find(x=>x.id===d).name).join(', ')||'Scenario source data')}</p><h3>Constraints</h3>${list(a.constraints)}<label for="blueprint-text">Your team’s instructions</label><textarea id="blueprint-text" class="blueprint-text" rows="6" maxlength="4000" placeholder="e.g. Use a concise executive tone. Highlight the two largest operational risks.">${esc(a.instructions)}</textarea><p class="muted">Live models use these preferences. Rehearsal responses are scripted; calculations and review gates remain fixed. Changes apply to future runs.</p><div class="form-actions"><button id="run-specialist" class="secondary">Run specialist + dependencies</button><button id="save-blueprint" class="primary">Save blueprint ↗</button></div>`;
  }
  if(!$('inspector').open)openDialog('inspector');
}
function renderMessages(messages) {
  $('transcript').innerHTML='';
  if(!messages.length) addMessage('assistant', 'Systems ready. Your six specialists are standing by. Run a launch simulation, ask a domain question, or give me evidence to remember.\n\n'+(state.settings.provider==='rehearsal'?'You are in rehearsal mode: responses are scripted, and calculations run through real tools.':'Live model mode is configured. Model responses will be verified on the first successful request.'));
  else messages.forEach(m=>addMessage(m.role,m.content));
}
function addMessage(role,content) {
  const item=document.createElement('div'); item.className='message '+role;
  const name=role==='user'?'YOU':$('chat-agent').value?state.agents.find(a=>a.id===$('chat-agent').value)?.name:'JARVIS';
  item.innerHTML=`<span class="speaker">${esc(name)}</span><p>${esc(content)}</p>`;
  $('transcript').appendChild(item); $('transcript').scrollTop=$('transcript').scrollHeight;
}
async function sendChat(message) {
  if(state.chatBusy)return;
  if(state.active){toast('The launch swarm is running. Ask your question after it completes.',true);return;}
  const text=message||$('prompt').value.trim(); if(!text)return;
  state.chatBusy=true; $('send').disabled=true; $('chat-agent').disabled=true; $('chat-progress').classList.remove('hidden');
  addMessage('user',text); $('prompt').value='';
  try {
    const result=await api('/api/chat',{method:'POST',body:JSON.stringify({...requestBody($('chat-agent').value||null),message:text})});
    addMessage('assistant',result.answer);
    result.events.forEach(addEvent);
    if($('speak').checked && 'speechSynthesis' in window){speechSynthesis.cancel(); const utterance=new SpeechSynthesisUtterance(result.answer.slice(0,2500));utterance.rate=1.02;speechSynthesis.speak(utterance);}
  } catch(error){addMessage('assistant','Request could not complete: '+error.message);toast(error.message,true);}
  finally{state.chatBusy=false;$('send').disabled=false;$('chat-agent').disabled=false;$('chat-progress').classList.add('hidden');$('prompt').focus();}
}
function renderNotes() {
  $('note-count').textContent=state.notes.length;
  $('notes-list').innerHTML=state.notes.length?state.notes.map(n=>`<article class="note-card"><div class="note-heading"><h3>${esc(n.title)}</h3><button class="text-button" data-delete-note="${n.id}">Remove</button></div><pre>${esc(n.text)}</pre><small>${esc(new Date(n.created).toLocaleString())} / ${n.text.length} CHARACTERS</small></article>`).join(''):'<div class="empty-list">Your team vault is empty. Add a source note, then ask Jarvis about it.</div>';
}
function renderArchive() {
  $('run-count').textContent=state.runs.length;
  $('archive-list').innerHTML=state.runs.length?state.runs.map(r=>`<article class="archive-row"><input type="checkbox" data-compare="${r.id}" aria-label="Compare run ${r.id.slice(0,8)}"><div class="run-meta"><h3>${esc(r.scenario.name)} / ${esc(human(r.challenge))}</h3><p>${r.id.slice(0,8)} · ${esc(new Date(r.created).toLocaleString())} · ${esc(r.provider)} · ${r.duration_seconds}s</p></div><span class="badge ${r.status}">${esc(r.reports['general-management']?.metrics.decision||r.status)}</span><button data-load-run="${r.id}">Open ↗</button></article>`).join(''):'<div class="empty-list">No saved missions yet. Run the swarm to create your first record.</div>';
  $('comparison').classList.add('hidden');
}
function compareRuns() {
  const chosen=[...document.querySelectorAll('[data-compare]:checked')].map(x=>state.runs.find(r=>r.id===x.dataset.compare));
  if(chosen.length!==2){$('comparison').classList.add('hidden'); if(chosen.length>2)toast('Select exactly two completed runs to compare.',true);return;}
  const [a,b]=chosen.sort((x,y)=>x.created.localeCompare(y.created));
  if(a.status!=='completed'||b.status!=='completed'){toast('Comparison needs two completed runs.',true);return;}
  const am=a.reports.finance?.metrics,bm=b.reports.finance?.metrics;
  $('comparison').innerHTML=`<span class="micro cyan">${a.id.slice(0,8)} → ${b.id.slice(0,8)}</span><h2>What changed?</h2><p class="muted">${esc(a.challenge)} → ${esc(b.challenge)} · compare source snapshots for other input changes.</p><div class="comparison-grid"><div><small>EXECUTIVE GATE</small><strong>${esc(a.reports['general-management']?.metrics.decision||'Specialist')} → ${esc(b.reports['general-management']?.metrics.decision||'Specialist')}</strong></div><div><small>LAUNCH BUDGET</small><strong>${money(a.scenario.budget)} → ${money(b.scenario.budget)}</strong><em>${money(b.scenario.budget-a.scenario.budget)} change</em></div><div><small>FUNDING GAP</small><strong>${am&&bm?money(am.funding_gap_inr)+' → '+money(bm.funding_gap_inr):'Finance not in both runs'}</strong></div></div>`;
  $('comparison').classList.remove('hidden');
}
function renderWorkshop() {
  const run=state.run;
  $('checks').innerHTML=run?.checks?run.checks.map(c=>`<div class="check-row"><span class="mark">${c.passed?'✓':'!'}</span><div><strong>${esc(c.name)}</strong><p>${esc(c.detail)}</p></div></div>`).join(''):'Complete a swarm run to inspect its observable checks.';
  $('assessment-run').textContent=run?.status==='completed'?'SCORING RUN '+run.id.slice(0,8):'SELECT A COMPLETED RUN FIRST';
  $('rubric-fields').innerHTML=state.rubric.map((r,i)=>`<div class="rubric-row"><label for="score-${i}">${esc(r.name)}<small>${esc(r.check)}</small></label><span class="weight">${r.weight}%</span><input id="score-${i}" type="number" min="0" max="5" step="1" value="${run?.assessment?.scores?.[i]??0}" required aria-label="${esc(r.name)} score out of 5"></div>`).join('');
  $('reflection').value=run?.assessment?.reflection||'';
  $('rubric-total').textContent=run?.assessment?'Saved score: '+run.assessment.weighted_total+'/100':'';
}
function download(filename,content,type) {const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=filename;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}

document.addEventListener('click',async(event)=>{
  const el=event.target.closest('button'); if(!el)return;
  if(el.dataset.view)navigate(el.dataset.view);
  if(el.classList.contains('close-dialog'))el.closest('dialog').close();
  if(el.dataset.agent)inspect(el.dataset.agent);
  if(el.dataset.inspectorTab)inspect(inspectorAgent,el.dataset.inspectorTab);
  if(el.dataset.challenge){if(guardBusy())return;state.challenge=el.dataset.challenge;clearCurrent();renderScenario();}
  if(el.dataset.prompt)sendChat(el.dataset.prompt);
  if(el.dataset.deleteNote){try{await api(`/api/notes/${el.dataset.deleteNote}?${teamQuery()}`,{method:'DELETE'});state.notes=state.notes.filter(n=>n.id!==el.dataset.deleteNote);renderNotes();toast('Note removed. Existing run exports and conversations retain their snapshots.');}catch(e){toast(e.message,true);}}
  if(el.dataset.loadRun){if(guardBusy())return;state.run=state.runs.find(r=>r.id===el.dataset.loadRun);state.scenario=state.run.base_scenario;state.challenge=state.run.challenge;state.statuses=Object.fromEntries(Object.entries(state.run.reports).map(([d,r])=>[d,r.status==='hold'?'hold':'completed']));renderScenario();renderNetwork();renderReports();renderWorkshop();$('swarm-state').textContent='ARCHIVED / '+state.run.status.toUpperCase();$('elapsed').textContent=state.run.duration_seconds+'s / SAVED RUN';navigate('command');}
  if(el.id==='save-blueprint'){try{const instructions=$('blueprint-text').value;await api(`/api/agents/${inspectorAgent}/blueprint`,{method:'PUT',body:JSON.stringify({team:state.team,instructions})});state.agents.find(a=>a.id===inspectorAgent).instructions=instructions;toast('Blueprint saved for future runs.');}catch(e){toast(e.message,true);}}
  if(el.id==='run-specialist'){$('inspector').close();startRun(inspectorAgent);}
});
document.addEventListener('change',event=>{if(event.target.dataset.compare)compareRuns();});
$('run-swarm').onclick=()=>startRun();
$('cancel-run').onclick=async()=>{try{await api(`/api/runs/${state.run.id}/cancel?${teamQuery()}`,{method:'POST'});toast('Cancellation requested. Any active model call must return or time out first.');}catch(e){toast(e.message,true);}};
$('provider').onclick=$('settings-button').onclick=()=>openDialog('settings-dialog');
$('team-form').onsubmit=event=>{event.preventDefault();if(guardBusy())return;state.team=$('team').value.trim();localStorage.setItem('agentforge-team',state.team);bootstrap();};
$('edit-scenario').onclick=()=>{if(guardBusy())return;$('scenario-json').value=JSON.stringify(state.scenario,null,2);openDialog('scenario-dialog');};
$('save-scenario').onclick=async()=>{try{const scenario=await api('/api/scenario/validate',{method:'POST',body:$('scenario-json').value});state.scenario=scenario;localStorage.setItem('agentforge-scenario-'+state.team,JSON.stringify(scenario));clearCurrent();renderScenario();$('scenario-dialog').close();toast('Validated scenario applied.');}catch(e){toast(e.message,true);}};
$('scenario-file').onchange=async event=>{const f=event.target.files[0];if(!f)return;if(f.size>150000){toast('Scenario file must be under 150 KB.',true);return;}$('scenario-json').value=await f.text();event.target.value='';};
$('download-scenario').onclick=()=>download('agentforge-scenario.json',$('scenario-json').value,'application/json');
$('export-md').onclick=()=>{if(state.run)window.location.href=`/api/runs/${state.run.id}/export?${teamQuery()}&format=md`;};
$('export-json').onclick=()=>{if(state.run)window.location.href=`/api/runs/${state.run.id}/export?${teamQuery()}&format=json`;};
$('chat-form').onsubmit=e=>{e.preventDefault();sendChat();};
$('prompt').onkeydown=e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing){e.preventDefault();sendChat();}};
$('chat-agent').onchange=async()=>{try{const messages=await api('/api/messages?'+teamQuery()+'&domain='+encodeURIComponent($('chat-agent').value||'supervisor'));renderMessages(messages);}catch(e){toast(e.message,true);}};
$('note-form').onsubmit=async e=>{e.preventDefault();try{const note=await api('/api/notes',{method:'POST',body:JSON.stringify({team:state.team,title:$('note-title').value,text:$('note-text').value})});state.notes.unshift(note);renderNotes();$('note-form').reset();toast('Source note saved to your team vault.');}catch(e){toast(e.message,true);}};
$('note-file').onchange=async e=>{const f=e.target.files[0];if(!f)return;if(f.size>60000){toast('Use a text note under 60 KB and 30,000 characters.',true);return;}$('note-title').value=f.name.slice(0,100);$('note-text').value=await f.text();e.target.value='';};
$('assessment-form').onsubmit=async e=>{e.preventDefault();if(state.run?.status!=='completed'){toast('Open a completed run first.',true);return;}try{const scores=state.rubric.map((_,i)=>Number($('score-'+i).value));const result=await api(`/api/runs/${state.run.id}/assessment`,{method:'POST',body:JSON.stringify({team:state.team,scores,reflection:$('reflection').value})});state.run.assessment=result;const saved=state.runs.find(r=>r.id===state.run.id);if(saved)saved.assessment=result;$('rubric-total').textContent='Saved score: '+result.weighted_total+'/100';toast('Assessment saved and included in future exports.');}catch(e){toast(e.message,true);}};
const Recognition=window.SpeechRecognition||window.webkitSpeechRecognition;
if(Recognition){const recognition=new Recognition();recognition.lang='en-IN';recognition.continuous=false;recognition.interimResults=false;$('mic').onclick=()=>{try{recognition.start();toast('Listening. Your browser may process speech online.');}catch{toast('Voice input is already active.',true);}};recognition.onresult=e=>{$('prompt').value=e.results[0][0].transcript;toast('Voice captured. Review the text, then send.');};recognition.onerror=e=>toast('Voice input unavailable: '+e.error+'. You can type your command.',true);}
else{$('mic').disabled=true;$('mic').title='Speech recognition is unavailable in this browser. Use Chrome or type your command.';}
if(!('speechSynthesis' in window)){$('speak').disabled=true;}
$('speak').onchange=()=>{if(!$('speak').checked && 'speechSynthesis' in window)speechSynthesis.cancel();};
setInterval(()=>$('clock').textContent=new Date().toLocaleTimeString('en-GB',{hour12:false}),1000);
bootstrap();

async function refreshProvider() {
  try { const health=await api('/api/health'); state.settings=health;
    $('provider').textContent=health.provider==='rehearsal'?'◌ REHEARSAL MODE':health.provider.toUpperCase()+' · '+(health.live_verified?'LIVE VERIFIED':'READY TO TEST');
    $('settings-info').textContent=health.model+' · '+(health.last_provider_error||(health.live_verified?'Live response verified at '+health.live_verified_at:'Run an agent to verify connectivity.'));
  } catch { /* Keep the last known connection state. */ }
}
$('login-dialog').addEventListener('cancel',e=>e.preventDefault());
$('login-form').addEventListener('submit',async e=>{e.preventDefault(); const button=e.target.querySelector('button');button.disabled=true;
 try {const result=await api('/api/auth/login',{method:'POST',body:JSON.stringify({team:$('login-team').value.trim(),password:$('login-code').value})});state.team=result.team;$('login-code').value='';$('login-error').textContent='';$('login-dialog').close();await bootstrap();}
 catch(error){$('login-error').textContent=error.message;}finally{button.disabled=false;}
});
$('sign-out').addEventListener('click',async()=>{if(guardBusy())return;await api('/api/auth/logout',{method:'POST'});location.reload();});

$('evidence-image').addEventListener('change',async e=>{
 const file=e.target.files[0];if(!file)return;
 if(file.size>2000000){toast('Use a PNG or JPEG under 2 MB.',true);return;}
 if(guardBusy())return;
 state.chatBusy=true;toast('Gemini is reading the image…');
 try {const data=await new Promise((resolve,reject)=>{const reader=new FileReader();reader.onload=()=>resolve(reader.result.split(',')[1]);reader.onerror=reject;reader.readAsDataURL(file);});
 const result=await api('/api/media/extract',{method:'POST',body:JSON.stringify({team:state.team,mime:file.type,data})});
 $('note-text').value=result.text;$('note-title').value=file.name;toast('Review the extracted text, then Save to memory.');
 }catch(error){toast(error.message,true);}finally{state.chatBusy=false;e.target.value='';}
});
