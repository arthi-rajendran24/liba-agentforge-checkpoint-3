# Arthi's GitHub publishing and clone checklist

Publish the **agentforge-jarvis project folder itself**. It contains `pyproject.toml`, the application, tests, first-agent lab, slides and handouts. Do not publish the parent workspace containing unrelated proposals and apps. Target repository: [arthi-rajendran24/agentforge](https://github.com/arthi-rajendran24/agentforge). Use this checklist when publishing or updating the workshop source.

## 1. Prepare the project

Open a terminal in the folder containing `pyproject.toml` and check:

```sh
uv sync --frozen
uv run pytest -q
uv run python workshop/first_agent_live.py
uv run agentforge-jarvis doctor
```

Configure live Gemini privately as shown in LIVE_QUICKSTART.md before the live commands. Include the Main Workshop deck, LIVE_QUICKSTART.md, MAIN_FACILITATOR_GUIDE.md and TEAM_WORKBOOK.md in `workshop/`. `.gitignore` already excludes `.env`, `.venv`, `.agentforge`, caches and build output. Review any other files you add before sharing them.

## 2. Create an empty remote

In GitHub, create a new repository under the account or organization you intend to use. Choose visibility and access deliberately. Leave README, license and .gitignore initialization unchecked because this project already supplies its files. Copy the new repository's HTTPS URL. If it is private, invite the LIBA participants before the session.

## 3. Commit locally

For a new standalone copy without Git history (skip initialization for an existing clone):

```sh
git init -b main
git add .
git status --short
git diff --cached --stat
```

Read the staged-file list. Confirm there are no API keys, private notes, database files or unrelated parent folders. Then:

```sh
git commit -m "Add AgentForge JARVIS and LIBA live workshop kit"
```

If Git asks for your identity, configure your own Git name and email following your organization's policy; do not use someone else's identity. If you already initialized the folder, inspect the current history/remotes instead of starting over.

## 4. Set the actual remote and push

macOS Terminal:

```sh
printf 'Paste the empty repository HTTPS URL: '
read REPO_URL
git remote add origin "$REPO_URL"
git remote -v
git push -u origin main
```

Windows PowerShell:

```powershell
$repoUrl = Read-Host "Paste the empty repository HTTPS URL"
git remote add origin $repoUrl
git remote -v
git push -u origin main
```

Use GitHub's supported authentication flow if prompted. If `origin` already exists, inspect it before changing anything. If push is rejected because the remote has commits, do not force-push: use a new empty repository or deliberately reconcile its history.

## 5. Verify a fresh clone before sharing

From a different empty parent folder, follow the exact clone commands in LIVE_QUICKSTART.md using the newly published URL. Then:

```sh
cd agentforge-jarvis
uv sync --frozen
uv run pytest -q
uv run python workshop/first_agent_live.py
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
```

In the fresh clone, configure your approved Gemini key in its own ignored .env before doctor/web. Use a different port if your original app is still running. Open the browser, run the baseline, confirm the workshop deck exists and verify participant access if private. These checks establish the path learners will actually use.

Only then send the actual HTTPS clone URL and LIVE_QUICKSTART.md to the team. No placeholder URL in the deck needs to be guessed. A successful local commit does not prove a push or participant clone succeeded.

## Suggested session message (copy and complete yourself)

> Today we'll build AgentForge JARVIS in pairs using live Gemini and LangChain. Install Git and uv beforehand using the attached quickstart. Bring your laptop, charger and an editor. I will share the tested repository's HTTPS clone link here. We will complete one LangChain agent, adapt six specialists, run a launch challenge, and export our evidence. Bring approved Gemini API access for your local coding lab, or confirm your assigned hosted access and pair arrangement with me. Package installation and live Gemini calls need internet. Follow our staggered run schedule.

References: [GitHub cloning instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository), [project README](../README.md).
