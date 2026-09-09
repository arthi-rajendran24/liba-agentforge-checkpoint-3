# Antigravity merge prompt

Paste the following into Antigravity after adding both the student project and this recovery repository to the same Antigravity Project.

```text
You are recovering my AgentForge project to TARGET_CHECKPOINT.

The STUDENT folder is my submission and remains authoritative for my specialization, business formula, tests, naming and explanations. The RECOVERY folder is a cumulative reference repository. Never replace a passing student implementation merely because the reference differs.

1. Read STUDENT/BUILD.md, RECOVERY/BUILD.md, RECOVERY/RECOVERY_MATRIX.md and RECOVERY/checkpoint.json.
2. Inventory the student project by layer: scaffold, deterministic tool, tests, adapter, shared service, local interface, evidence review, approved memory and channel.
3. Run existing offline tests before editing. Do not make network calls.
4. State the highest checkpoint already evidenced and the exact missing delta to TARGET_CHECKPOINT.
5. Preserve passing student files. In particular, preserve their domain tool and tests unless they fail their own Domain Build Card.
6. Use the Git diff named in RECOVERY_MATRIX.md to understand the missing layer. Do not copy unrelated later-stage code.
7. Add the smallest compatibility adapter needed to connect the student's tool to the reference interface. Business calculations must not move into the adapter, service, interface or Telegram channel.
8. Add or update tests before implementation. All tests must remain offline and use fakes for model and channel boundaries.
9. Never read, print, edit or copy a real .env. Never expose credentials.
10. Run the full offline suite. Then report files preserved, files added, files changed, test evidence and any live step still unverified.

Stop and ask me if the student formula conflicts with the Domain Build Card or if preserving it would create an unsafe result.
```
