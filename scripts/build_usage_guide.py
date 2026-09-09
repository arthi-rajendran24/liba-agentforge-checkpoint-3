from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SHOTS = ROOT / "workshop" / "usage-screenshots"
ASSETS = ROOT / "workshop" / "usage-guide-assets"
OUTPUT = ROOT / "workshop" / "AgentForge_JARVIS_Complete_Usage_Manual.docx"

INK = "13262D"
TEAL = "0D8E83"
CYAN = "61D9C9"
PALE = "E8F6F3"
LIGHT = "F3F7F7"
MID = "D4E6E3"
AMBER = "B66B18"
WHITE = "FFFFFF"
MUTED = "536970"


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=100, start=130, bottom=100, end=130) -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{margin}"))
        if node is None:
            node = OxmlElement(f"w:{margin}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_repeat_table_header(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def keep_table_row_together(row) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    cant_split = OxmlElement("w:cantSplit")
    cant_split.set(qn("w:val"), "true")
    tr_pr.append(cant_split)


def set_run_font(run, name="Aptos") -> None:
    run.font.name = name
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), name)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), name)


def set_repeat_header(row) -> None:
    set_repeat_table_header(row)
    keep_table_row_together(row)
    for cell in row.cells:
        set_cell_shading(cell, INK)
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = RGBColor.from_string(WHITE)
                run.font.bold = True


def add_page_number(paragraph) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run("Page ")
    set_run_font(run)
    fld_char1 = OxmlElement("w:fldChar")
    fld_char1.set(qn("w:fldCharType"), "begin")
    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = "PAGE"
    fld_char2 = OxmlElement("w:fldChar")
    fld_char2.set(qn("w:fldCharType"), "end")
    run._r.extend([fld_char1, instr_text, fld_char2])


def draw_flow(filename: str, title: str, nodes: list[tuple[str, str]], footer: str) -> Path:
    ASSETS.mkdir(parents=True, exist_ok=True)
    width, height = 1800, 610
    image = Image.new("RGB", (width, height), "#071117")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 46)
    body_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
    small_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 21)
    draw.text((70, 48), title, font=title_font, fill="#E7F8F4")
    gap = 30
    left = 70
    node_width = (width - 140 - gap * (len(nodes) - 1)) // len(nodes)
    top, bottom = 180, 420
    palette = ["#123A43", "#1B354E", "#303254", "#403846", "#3D3324", "#173D37"]
    for index, (name, explanation) in enumerate(nodes):
        x1 = left + index * (node_width + gap)
        x2 = x1 + node_width
        draw.rounded_rectangle((x1, top, x2, bottom), radius=22, fill=palette[index % len(palette)], outline="#61D9C9", width=3)
        draw.text((x1 + 24, top + 34), f"{index + 1:02d}", font=small_font, fill="#61D9C9")
        draw.text((x1 + 24, top + 84), name, font=body_font, fill="#FFFFFF")
        words = explanation.split()
        lines, current = [], ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if draw.textlength(candidate, font=small_font) > node_width - 48:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
        for line_index, line in enumerate(lines[:4]):
            draw.text((x1 + 24, top + 140 + line_index * 31), line, font=small_font, fill="#BDD0D4")
        if index < len(nodes) - 1:
            ax = x2 + 7
            ay = (top + bottom) // 2
            draw.line((ax, ay, ax + gap - 14, ay), fill="#61D9C9", width=4)
            draw.polygon([(ax + gap - 14, ay - 9), (ax + gap - 14, ay + 9), (ax + gap - 3, ay)], fill="#61D9C9")
    draw.text((70, 505), footer, font=small_font, fill="#90A8AE")
    path = ASSETS / filename
    image.save(path)
    return path


architecture_flow = draw_flow(
    "architecture-flow.png",
    "How the six-agent swarm turns a brief into a decision",
    [
        ("Brief", "One shared business scenario and one injected change"),
        ("PRISM", "Finds demand signals and calculates the evidence"),
        ("Specialists", "Marketing, HR and Operations test the plan"),
        ("LEDGER", "Checks cash, margin and the funding gap"),
        ("JARVIS", "Combines the reports and preserves blocked gates"),
        ("Human", "Reviews sources, decides and owns the action"),
    ],
    "Plain-English rule: every specialist works from the same facts; a human remains accountable for the final decision.",
)

experiment_flow = draw_flow(
    "experiment-flow.png",
    "The experiment loop",
    [
        ("Baseline", "Run the unchanged Project Monsoon scenario"),
        ("Change", "Choose one challenge or edit the scenario JSON"),
        ("Rerun", "Let the same agents evaluate the new facts"),
        ("Compare", "Select exactly two completed runs in the archive"),
        ("Decide", "Explain what changed, why and what you verified"),
    ],
    "Change one important variable at a time. That makes the cause of a new recommendation easier to explain.",
)

memory_flow = draw_flow(
    "memory-flow.png",
    "How team memory is used",
    [
        ("Add source", "Paste text, import a file or extract text from an image"),
        ("Review", "Correct the extracted text before saving it"),
        ("Retrieve", "The agent searches the team vault for matching excerpts"),
        ("Calculate", "Domain tools produce the numbers and gates"),
        ("Respond", "The agent cites the source and labels assumptions"),
    ],
    "Memory is supporting evidence. It does not automatically become a verified fact.",
)

team_flow = draw_flow(
    "team-access-flow.png",
    "How a hosted team session works",
    [
        ("Facilitator", "Creates a team ID and one private access code"),
        ("Browser", "Participant opens the HTTPS workshop URL"),
        ("Sign in", "Server checks the team ID and hashed access code"),
        ("Workspace", "Runs, notes, chat and blueprints stay with that team"),
        ("Backup", "Facilitator copies the durable data directory"),
    ],
    "Never place the Gemini key in a browser, screenshot or team handout. Keep it only on the server.",
)


doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.65)
section.bottom_margin = Inches(0.65)
section.left_margin = Inches(0.72)
section.right_margin = Inches(0.72)

styles = doc.styles
normal = styles["Normal"]
normal.font.name = "Aptos"
normal.font.size = Pt(10)
normal.font.color.rgb = RGBColor.from_string(INK)
normal.paragraph_format.space_after = Pt(6)
normal.paragraph_format.line_spacing = 1.08

title_style = styles["Title"]
title_style.font.name = "Aptos Display"
title_style.font.size = Pt(35)
title_style.font.bold = True
title_style.font.color.rgb = RGBColor(0, 0, 0)
title_style.paragraph_format.space_after = Pt(10)

for style_name, size, color in (("Heading 1", 23, INK), ("Heading 2", 16, TEAL), ("Heading 3", 12, INK)):
    style = styles[style_name]
    style.font.name = "Aptos Display"
    style.font.size = Pt(size)
    style.font.bold = True
    style.font.color.rgb = RGBColor.from_string(color)
    style.paragraph_format.space_before = Pt(12)
    style.paragraph_format.space_after = Pt(6)
    style.paragraph_format.keep_with_next = True

header = section.header
header_p = header.paragraphs[0]
header_p.text = "AGENTFORGE JARVIS  |  COMPLETE USAGE MANUAL"
header_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
for run in header_p.runs:
    set_run_font(run)
    run.font.size = Pt(8)
    run.font.bold = True
    run.font.color.rgb = RGBColor.from_string(TEAL)

