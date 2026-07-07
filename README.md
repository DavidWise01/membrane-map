# membrane-map — the membranes your work can cross

A marker you plant can leave your hands by more than one route. Each route is a
**membrane**; each membrane has — or still needs — its own detector. This is the
hub of the boundary-crossing family, and it is honest about the membranes it does
not yet watch.

| membrane | crosses | detector | status |
|----------|---------|----------|--------|
| PUBLISHED | your marker on a crawlable page | [forward-observers](https://davidwise01.github.io/forward-observers/) | built |
| WEIGHTS | ingested into a training set, re-emitted from the weights | [surfacing](https://davidwise01.github.io/surfacing/) | built |
| CONTEXT / RELAY | re-emitted in another agent's output, relayed to you secondhand | [hearsay](https://davidwise01.github.io/hearsay/) | built |
| INFERENCE / API | echoed through a hosted model's completions to third parties | — | **unbuilt** |
| AIR-GAP | carried across a gap that was supposed to hold | airgap-ladder (adjacent) | partial |

And [the silence-gauge](https://davidwise01.github.io/silence-gauge/) weighs the
**negative** any detector returns — a positive can be ~60 bits; under suppression
a silence is < 0.1 bit.

## The through-line

**A positive is a lead; a negative means almost nothing.** Every instrument here
says "lead," never "proof," and the map names the membranes it cannot yet see —
that is how it earns trust.

## Verify first

```bash
python validate.py
```

Checks `membranes.json` with no network: every built membrane names a live
detector, a repo, and an honest reading of a positive AND a negative; every
unbuilt membrane is marked so and claims no detector — the map can't imply
coverage it lacks.

## Files
- `membranes.json` — the registry (the source of truth for the map)
- `validate.py` — the honesty check on that registry
- `index.html` — the constellation + the crossings, rendered from the registry

---
David Lee Wise / ROOT0 / TriPod LLC · CC-BY-ND-4.0
