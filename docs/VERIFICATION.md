# Verification record — live Gemini edition

Verified locally on 3 September 2026 on macOS with Python 3.12.12. Dependencies are pinned in uv.lock. This record supersedes the earlier rehearsal-only status.

## Real Gemini acceptance

Using the privately configured credential and **gemini-3.1-flash-lite**:

- All six specialists completed the baseline: funding gap 0; executive decision CONDITIONAL GO.
- All six completed Budget −25%: funding gap INR 600000; Finance and General Management HOLD.
- Every accepted specialist report included executed brief, domain and memory tools. The tool calculations and model narrative are distinct report fields.
- A live command-channel answer retrieved and cited the saved Packaging review note and named Mira.
- A saved Analytics blueprint required PRISM WORKSHOP BRIEF; Gemini followed the heading instruction.
- The completed first-agent lab executed estimate_launch_cash through LangChain and Gemini: cash 2400000, gap0, human review required. A completed budget-cut starter also ran live from the clean install: cash2400000, gap600000, HOLD.
- The live image API read the fictional slide's 24 lakh budget, 30000 units, 84 days and price120/unit cost65. Response status200 and saved=false confirmed explicit review-before-save.

Detailed sanitized records: examples/live-verification.json, examples/live-image-verification.json, examples/live-browser-verification.json.

## Browser acceptance

The in-app browser loaded the live JARVIS HUD. A fresh team completed a Gemini baseline in35.38seconds with6/6 reports and18 completed tool calls. After shared request pacing was added and the server restarted, a live budget-cut run completed in85.21seconds with6/6 reports,18 tool calls, Finance's INR600000 gap and a final HOLD. The provider badge showed LIVE VERIFIED. The prior live baseline remained stored across restart.

The earlier rehearsal browser checks also exercised Memory Vault save/retrieval, run comparison, export, rubric save, persisted archive reopening and a narrow mobile layout. These are UI checks; the live acceptance above separately verifies Gemini inference.

## Limits found and addressed

An overlapping command-line lab request hit a provider-reported **15 requests/minute** limit for this project/model. A shared LangChain rate limiter now paces Gemini requests at12/minute within each app process. A subsequent paced live browser run passed. Separate processes/laptops and other applications using the same project do not share the local limiter. Token and daily limits remain provider constraints; changing prompts does not grant more quota. Gemini2.5Flash was also callable but encountered quota during the initial trial; the configured/tested workshop model is3.1Flash-Lite.

## Automated checks

**27 tests passed in both the development folder and a clean source copy installed with uv sync --frozen.** Coverage includes all six tool loops, baseline and four scenario shocks, required tool enforcement, finite/range validation, protected-field rejection, finance arithmetic and capacity hand-offs, team-scoped persistence, authentication/session isolation, code rotation/expiry, request admission and rate limiting, production configuration boundaries, partial-report preservation, input-size/origin/host boundaries, image validation before provider calls, sanitized failures and explicit cancellation/recovery. Gemini model instances were checked to share the same request budget.

The runner emits one upstream Starlette/AnyIO deprecation warning. It does not fail the tests. Ruff lint and JavaScript syntax checks passed. Source distribution and wheel builds passed; the build fetched hatchling because it was not in the initial cache. The online SQLite backup command succeeded and its isolated restored copy passed integrity checking and preserved both live browser run records. Automated tests use controlled rehearsal inputs; they do not claim broad correctness of arbitrary generated prose.

## Main deck

98 editable PowerPoint slides covering the proposal's eight sessions, with full speaker notes, original generated illustrations and editable flow diagrams. All98 slides rendered and individually inspected; nine changed layouts were re-inspected after corrections. The final canvas-overflow check passed. The98-page PDF is a slide-only raster viewing copy. The facilitator script contains the same teaching notes; the workbook contains the activities and evidence forms.

## Operational boundaries

Authentication is implemented and tested through the actual FastAPI application in TestClient. Local loopback mode keeps authentication optional; hosted production mode requires it and secure cookies. The Docker/Caddy recipe has not been built or deployed on this host because Docker is not installed. No remote DNS/TLS, GitHub publication, GitHub Actions execution, Windows runtime or classroom-scale concurrency result is claimed. Browser microphone capture and audible speech have not been exercised. The Ollama adapter is not live-tested here.

The app is a single process with SQLite and an in-process bounded queue. Do not run multiple workers against one data directory. Follow deploy/README.md and measure the actual host/provider capacity before opening a shared classroom service. Live model prose and fictional business assumptions still need human review.