footer = section.footer
footer_table = footer.add_table(rows=1, cols=2, width=Inches(6.8))
footer_table.alignment = WD_TABLE_ALIGNMENT.CENTER
footer_table.columns[0].width = Inches(5.4)
footer_table.columns[1].width = Inches(1.4)
left_footer = footer_table.cell(0, 0).paragraphs[0]
left_footer.text = "LIBA workshop edition  |  Fictional workshop data"
for run in left_footer.runs:
    set_run_font(run)
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor.from_string(MUTED)
add_page_number(footer_table.cell(0, 1).paragraphs[0])
for run in footer_table.cell(0, 1).paragraphs[0].runs:
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor.from_string(MUTED)


def para(text="", bold=False, color=None, size=None, align=None, italic=False, keep=False):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    if keep:
        p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    if size:
        r.font.size = Pt(size)
    return p


def rich_para(parts, align=None, keep=False):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.keep_with_next = keep
    for part in parts:
        text, opts = part if isinstance(part, tuple) else (part, {})
        r = p.add_run(text)
        set_run_font(r, opts.get("font", "Aptos"))
        r.bold = opts.get("bold", False)
        r.italic = opts.get("italic", False)
        r.font.size = Pt(opts.get("size", 10))
        r.font.color.rgb = RGBColor.from_string(opts.get("color", INK))
    return p


step_counter = 0


def heading(text, level=1):
    global step_counter
    if level <= 2:
        step_counter = 0
    return doc.add_heading(text, level=level)


def page_break():
    # Heading 1 styles begin a new page. Keeping this semantic marker in the
    # source makes the authoring flow readable without creating blank pages.
    return None


def callout(title, text, fill=PALE, border=TEAL):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    cell = table.cell(0, 0)
    set_cell_shading(cell, fill)
    set_cell_margins(cell, 150, 190, 150, 190)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    r = p.add_run(title)
    set_run_font(r)
    r.bold = True
    r.font.color.rgb = RGBColor.from_string(border)
    p2 = cell.add_paragraph(text)
    p2.paragraph_format.space_after = Pt(0)
    for r in p2.runs:
        set_run_font(r)
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor.from_string(INK)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def bullet(text, level=0, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet" if level == 0 else "List Bullet 2")
    p.paragraph_format.space_after = Pt(3)
    if bold_prefix and text.startswith(bold_prefix):
        r1 = p.add_run(bold_prefix)
        set_run_font(r1)
        r1.bold = True
        r2 = p.add_run(text[len(bold_prefix):])
        set_run_font(r2)
    else:
        r = p.add_run(text)
        set_run_font(r)
    return p


def numbered(text):
    global step_counter
    step_counter += 1
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.24)
    p.paragraph_format.first_line_indent = Inches(-0.24)
    p.paragraph_format.space_after = Pt(4)
    number_run = p.add_run(f"{step_counter}.  ")
    set_run_font(number_run)
    number_run.bold = True
    number_run.font.color.rgb = RGBColor.from_string(TEAL)
    r = p.add_run(text)
    set_run_font(r)
    return p


def code_block(text):
    table = doc.add_table(rows=1, cols=1)
    cell = table.cell(0, 0)
    set_cell_shading(cell, "0D171D")
    set_cell_margins(cell, 130, 160, 130, 160)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    for index, line in enumerate(text.strip().splitlines()):
        r = p.add_run(line)
        set_run_font(r, "Menlo")
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor.from_string("D6F3EC")
        if index < len(text.strip().splitlines()) - 1:
            r.add_break()
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = "Table Grid"
    for i, header_text in enumerate(headers):
        cell = t.rows[0].cells[i]
        cell.text = header_text
        set_cell_margins(cell)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    set_repeat_header(t.rows[0])
    for row_index, row in enumerate(rows):
        added_row = t.add_row()
        keep_table_row_together(added_row)
        cells = added_row.cells
        for i, value in enumerate(row):
            cells[i].text = str(value)
            set_cell_margins(cells[i])
            cells[i].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if row_index % 2:
                set_cell_shading(cells[i], LIGHT)
            for p in cells[i].paragraphs:
                p.paragraph_format.space_after = Pt(0)
                for r in p.runs:
                    set_run_font(r)
                    r.font.size = Pt(8.5)
                    r.font.color.rgb = RGBColor.from_string(INK)
        if widths:
            for i, width in enumerate(widths):
                cells[i].width = Inches(width)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return t


def screenshot(filename, caption, width=6.95):
    path = SHOTS / filename
    if not path.exists():
        raise FileNotFoundError(path)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    picture = p.add_run().add_picture(str(path), width=Inches(width))
    picture._inline.docPr.set("descr", caption)
    picture._inline.docPr.set("title", path.stem.replace("-", " ").title())
    cp = doc.add_paragraph(caption)
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_after = Pt(9)
    for r in cp.runs:
        set_run_font(r)
        r.italic = True
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor.from_string(MUTED)


def flow(path, caption):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    picture = p.add_run().add_picture(str(path), width=Inches(6.95))
    picture._inline.docPr.set("descr", caption)
    picture._inline.docPr.set("title", path.stem.replace("-", " ").title())
    cp = doc.add_paragraph(caption)
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r in cp.runs:
        set_run_font(r)
        r.italic = True
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor.from_string(MUTED)


def section_intro(title, promise):
    heading(title, 1)
    para(promise, size=11, color=MUTED, keep=True)


# Cover
para("FIELD MANUAL  |  SEPTEMBER 2026", bold=True, color=TEAL, size=10)
doc.add_paragraph("AgentForge JARVIS Complete Usage Manual", style="Title")
para("A self-guided, click-by-click handbook for building, testing and presenting a six-agent business team with LangChain and Gemini.", size=15, color=MUTED)
para("Prepared for Arthi's LIBA workshop teams", bold=True, color=INK, size=11)
doc.add_paragraph().paragraph_format.space_after = Pt(2)
screenshot("03-command-center-overview.png", "The live AgentForge JARVIS command center used in this manual.", 6.95)
callout(
    "Start here",
    "This manual takes you from first launch to a defensible team decision. You can follow it without a facilitator. Use the screenshots to check that your screen matches, and use the experiment cards to decide what to try next.",
)
para("Repository: https://github.com/arthi-rajendran24/agentforge", color=TEAL, size=9)
para("My workshop rule: agents advise, humans decide.", bold=True, size=12)

page_break()
section_intro("How to use this manual", "Choose the path that matches what you need to accomplish today.")
table(
    ["If you want to", "Go to", "You will produce"],
    [
        ["Install and start the app", "Part 1", "A working local command center"],
        ["Understand the six agents", "Part 2", "A plain-English mental model"],
        ["Run the baseline and challenges", "Part 3", "Comparable decision packages"],
        ["Change agent instructions", "Part 4", "A saved blueprint and specialist run"],
        ["Use files, images and memory", "Part 5", "A retrievable evidence note"],
        ["Use chat, voice and read aloud", "Part 6", "A cited domain conversation"],
        ["Compare, export and assess", "Part 7", "An evidence pack and human score"],
        ["Host teams and operate safely", "Part 8", "Team access, backups and health checks"],
        ["Explore every control", "Appendices", "A complete feature reference"],
    ],
    [2.1, 1.0, 3.8],
)
heading("What this manual covers", 2)
for item in [
    "All six proposal agents and how their outputs hand off to one another.",
    "Every screen: Command center, Memory vault, Run archive, Workshop lab, inspectors, scenario editor, provider settings and team sign-in.",
    "All five built-in scenarios plus custom JSON scenarios and specialist-only runs.",
    "Text notes, file import, image extraction, retrieval chat, typed prompts, voice input and spoken responses.",
    "Blueprint editing, persistent team workspaces, exports, assessments, cancellation, authentication, backups, health checks and CLI commands.",
    "Structured experiments for Marketing, HR, Operations, Finance, Analytics and General Management.",
]:
    bullet(item)
