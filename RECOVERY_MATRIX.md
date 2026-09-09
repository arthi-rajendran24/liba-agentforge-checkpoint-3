# Recovery matrix

Open the student's project and this recovery repository as two folders in one Antigravity Project. Use `ANTIGRAVITY_MERGE_PROMPT.md`; do not blindly copy the reference over student files.

| Student has | Target | Reference delta Antigravity should inspect |
|---|---|---|
| Nothing usable | Checkpoint 1 | `checkpoint-1` |
| Nothing usable | Checkpoint 2 | `checkpoint-2` (cumulative) |
| Nothing usable | Checkpoint 3 | `checkpoint-3` (cumulative) |
| Checkpoint 1 | Checkpoint 2 | `checkpoint-1..checkpoint-2` |
| Checkpoint 1 | Checkpoint 3 | `checkpoint-1..checkpoint-3` |
| Checkpoint 2 | Checkpoint 3 | `checkpoint-2..checkpoint-3` |
| Partial or uncertain | Any | Run the target's tests, inventory passing layers, then choose the nearest passing source checkpoint |

The reference finance defaults are fallback examples. The student's chosen specialization, function, tests and wording take precedence when they are valid.
