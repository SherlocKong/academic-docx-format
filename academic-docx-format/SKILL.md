---
name: academic-docx-format
description: Audits, plans, safely modifies, and validates formatting in existing academic DOCX manuscripts, theses, journal submissions, and supplementary documents. Use when reviewing or correcting fonts, spacing, equations, scientific notation, tables, captions, numbering, cross-references, page layout, anonymity, metadata, or submission-package formatting while preserving unrelated content and structure.
---

# Academic DOCX Format

Govern academic DOCX formatting through an auditable, copy-based workflow. Use the installed `docx` skill for every DOCX read, edit, render, or package operation; this skill supplies the safety gates, academic-format rules, project continuity, and regression checks around it.

## Non-negotiable gates

1. **Preflight first.** Verify that the `docx` skill and required DOCX tooling are available. Run `scripts/preflight.py`. If dependencies are missing, help configure them before handling the document. When global or project dependencies conflict, follow `references/environment-setup.md`, create a dedicated environment, and record its interpreter and tool paths in `AGENTS.md`.
2. **Establish project memory.** Read the repository-root `AGENTS.md` before work. If absent, create it from `assets/AGENTS.template.md`, ask the user to confirm the initial index, and do not begin formal modification until confirmed. Keep `AGENTS.md` concise: it is a navigation and handoff index, never the full format audit or detailed worklog. Treat existing `CLAUDE.md` or similar files as indexed project records, not replacements for `AGENTS.md`.
3. **Survey before repair.** Perform a read-only survey and create a Markdown report before proposing changes. Locate every affected object, related field, reference, and structurally similar non-target object.
4. **Obtain approval and plan.** Do not modify a DOCX until the user has reviewed the survey and approved an execution plan. Enter Plan mode before every modification when the host supports it. When it does not, stop after presenting the written plan and wait for explicit approval. Resolve all ambiguity; never guess about unclear formatting requirements.
5. **Never overwrite the input.** Create a timestamped working copy with `scripts/create_working_copy.py`. Edit only that copy. Overwrite only when the user explicitly requests it after being warned.
6. **Use targeted edits.** Modify only approved objects. Preserve unrelated content, styles, layout, package parts, relationships, fields, images, and metadata unless they are explicitly in scope.
7. **Prove no collateral damage.** Validate content, OOXML structure, and rendered pages. A successfully opening DOCX is necessary but insufficient.
8. **Update project records.** Write complete findings, execution details, validation evidence, and residual risks to the independent master `*_format_audit.md`. Update `AGENTS.md` only with its path, a short status summary, the active baseline, and the next task.

## Route the task

- **Audit only:** Read `references/audit-workflow.md`. Do not create a modified DOCX.
- **Targeted format repair:** Read `references/targeted-repair.md` and the relevant academic rules in `references/scientific-formatting.md`.
- **Regression check after user or agent edits:** Read `references/validation-and-handoff.md`.
- **Final submission-package check:** Read `references/validation-and-handoff.md` and inspect DOCX, PDF, metadata, filenames, and directory contents together.
- **Project bootstrap or handoff:** Read `references/project-memory.md`.
- **Missing or conflicting DOCX dependencies:** Read `references/environment-setup.md`.

## Required operating sequence

1. Read `AGENTS.md`, current reports, requirements, and the latest user-approved baseline.
2. Run environment preflight and record any dedicated environment path.
3. Extract the applicable school, journal, or user formatting contract.
4. Run a read-only DOCX inventory; use `scripts/docx_inventory.py` as a helper, then inspect the actual document with the `docx` skill.
5. Write or update an independent master Markdown audit report named descriptively, normally `*_format_audit.md`. Never use `AGENTS.md` as the format-task overview. Use `assets/format-audit-report.template.md` when no report exists.
6. Wait for user review. Produce a precise execution plan with allowed and forbidden changes.
7. Create a timestamped copy such as `manuscript_20260606_153000_equation-format.docx`.
8. Use the `docx` skill to apply the approved targeted changes to the copy.
9. Validate according to `references/validation-and-handoff.md`, including rendered-page inspection.
10. Update the full audit report, then add only its status summary, path, new approved baseline, and next task to `AGENTS.md`; do not delete prior versions.

## Boundaries

- Do not use this skill for ordinary business documents or net-new general DOCX creation.
- Do not rewrite academic content merely because a formatting task exposes a prose issue. Report it separately.
- Do not rebuild an existing manuscript from Markdown, plain text, or a fresh document.
- Do not treat helper scripts as substitutes for the `docx` skill.
- Do not run broad formatting, field-update, or style-normalization operations without explicit approval.
- Do not silently clean unrelated issues discovered during a targeted task; add them to the report.
- Do not place detailed findings, issue-by-issue evidence, execution narratives, or full validation logs in `AGENTS.md`.

## Bundled resources

- `scripts/preflight.py`: inspect DOCX skill and environment readiness.
- `scripts/create_working_copy.py`: create a timestamped, hashed working copy.
- `scripts/docx_inventory.py`: produce a read-only structural/package inventory.
- `assets/AGENTS.template.md`: project continuity index.
- `assets/format-audit-report.template.md`: master audit/status report.
- `assets/targeted-survey-report.template.md`: focused read-only survey report.