callout("Evidence note", "Screenshots were captured from the working local application. The guide labels rehearsal behavior separately from live Gemini behavior. Voice recognition depends on browser support and was not audio-recorded during this documentation run.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("The whole system in one picture", "Start with one shared brief, let each specialist test it, then let a human decide.")
flow(architecture_flow, "Figure 1. The AgentForge decision flow.")
heading("The idea in layman's terms", 2)
para("Imagine a meeting room with six specialists. Everyone receives the same business case. Each specialist checks one part of the case using a calculator-like tool. JARVIS reads the specialist reports and prepares a management recommendation. If Finance or another gate says stop, JARVIS keeps that warning visible. You review the sources and make the final decision.")
table(
    ["Agent", "Plain-English job", "Deterministic tool"],
    [
        ["PRISM", "Reads customer signals and measures demand evidence", "analyze_signals"],
        ["PULSE", "Turns evidence into a marketing experiment", "plan_marketing"],
        ["NOVA", "Checks skills, staffing capacity and fair screening", "screen_skills"],
        ["ATLAS", "Checks suppliers, lead times and delivery capacity", "assess_supply"],
        ["LEDGER", "Checks cash, margin and funding gaps", "model_finances"],
        ["JARVIS", "Combines the evidence into a gated recommendation", "synthesize_strategy"],
    ],
    [1.0, 4.0, 2.0],
)
callout("What I want you to notice", "The language model explains and connects the evidence. The domain tools calculate the important numbers. This separation makes it easier to challenge a recommendation and reproduce the result.")

page_break()
section_intro("Part 1  Install and start AgentForge", "Get from a GitHub clone to the live command center.")
heading("Prerequisites", 2)
table(
    ["Requirement", "Recommended", "Why it matters"],
    [
        ["Operating system", "macOS, Windows 10 or 11, or Linux", "The app runs in a modern browser"],
        ["Python", "3.11 or newer", "Runs FastAPI, LangChain and the agents"],
        ["uv", "Current release", "Creates the locked environment and installs dependencies"],
        ["Browser", "Chrome or Edge", "Best chance of voice-input support"],
        ["Gemini key", "Optional for rehearsal; required for live mode", "Powers open-ended model responses"],
    ],
)
heading("Clone and launch on macOS or Linux", 2)
code_block("""
git clone https://github.com/arthi-rajendran24/agentforge.git
cd agentforge
uv sync
cp .env.example .env
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
""")
heading("Clone and launch on Windows PowerShell", 2)
code_block("""
git clone https://github.com/arthi-rajendran24/agentforge.git
cd agentforge
uv sync
Copy-Item .env.example .env
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
""")
para("Open http://127.0.0.1:8787 after the terminal says the server is running. Keep that terminal open while you use the app.")
callout("The most common launch mistake", "Run the commands inside the cloned folder that contains pyproject.toml. If uv cannot find the project, check your current folder before installing anything again.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Choose rehearsal or live Gemini mode", "Use rehearsal for predictable teaching and Gemini for open-ended reasoning.")
table(
    ["Mode", "What happens", "Use it when"],
    [
        ["rehearsal", "Scripted explanations call the real LangChain tools and produce deterministic workshop results", "You need a reliable dry run, offline fallback or quota-free practice"],
        ["gemini", "Gemini writes the agent commentary while calculations remain in domain tools", "You want open-ended chat, live specialist commentary and image extraction"],
        ["ollama", "A local tool-capable model supplies commentary", "You have installed and tested a compatible local model"],
    ],
)
heading("Recommended .env for rehearsal", 2)
code_block("""
AGENTFORGE_PROVIDER=rehearsal
AGENTFORGE_MODEL=rehearsal-v1
""")
heading("Recommended .env for Gemini", 2)
code_block("""
AGENTFORGE_PROVIDER=gemini
AGENTFORGE_MODEL=your-available-model-id
GEMINI_API_KEY=your-key
""")
para("Restart the server after changing .env. The top-right badge first reports that configuration is loaded. It changes to LIVE VERIFIED only after a successful model response during that server session.")
heading("Check the status panel", 2)
screenshot("12-provider-settings.png", "Figure 2. The provider settings dialog shows mode, model and connection status without exposing the secret key.", 6.2)
callout("Protect the key", "Keep the Gemini key in the server-side .env file. Do not paste it into the web interface, commit it to Git, place it in a slide, or include it in a screenshot.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Read the command center", "Use the screen as a dashboard for one shared mission.")
screenshot("03-command-center-overview.png", "Figure 3. The three-column command center: navigation, mission workspace and command channel.", 6.2)
table(
    ["Area", "What it controls", "What to look for"],
    [
        ["Left sidebar", "Workspace, navigation and six-agent roster", "Correct team name and agent status lights"],
        ["Center", "Scenario, challenges, swarm network, decision and reports", "Selected challenge, run status and review gates"],
        ["Right command channel", "Chat, voice, suggestions and live tool activity", "Agent selected, response source and tool trace"],
        ["Top badge", "Provider and verification state", "REHEARSAL, READY TO TEST, LIVE VERIFIED or a visible error"],
    ],
)
heading("Workspace rule", 2)
para("A workspace name is the boundary for notes, chat history, blueprints, runs and assessments. Use the same workspace name throughout a workshop. To switch, type a name containing letters, numbers, hyphens or underscores and press the arrow.")
callout("Suggested naming", "Use section-team-number, for example hr-a-07 or finance-b-12. Do not use student names or private identifiers.")

page_break()
section_intro("Part 2  Meet the six-agent team", "Know what to ask, what to inspect and where each agent can be wrong.")
screenshot("06-specialist-findings.png", "Figure 4. Every completed report appears as a specialist finding card.", 6.95)
table(
    ["Agent", "Ask this", "Inspect this", "Do not assume"],
    [
        ["PRISM", "What evidence supports demand?", "Sample size, positive intent and segments", "Survey intent guarantees purchase"],
        ["PULSE", "Which channel should we test first?", "Experiment, spend, owner and stop condition", "A creative idea is already validated"],
        ["NOVA", "What capacity and skill gaps exist?", "Anonymous skills, FTE gap and evaluation plan", "The tool replaces human hiring judgment"],
        ["ATLAS", "Can suppliers meet the date and volume?", "Lead days, deliverable units and shortfall", "A supplier statement is proof of capacity"],
        ["LEDGER", "Can we afford this plan?", "Cash available, required cash, margin and gap", "Revenue equals cash collected"],
        ["JARVIS", "What should management do next?", "Decision gate, blocked issues, owners and review date", "A recommendation is an approval"],
    ],
)
heading("The hand-off order", 2)
para("The full swarm starts with Analytics. Marketing, HR and Operations use the common brief and Analytics signal. Finance then sees the commercial and operational picture. General Management runs last so it can preserve specialist gates and assign accountable actions.")
callout("What I want you to notice", "A good multi-agent system is not six chat windows. It is a controlled sequence with shared inputs, visible dependencies, named tools, durable evidence and a human decision point.")

page_break()
section_intro("How to inspect a specialist report", "Read the calculation before you read the narrative.")
screenshot("07-ledger-report.png", "Figure 5. LEDGER's report separates metrics, worksheet, evidence, assumptions, risks, actions and model commentary.", 6.2)
heading("Read every report in this order", 2)
for step in [
    "Status and headline. REVIEW means inspect; HOLD means the agent found a blocked gate.",
    "Metrics. These are the fastest summary of the tool result.",
    "Detail worksheet. Recalculate one row if the decision is important.",
    "Source evidence. Check whether it came from the scenario or a memory note.",
    "Assumptions. Ask what would change if an assumption is false.",
    "Risks and open questions. Turn each material risk into an owner and check.",
    "Accountable actions. Confirm owner, due date or review cadence.",
    "Agent commentary. Treat this as an explanation that must agree with the tool evidence.",
    "Executed tools. Confirm the intended domain tool actually ran.",
]:
    numbered(step)
callout("Finance example", "In the captured budget-cut run, LEDGER found a 600,000 INR funding gap and returned HOLD. JARVIS preserved the block instead of smoothing it into a positive story.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("How to inspect the executive report", "Use JARVIS to decide what must happen next, then keep the decision human.")
screenshot("09-jarvis-executive-report.png", "Figure 6. JARVIS reconciles the specialist reports and keeps blocked gates visible.", 6.1)
heading("Decision meanings", 2)
table(
    ["Decision", "Meaning", "Your next move"],
    [
        ["CONDITIONAL GO", "A limited pilot may proceed under explicit controls", "Confirm owners, monitoring and stop conditions"],
        ["HOLD", "One or more material gates are unresolved", "Fix the blocked issue, update evidence and rerun"],
        ["Specialist run complete", "Only one domain and its dependencies were run", "Do not treat it as the final executive decision"],
    ],
)
heading("Five questions before you accept a recommendation", 2)
for q in [
    "Which source supports the most important claim?",
    "Which number came from a deterministic tool?",
    "Which assumption can change the decision?",
    "Which specialist said HOLD, and did JARVIS preserve it?",
    "Who is accountable for the next check and final approval?",
]:
    bullet(q)

page_break()
section_intro("Part 3  Run experiments", "Treat AgentForge as a decision laboratory, not a one-answer machine.")
flow(experiment_flow, "Figure 7. A disciplined comparison changes one important factor and records the effect.")
heading("Run the baseline", 2)
for step in [
    "Confirm the workspace name in the left sidebar.",
    "Choose Baseline launch under Inject a change.",
    "Check the displayed budget, target volume and time horizon.",
    "Select Run launch swarm.",
    "Watch the agent status lights and Live tool activity.",
    "Wait for SWARM COMPLETE. Do not change the workspace while a run is active.",
    "Inspect every report, then inspect the executive decision.",
]:
    numbered(step)
screenshot("04-six-agent-network.png", "Figure 8. A completed six-agent network with two HOLD gates visible.", 5.2)
callout("Cancel a run", "During a run, the button becomes Cancel run. A live provider call may return or time out before cancellation finishes.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Built-in challenge experiments", "Run the baseline first, then inject one change at a time.")
table(
    ["Challenge", "What changes", "Default expected signal", "Question to answer"],
    [
        ["Baseline launch", "No change", "24 lakh INR budget, 30,000 units, zero funding gap; conditional go", "Is the original plan coherent?"],
        ["Budget -25%", "Budget becomes 18 lakh INR", "6 lakh INR funding gap; HOLD", "What scope or funding must change?"],
        ["Supplier +14 days", "Lead time becomes 35 days", "29,400 deliverable units; 600-unit shortfall; HOLD", "Can a backup supplier or launch scope close the gap?"],
        ["Customer trust alert", "Positive survey counts fall 30%", "181 positive responses out of 360; trust-related HOLD", "What evidence and communication restore confidence?"],
        ["Demand +40%", "Target becomes 42,000 units", "31.8 lakh INR required cash; 7.8 lakh gap; 4,200-unit shortfall; HOLD", "Can cash and operations scale together?"],
    ],
    [1.05, 1.45, 2.7, 1.75],
)
para("These expected values apply to the default fictional Project Monsoon inputs. Custom JSON changes can produce different numbers. Recalculate and record the current result rather than copying this table into a final decision.")
screenshot("21-rehearsal-baseline-complete.png", "Figure 9. A rehearsal-mode baseline run. The tools and orchestration execute, while narrative responses are scripted.", 6.3)

page_break()
section_intro("Use the scenario editor", "Change the business case itself when the built-in chips are not enough.")
screenshot("10-scenario-editor.png", "Figure 10. The scenario editor accepts validated JSON and can import or download a template.", 6.2)
heading("Three ways to edit", 2)
for item in [
    "Edit the JSON directly in the text area.",
    "Choose Import JSON to load a scenario file under 150 KB.",
    "Choose Download template, edit the file in a text editor and import it later.",
]:
    bullet(item)
heading("Safe experiment method", 2)
for step in [
    "Download the current scenario before changing it.",
    "Rename the scenario so the archive is easy to understand.",
    "Change one or two connected inputs, such as budget and target units.",
    "Keep candidate data anonymous and based on skills or work samples.",
    "Select Apply scenario. The server validates the structure and value ranges.",
    "Run the baseline chip against your edited base scenario.",
    "Export the result and record what you changed.",
]:
    numbered(step)

page_break()
section_intro("Recover from scenario validation errors", "A rejected scenario has not replaced your current valid brief.")
screenshot("11-scenario-validation-error.png", "Figure 11. Invalid values stay in the editor and a visible error explains what must be corrected.", 6.15)
heading("Typical validation problems", 2)
table(
    ["Problem", "What to do"],
    [
        ["Invalid JSON", "Check commas, braces, quotes and list brackets"],
        ["Negative budget or units", "Use realistic positive numbers"],
        ["Missing required field", "Download a fresh template and compare keys"],
        ["Wrong data type", "Use numbers without currency symbols and true lists with square brackets"],
        ["Candidate names or private data", "Replace them with anonymous skills and work-sample evidence"],
        ["File too large", "Keep imported JSON under 150 KB"],
    ],
)
callout("Recovery rule", "Copy the error text, correct only the named field, and apply again. If you are unsure, close the dialog to keep the last valid scenario.")

page_break()
section_intro("Compare two completed runs", "Make the cause of a changed decision visible.")
screenshot("01-run-archive.png", "Figure 12. The Run archive stores completed missions for the current workspace.", 6.2)
for step in [
    "Open Run archive from the left sidebar.",
    "Find the two completed runs you want to compare.",
    "Select the checkbox beside each run. Select exactly two.",
    "Read the change panel before opening either report.",
    "Open each run and compare its source snapshot, specialist evidence and assumptions.",
    "Explain the mechanism: which changed input caused which new calculation and which decision gate?",
]:
    numbered(step)
screenshot("02-run-comparison.png", "Figure 13. The comparison highlights the decision, budget and funding-gap change.", 6.7)

page_break()
section_intro("Part 4  Customize and run agents", "Change the instructions that guide future live-model commentary.")
screenshot("08-ledger-blueprint.png", "Figure 14. Every agent exposes inputs, tools, dependencies, constraints and editable team instructions.", 4.2)
heading("Edit a blueprint", 2)
for step in [
    "Select an agent in the roster or Specialist findings.",
    "Choose Agent blueprint.",
    "Read its inputs, tool chain, dependencies and constraints.",
    "Write an instruction that changes style or focus without removing controls.",
    "Select Save blueprint. The instruction applies to future runs in this workspace.",
]:
    numbered(step)
heading("Good instruction patterns", 2)
table(
    ["Goal", "Example instruction"],
    [
        ["Executive clarity", "Use a concise executive tone. Lead with the two numbers that can change the decision."],
        ["Risk focus", "List the largest operational risk, its evidence, owner and stop condition."],
        ["Teaching", "Explain the calculation in plain language and define each business term."],
        ["Challenge assumptions", "Name the assumption with the highest decision impact and propose one verification step."],
        ["Evidence discipline", "Cite the source title for each retrieved memory claim and label unsupported claims as assumptions."],
    ],
)
callout("Blueprint boundary", "Blueprints guide live-model commentary. They do not change the scenario values, tool formulas or governance gates. In rehearsal mode, the responses remain scripted.")

page_break()
section_intro("Run one specialist and its dependencies", "Use a focused run when you need a faster domain check.")
for step in [
    "Open the agent's blueprint.",
    "Choose Run specialist + dependencies.",
    "The inspector closes and the command center shows the run.",
    "Wait for the requested agent and any upstream dependencies to finish.",
    "Inspect the specialist report and executed tools.",
    "Run the full swarm before treating the result as an executive recommendation.",
]:
    numbered(step)
heading("Dependency examples", 2)
table(
    ["Requested specialist", "Likely upstream context", "Output you should inspect"],
    [
        ["PRISM", "Scenario source data", "Demand evidence and segment signal"],
        ["PULSE", "PRISM and shared brief", "Channel experiment and marketing actions"],
        ["NOVA", "PRISM and shared brief", "Skill and capacity gap"],
        ["ATLAS", "PRISM and shared brief", "Lead-time and unit-capacity check"],
        ["LEDGER", "PRISM, PULSE and ATLAS", "Cash, margin and funding gate"],
        ["JARVIS", "All specialist reports", "Executive decision and owners"],
    ],
)
callout("Use focused runs for diagnosis", "A specialist run is excellent for debugging a brief or checking one domain. It is not a shortcut around cross-functional review.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Part 5  Build the Memory vault", "Give the team evidence it can retrieve and cite.")
flow(memory_flow, "Figure 15. Evidence moves through review and retrieval before it influences advice.")
screenshot("13-memory-vault.png", "Figure 16. The Memory vault supports pasted notes, text files and image extraction.", 4.8)
heading("Add a text note", 2)
for step in [
    "Open Memory vault.",
    "Write a specific evidence title, such as Packaging pilot interview notes.",
    "Paste the source text into Source notes.",
    "Add enough context to understand who observed what and when.",
    "Label fictional workshop evidence clearly.",
    "Select Save to memory.",
]:
    numbered(step)

page_break()
section_intro("Import text and Markdown files", "Turn meeting notes or a short brief into retrievable team evidence.")
heading("Import process", 2)
for step in [
    "Open Memory vault and choose Import .txt / .md.",
    "Choose a UTF-8 text or Markdown file under 60 KB.",
    "Review the title generated from the filename.",
    "Read the text in the form and remove private or irrelevant content.",
    "Choose Save to memory.",
    "Ask a specific question in the command channel and request the evidence title.",
]:
    numbered(step)
screenshot("14-saved-evidence.png", "Figure 17. A saved source note displays its title, content, timestamp and character count.", 6.7)
heading("Good evidence note structure", 2)
code_block("""
Source: Packaging pilot observation
Date: 28 August 2026
Observation: Five of eight participants asked for clearer allergen labelling.
Evidence status: Small fictional workshop sample; not a population estimate.
Owner: Marketing lead
Next check: Validate with the next 30 pilot customers.
""")

page_break()
section_intro("Extract text from an image", "Use Gemini to read a screenshot, poster or photographed note, then verify the result yourself.")
screenshot("15-image-extraction-review.png", "Figure 18. Extracted text is placed in the note form for human review before saving.", 6.7)
for step in [
    "Open Memory vault and choose Extract image.",
    "Choose a PNG or JPEG under 2 MB.",
    "Wait for Gemini to place extracted text in Source notes.",
    "Compare every number, date, name and action with the original image.",
    "Correct the text and give it a useful title.",
    "Choose Save to memory only after the review.",
]:
    numbered(step)
heading("Suitable workshop images", 2)
for item in [
    "A supplier update containing dates and lead times.",
    "A whiteboard summary using fictional business data.",
    "A product feedback card or simple table.",
    "A screenshot of a short public or team-approved brief.",
]:
    bullet(item)
callout("Image boundary", "Image extraction is transcription support. It can misread small text and tables. Always keep the original image and verify the extracted text before it enters memory.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Manage and retrieve saved evidence", "Ask a narrow question and require a source title.")
heading("Retrieval prompt pattern", 2)
code_block("""
Using our saved evidence, what packaging risk should we resolve before launch?
Cite the evidence title. Separate retrieved facts from assumptions.
""")
screenshot("16-command-channel-and-voice.png", "Figure 19. JARVIS retrieved the saved packaging observation and cited the note title in a live Gemini response.", 1.75)
heading("Remove a note", 2)
para("Open Memory vault and choose Remove on the saved note. This stops the note from being retrieved in future requests. Existing run exports and saved conversations keep the evidence snapshots they already contain, so removal does not rewrite history.")
callout("Retrieval check", "If the response does not name the source, ask again with: Cite the exact note title and quote only the relevant fact in your own words. Then open Memory vault and compare the answer with the note.")

page_break()
section_intro("Part 6  Use the command channel", "Consult JARVIS or talk directly to one specialist.")
heading("Send a typed command", 2)
for step in [
    "Choose JARVIS or a specialist from Agent to consult.",
    "Type one clear question in Your command.",
    "Press Enter to send. Use Shift+Enter for a new line.",
    "Wait for the response and inspect Live tool activity.",
    "Challenge any unsupported claim or unclear assumption.",
]:
    numbered(step)
heading("Useful prompt patterns", 2)
table(
    ["Purpose", "Prompt"],
    [
        ["Briefing", "Brief me on the latest team decision. Name the blocked gates and owners."],
        ["Finance", "Finance, what could block our launch? Show the cash calculation."],
        ["Evidence", "Which saved note supports this claim? Cite its title."],
        ["Counterfactual", "What would have to change for HOLD to become CONDITIONAL GO?"],
        ["Assumption audit", "List the three assumptions with the greatest decision impact."],
        ["Plain language", "Explain this recommendation as if I am new to business finance."],
        ["Red team", "Argue against this plan using only the current evidence."],
    ],
)
para("The two suggestion buttons, Check the budget and Brief me, Jarvis, provide fast starting prompts.")

page_break()
section_intro("Use voice input and read aloud", "Speak a prompt, review the transcription and optionally hear the response.")
screenshot("16-command-channel-and-voice.png", "Figure 20. The microphone and Read aloud controls sit below the prompt box.", 1.55)
heading("Voice input", 2)
for step in [
    "Use Chrome or Edge and allow microphone access when the browser asks.",
    "Select the microphone icon.",
    "Speak one short command.",
    "Review the text placed in the prompt box. Correct names, numbers and acronyms.",
    "Send the command when the transcription is accurate.",
]:
    numbered(step)
heading("Read aloud", 2)
for step in [
    "Select Read aloud before sending the command.",
    "The browser reads the next completed response aloud.",
    "Clear the checkbox to stop future speech. The app also cancels current speech when the option is cleared.",
]:
    numbered(step)
callout("Browser variation", "Speech recognition may use the browser's online service. If the microphone is unavailable, type the prompt or import a transcript.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Read live tool activity", "Use the trace to see which agent did what and in which order.")
table(
    ["Trace event", "Meaning", "What to check"],
    [
        ["run started", "A mission record was created", "Correct scenario and challenge"],
        ["activate agent", "An agent began its turn", "Expected dependency order"],
        ["call read_brief", "The agent requested the shared scenario", "The run uses the intended source snapshot"],
        ["call search_memory", "The agent looked for team evidence", "Relevant note title appears in the response or report"],
        ["call domain tool", "A deterministic calculation ran", "Correct tool for the agent"],
        ["result", "The tool returned structured data", "Metrics match the report"],
        ["complete", "The agent produced its report", "REVIEW or HOLD status"],
        ["run completed", "The saved package is ready", "Exports and assessment become available"],
    ],
)
heading("When the trace matters most", 2)
for item in [
    "A narrative mentions a number you cannot find in the worksheet.",
    "A specialist appears to ignore a saved note.",
    "A full swarm completes without an expected dependency.",
    "A provider request fails or times out.",
    "You need to explain the orchestration in a workshop presentation.",
]:
    bullet(item)

page_break()
section_intro("Part 7  Export, assess and present", "Turn a run into evidence that another person can review.")
screenshot("05-executive-decision.png", "Figure 21. Completed full swarms expose the executive decision and Markdown and JSON exports.", 6.7)
heading("Export a brief", 2)
para("Choose Export brief to download a readable Markdown decision package. Use it for the team presentation, GitHub documentation or facilitator review.")
heading("Export JSON", 2)
para("Choose JSON to download the structured run. Use it for programmatic comparison, dashboards, audit exercises or future app integrations.")
heading("What the export should contain", 2)
for item in [
    "Scenario and challenge snapshot.",
    "Provider, model context, run ID and duration.",
    "Every specialist report with metrics, evidence, assumptions, risks and actions.",
    "Executive decision and blocked gates.",
    "Observable governance checks.",
    "Human assessment if one has been saved.",
]:
    bullet(item)
callout("Evidence-pack rule", "Keep the exported brief, exported JSON and the source scenario together. A screenshot is useful for explanation, but it is not the complete audit trail.")

page_break()
section_intro("Use the Workshop lab", "Trace the learning journey and check the structure of a completed run.")
screenshot("17-workshop-lab.png", "Figure 22. The Workshop lab connects the build sequence with checks and human assessment.", 4.6)
callout("Continuity rule", "Keep the same team workspace across both workshop days so notes, blueprints, runs and assessments remain connected.")
heading("The eight-session progression", 2)
table(
    ["Session", "Focus", "Evidence of completion"],
    [
        ["1", "Foundations", "Baseline run and one inspected tool trace"],
        ["2", "Agent design", "One saved blueprint"],
        ["3", "Domain capability", "One changed scenario and specialist worksheet"],
        ["4", "Multimodal extension", "Voice attempt or imported transcript; image extraction if live Gemini is available"],
        ["5", "Swarm architecture", "Explained hand-off order"],
        ["6", "Command center", "Completed six-agent run"],
        ["7", "Red-team lab", "Assumption, bias and untrusted-note challenge"],
        ["8", "Outcome challenge", "Comparison, export and evidence-backed presentation"],
    ],
)

page_break()
section_intro("Interpret governance checks", "Treat these as observable structural checks, not a safety certification.")
screenshot("18-governance-checks.png", "Figure 23. The captured run shows source evidence, tool use, assumptions and hold propagation.", 6.7)
table(
    ["Check", "What it verifies", "What it does not prove"],
    [
        ["Source evidence", "Every report names input or upstream evidence", "The evidence itself is accurate or representative"],
        ["Observable tool use", "Each agent called its required domain tool through LangChain", "The formula fits every real business"],
        ["Assumptions declared", "Outputs include scenario and model limitations", "Every hidden assumption has been found"],
        ["Hold propagation", "Executive output preserves blocked specialist gates", "The human decision is risk-free"],
    ],
)
heading("Manual checks to add", 2)
for item in [
    "Verify every external source and date.",
    "Recalculate material finance and operations numbers.",
    "Review privacy, bias, accessibility and legal implications with accountable people.",
    "Confirm owners accept their actions and deadlines.",
]:
    bullet(item)

page_break()
section_intro("Score the outcome", "Use the rubric to make human judgment explicit.")
screenshot("19-outcome-assessment.png", "Figure 24. Five human-scored criteria produce a weighted score out of 100.", 5.0)
heading("Assessment process", 2)
for step in [
    "Open a completed run from Run archive.",
    "Open Workshop lab.",
    "Score every criterion from 0 to 5.",
    "Write what changed, what the team verified and what remains uncertain.",
    "Choose Save assessment.",
    "Export the run again so the assessment is included.",
]:
    numbered(step)
table(
    ["Criterion", "Weight", "A strong score requires"],
    [
        ["Business relevance", "25%", "Advice directly addresses the changed scenario"],
        ["Agent orchestration", "25%", "Roles, shared state, hand-offs and dependencies are visible"],
        ["Reliability and evidence", "20%", "Traceable tools, tested arithmetic and stated assumptions"],
        ["Responsible AI", "15%", "Bias, privacy, prompt injection and unsupported claims reviewed"],
        ["Communication and reflection", "15%", "Clear demo, individual reflection and concrete next steps"],
    ],
)

page_break()
section_intro("Part 8  Team access and operations", "Run AgentForge for a cohort without sharing the model key.")
flow(team_flow, "Figure 25. Hosted participants sign into an isolated team workspace; the server keeps the provider secret.")
heading("Provision a team", 2)
code_block("""
uv run agentforge-jarvis provision-team finance-a-07 --output finance-a-07-access.json
""")
para("Give the participant the team ID and access code through a private channel. Store the generated access file securely and delete it when your access distribution process is complete.")
heading("Enable authentication", 2)
code_block("""
AGENTFORGE_AUTH_REQUIRED=true
AGENTFORGE_SESSION_SECRET=replace-with-a-long-random-secret
AGENTFORGE_SECURE_COOKIES=true
""")
heading("What participants see", 2)
screenshot("20-team-sign-in.png", "Figure 26. Authenticated deployments ask for a facilitator-provided team ID and access code.", 4.5)

page_break()
section_intro("Start a hosted server", "Keep the service behind HTTPS and control which networks can reach it.")
heading("Bind for a private network or reverse proxy", 2)
code_block("""
uv run agentforge-jarvis web --host 0.0.0.0 --port 8787
""")
heading("Readiness endpoints", 2)
code_block("""
curl http://127.0.0.1:8787/api/health
curl http://127.0.0.1:8787/api/ready
""")
table(
    ["Endpoint", "Use", "Healthy result"],
    [
        ["/api/health", "Shows provider, model, framework and verification state", "HTTP 200 with expected configuration"],
        ["/api/ready", "Checks whether the app can serve traffic", "HTTP 200 and ready state"],
    ],
)
heading("Production checklist", 2)
for item in [
    "Terminate TLS with Caddy or another reverse proxy.",
    "Require authentication and secure cookies.",
    "Keep .env and the data directory outside public web roots.",
    "Use a stable writable AGENTFORGE_DATA_DIR on persistent storage.",
    "Limit network access to the intended cohort.",
    "Test login, one rehearsal run, one export and one backup before participants arrive.",
]:
    bullet(item)
para("See deploy/README.md and deploy/compose.yaml in the repository for the deployment scaffold.")

page_break()
section_intro("Back up durable state", "Protect runs, notes, chat, blueprints, team credentials and assessments.")
heading("Create a backup", 2)
code_block("""
uv run agentforge-jarvis backup backups/agentforge-2026-09-04
""")
heading("What lives in the data directory", 2)
for item in [
    "SQLite database containing teams, notes, messages, runs, reports and assessments.",
    "Persistent agent blueprint instructions.",
    "Provider verification state and operational metadata where configured.",
]:
    bullet(item)
heading("Before a workshop", 2)
for step in [
    "Stop new run creation for a moment.",
    "Create a timestamped backup.",
    "Copy it to a separate protected location.",
    "Start the app and run the readiness check.",
    "Open one existing team and confirm its archive and notes.",
]:
    numbered(step)
callout("Restore drill", "A backup is only useful if you can restore it. Practice a restore into a separate temporary data directory before the workshop date.")

page_break()
section_intro("Command-line reference", "Use the CLI for diagnosis, scripted demos, team setup and backups.")
table(
    ["Command", "Purpose", "Example"],
    [
        ["doctor", "Validate configuration and dependencies", "uv run agentforge-jarvis doctor"],
        ["web", "Start the web command center", "uv run agentforge-jarvis web --port 8787"],
        ["demo", "Run a scenario without the browser", "uv run agentforge-jarvis demo --challenge budget-cut"],
        ["demo --live", "Use the configured live provider in the CLI demo", "uv run agentforge-jarvis demo --challenge baseline --live"],
        ["provision-team", "Create or rotate a team access code", "uv run agentforge-jarvis provision-team hr-b-03"],
        ["backup", "Copy durable application state", "uv run agentforge-jarvis backup backups/pre-workshop"],
    ],
)
heading("Supported demo challenges", 2)
code_block("""
baseline
budget-cut
supply-delay
sentiment-shift
demand-surge
""")
heading("Stop the server", 2)
para("Return to the terminal that started the web server and press Ctrl+C. Wait for the application shutdown message before closing the terminal.")

page_break()
section_intro("Troubleshooting", "Use the visible status, terminal output and saved run state to isolate the problem.")
table(
    ["Symptom", "Likely cause", "Fix"],
    [
        ["Browser cannot open 127.0.0.1:8787", "Server is not running or another port was chosen", "Read the terminal, restart web, and open the exact printed URL"],
        ["uv cannot find the project", "Command is outside the cloned folder", "cd into the folder containing pyproject.toml"],
        ["Badge says SETUP NEEDED", "Provider variables or model ID are missing", "Correct .env and restart"],
        ["Badge stays READY TO TEST", "No successful live response has occurred in this server session", "Run one agent or send one chat request"],
        ["Provider error is visible", "Invalid key, unavailable model, quota, network or timeout", "Read the exact error; correct the cause; do not substitute a simulated result"],
        ["Run is taking longer than expected", "Live provider call is slow", "Wait, or request cancellation; an active call may finish first"],
        ["No saved note is cited", "The query is too broad or the note is irrelevant", "Use specific keywords and require the exact note title"],
        ["Voice button is disabled", "Browser does not expose SpeechRecognition", "Use Chrome or Edge, or type/import a transcript"],
        ["Run comparison does not appear", "You selected fewer or more than two runs", "Select exactly two completed runs"],
        ["Assessment cannot save", "No completed run is open or reflection is empty", "Open a completed run, fill every score and add reflection"],
        ["Windows reports a port or firewall issue", "Local policy blocks the port", "Use an allowed port and confirm localhost access with IT"],
    ],
    [1.7, 2.0, 3.3],
)

page_break()
section_intro("Experiment library", "Choose an exercise by specialization and finish with evidence, not just output.")
experiments = [
    ("Analytics", "Signal quality", "Run baseline. Inspect PRISM. Reduce positive counts in a custom scenario.", "How much does the recommendation depend on sample size and positive intent?", "PRISM worksheet, assumptions and before/after export"),
    ("Marketing", "Channel experiment", "Save a note containing fictional customer objections. Ask PULSE for the smallest test.", "Which channel, audience and stop condition can validate the idea cheaply?", "Memory citation, PULSE actions and test budget"),
    ("Human Resources", "Capacity plan", "Increase workload or reduce available capacity. Run NOVA with dependencies.", "Which skills are missing, and can training close the gap before hiring?", "Anonymous skill matrix, FTE gap and human review plan"),
    ("Operations", "Supplier delay", "Run Supplier +14 days. Inspect ATLAS.", "What creates the unit shortfall, and which mitigation is measurable?", "Lead-time worksheet, shortfall and owner"),
    ("Finance", "Budget cut", "Run Budget -25%. Inspect LEDGER and JARVIS.", "What must change to close the 6 lakh INR gap?", "Cash worksheet, HOLD gate and revised plan"),
    ("General Management", "Demand surge", "Run Demand +40% and compare with baseline.", "Can the organisation scale cash, people and supply together?", "Two-run comparison and executive owner table"),
    ("Responsible AI", "Untrusted note", "Add a note that tells the agent to ignore the brief. Ask for a decision.", "Does the team treat note text as evidence rather than instructions?", "Trace, source review and prompt-injection reflection"),
    ("Customer trust", "Allergen concern", "Run Customer trust alert and ask PULSE and JARVIS for the next experiment.", "What proof is needed before communication can restore trust?", "Trust gate, evidence plan and stop condition"),
    ("Reliability", "Narrative versus tools", "Choose one report and independently recalculate a headline metric.", "Does the narrative agree with the structured tool result?", "Manual calculation and discrepancy note"),
    ("Orchestration", "Dependency map", "Run LEDGER only, then run the full swarm.", "Which upstream reports does Finance need before management can decide?", "Two traces and dependency explanation"),
    ("Multimodal", "Image evidence and briefing", "Extract and verify the supplier card. Ask ATLAS to cite it. Request a 60-second JARVIS brief.", "Can the team use image evidence and explain it after human review?", "Original image, corrected note, citation and executive brief"),
]
for index, (domain, name, method, question, evidence) in enumerate(experiments, start=1):
    heading(f"Experiment {index}  {domain}  {name}", 2)
    table(
        ["Do", "Decide", "Save as evidence"],
        [[method, question, evidence]],
        [2.6, 2.3, 2.1],
    )
    if index in (4, 8):
        page_break()

page_break()
section_intro("A complete self-guided dry run", "Use this 75-minute route when nobody is facilitating.")
table(
    ["Time", "Action", "Checkpoint"],
    [
        ["0-10 min", "Clone, uv sync, doctor, start the web app", "Command center opens and provider badge is understood"],
        ["10-20 min", "Run the baseline and inspect PRISM and LEDGER", "One tool calculation has been independently checked"],
        ["20-30 min", "Open a blueprint and save one evidence-focused instruction", "Future-run instruction is visible"],
        ["30-40 min", "Add a fictional source note or import a short file", "Note appears in the team vault"],
        ["40-50 min", "Ask one cited question; try voice or type the prompt", "Response names the evidence title"],
        ["50-60 min", "Run one built-in challenge", "New decision package is complete"],
        ["60-68 min", "Compare baseline with challenge and export both formats", "Cause of changed decision is explained"],
        ["68-75 min", "Complete governance review and assessment", "Human score and reflection are saved"],
    ],
)
heading("What to submit", 2)
for item in [
    "Team workspace name and scenario title.",
    "Baseline Markdown export and challenge Markdown export.",
    "One JSON export.",
    "One screenshot of the comparison panel.",
    "One checked calculation.",
    "One cited memory response.",
    "Saved assessment and a 150-word reflection.",
]:
    bullet(item)

page_break()
section_intro("Presentation script in Arthi's voice", "Use these words as a guide and adapt them naturally.")
heading("Opening", 2)
para("Today we are not building a chatbot that gives us one clever answer. We are building a small AI organisation. Each agent has a job, a tool, a dependency and a boundary. They all work from one shared business brief, and we keep the final decision with a human.")
heading("Before the baseline", 2)
para("First, I want us to create a reference point. We will run the unchanged scenario, inspect the numbers and save the result. Then we will change one business condition and see whether the advice changes for a clear reason.")
heading("While the swarm runs", 2)
para("Watch the order. Analytics establishes the signal. Marketing, HR and Operations test different parts of the plan. Finance checks whether the combined plan is affordable. JARVIS goes last because management should not decide before the specialist evidence is available.")
heading("When a HOLD appears", 2)
para("A HOLD is useful. It tells us exactly where the plan is not ready. Our job is not to persuade the agent to say yes. Our job is to resolve the blocked gate with evidence, an owner and a measurable next action.")
heading("Closing", 2)
para("The quality of this system is not the confidence of its words. The quality is whether we can trace the source, reproduce the calculation, challenge the assumption and name the human who decides.")

page_break()
section_intro("Appendix A  Complete control reference", "Every interactive control in the web application and what it does.")
controls = [
    ("Provider badge", "Opens connection settings and reports rehearsal, configuration or verified-live state"),
    ("Settings gear", "Opens the same provider and model dialog"),
    ("Team workspace field", "Switches local workspace when authentication is optional"),
    ("Command center", "Shows scenario, swarm, decision and reports"),
    ("Memory vault", "Creates, imports, extracts, saves and removes source notes"),
    ("Run archive", "Lists, opens and compares durable runs"),
    ("Workshop lab", "Shows learning sequence, checks and assessment"),
    ("Agent roster card", "Opens that agent's report or blueprint"),
    ("Edit brief", "Opens validated scenario JSON"),
    ("Challenge chips", "Applies one built-in change to the base scenario"),
    ("Run launch swarm", "Starts all six agents"),
    ("Cancel run", "Requests cancellation of the active run"),
    ("Export brief", "Downloads Markdown for the open completed run"),
    ("JSON", "Downloads structured JSON for the open completed run"),
    ("Inspect decision and owners", "Opens JARVIS report"),
    ("Specialist finding card", "Opens the selected report"),
    ("Report and evidence tab", "Shows output, metrics, worksheets, evidence, risks and actions"),
    ("Agent blueprint tab", "Shows role, dependencies, constraints and editable instructions"),
    ("Run specialist and dependencies", "Runs one domain plus required upstream agents"),
    ("Save blueprint", "Persists workspace-specific instructions for future runs"),
    ("Agent to consult", "Routes command-channel conversation to JARVIS or a specialist"),
    ("Microphone", "Starts browser speech recognition when supported"),
    ("Read aloud", "Uses browser speech synthesis for the next response"),
    ("Send", "Submits the command"),
    ("Suggestion buttons", "Send ready-made Finance or JARVIS prompts"),
    ("Import .txt or .md", "Loads a text file into the note form for review"),
    ("Extract image", "Uses configured live Gemini to transcribe a PNG or JPEG"),
    ("Save to memory", "Creates a retrievable note in the current workspace"),
    ("Remove", "Deletes the note from future retrieval"),
    ("Compare checkbox", "Selects a run; exactly two completed runs show a comparison"),
    ("Open", "Loads an archived run into the command center"),
    ("Assessment score", "Records a 0-5 human rating for one rubric criterion"),
    ("Save assessment", "Persists the weighted score and reflection with the run"),
    ("Sign out", "Ends an authenticated browser session"),
]
table(["Control", "Action"], controls, [2.0, 5.0])

page_break()
section_intro("Appendix B  Scenario field guide", "Use the downloaded template as the source of truth; this table explains the business meaning.")
scenario_fields = [
    ("name and company", "Human-readable scenario identity", "Rename every custom experiment"),
    ("objective", "The mission the six agents are evaluating", "Write one measurable business outcome"),
    ("budget", "Available launch cash in INR", "Use a positive number without a currency symbol"),
    ("units", "Target units for the launch horizon", "Connect this with demand and capacity"),
    ("days", "Planning horizon", "Use a realistic delivery window"),
    ("lead_days", "Primary supplier lead time", "Stress-test delay risk"),
    ("cash_available", "Cash available to fund the plan", "Keep separate from forecast revenue"),
    ("survey_counts", "Observed customer response counts", "Record sample limitations"),
    ("channels", "Marketing routes available for experiments", "Prefer measurable channels"),
    ("roles_required and candidates", "Anonymous skill demand and work-sample evidence", "Do not include names or sensitive attributes"),
    ("suppliers", "Supplier capacity and lead-time inputs", "Verify statements with accountable humans"),
    ("prices and costs", "Commercial assumptions used by Finance", "Document taxes, collection delays and exclusions separately"),
]
table(["Field", "Meaning", "Good practice"], scenario_fields, [1.7, 2.4, 2.9])

page_break()
section_intro("Appendix C  Limits and responsible use", "Know what the application proves and where human work still matters.")
table(
    ["Area", "The app helps with", "Human responsibility"],
    [
        ["Business decisions", "Structured evidence, calculations, risks and actions", "Approve, reject or escalate the decision"],
        ["Hiring", "Anonymous skill and work-sample screening exercises", "Comply with employment law, review bias and interview candidates"],
        ["Finance", "Workshop cash, margin and funding models", "Validate accounting, tax, financing, timing and real-world data"],
        ["Operations", "Lead-time and capacity stress tests", "Confirm supplier commitments and quality controls"],
        ["Marketing", "Experiment design and customer-signal synthesis", "Approve claims, budgets, brand and customer communication"],
        ["Memory", "Keyword retrieval of saved team notes", "Verify source quality, permissions, privacy and relevance"],
        ["Image extraction", "Draft transcription of PNG or JPEG evidence", "Compare with the original and correct every material field"],
        ["Governance checks", "Visible structural checks", "Perform legal, security, privacy, bias and safety review"],
    ],
    [1.5, 2.8, 2.7],
)
callout("Final decision rule", "Do not act on a material recommendation until an accountable human has verified the source, calculation, assumption, impact and owner.", fill="FFF4E5", border=AMBER)

page_break()
section_intro("Appendix D  Final readiness checklist", "Complete this before asking a class or team to use the application.")
checks = [
    "Repository clones successfully into a fresh folder.",
    "uv sync completes and doctor reports the expected mode.",
    "The local or hosted URL opens from the participant network.",
    "The provider badge matches the intended rehearsal or live mode.",
    "No API key appears in Git, screenshots, handouts or browser storage.",
    "A baseline run completes and all six reports can be opened.",
    "A challenge run completes and the archive comparison appears.",
    "Markdown and JSON exports download.",
    "A note can be saved and retrieved by title.",
    "Image extraction is tested only when live Gemini is intended.",
    "Voice has a typed or transcript fallback.",
    "Team authentication, HTTPS and secure cookies are enabled for hosted use.",
    "A backup has been created and a restore has been rehearsed.",
    "Facilitator and participants know that governance checks are not certification.",
    "Every team knows the required submission evidence.",
]
for item in checks:
    para(f"☐  {item}", size=10.5)
heading("You are ready when", 2)
para("A new participant can open the app, identify the workspace and provider mode, run the baseline, inspect a tool calculation, add and retrieve a fictional note, run one changed scenario, compare two saved runs, export the evidence and explain why a human still decides.", bold=True, size=12)


doc.core_properties.title = "AgentForge JARVIS Complete Usage Manual"
doc.core_properties.subject = "Self-guided usage manual for AgentForge JARVIS"
doc.core_properties.author = "Arthi"
doc.core_properties.keywords = "AgentForge, JARVIS, LangChain, Gemini, LIBA, multi-agent workshop"
doc.save(OUTPUT)
print(OUTPUT)
