# AGENTS.md Project Memory

Maintain one concise repository-root `AGENTS.md` for every academic article or thesis project. It is a navigation and handoff index, not the format-task overview.

## Separation rule

- Store complete format findings, stable issue IDs, evidence, execution details, and validation records in independent reports named `*_format_audit.md`.
- Store focused read-only investigations in `*_targeted_survey.md`.
- Store chronological execution detail in a dedicated worklog when the project uses one.
- In `AGENTS.md`, record only links, short status summaries, active baselines, key decisions, risks, and the next task.
- Never rename a format audit report to `AGENTS.md` or paste a complete audit into it.
- Keep `AGENTS.md` short enough for a new agent to understand the project quickly without loading detailed reports.

## Required contents

- project objective and current phase
- active baseline DOCX, PDF, title page, supplementary files, and submission package
- journal, school, template, and user-rule indexes
- master `*_format_audit.md` and focused survey-report indexes with short status summaries
- worklog and change-declaration indexes
- DOCX skill path, dedicated environment interpreter, renderers, and last preflight date
- concise completed-work summary
- concise prioritized pending-work summary
- key risks, prohibited operations, and user decisions
- latest user manual edits
- latest validation, commit, and push records where applicable

## Session behavior

At task start:

1. Read `AGENTS.md`.
2. Confirm the active baseline and pending task against actual files.
3. Read only the indexed reports needed for the task.

At task end:

1. Update active baseline and a short status summary.
2. Add links to new reports or outputs.
3. Link to complete validation and remaining-risk records rather than copying them in full.
4. Keep existing `CLAUDE.md` or other agent files indexed and consistent where the project requires them.
