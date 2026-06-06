# Targeted Academic DOCX Repair

## Entry requirements

Do not begin until all are true:

- a read-only survey exists
- the user approved the issue scope
- ambiguous decisions are resolved
- an execution plan defines allowed and forbidden changes
- a timestamped copy has been created

## Protection contract

Every plan must state:

- **Input baseline:** exact path, timestamp, and preferably SHA-256
- **Output copy:** timestamped path and task slug
- **Allowed changes:** exact objects, locations, styles, or package parts
- **Forbidden changes:** unrelated prose, tables, figures, styles, pagination, fields, metadata, or package parts
- **Expected secondary effects:** legitimate line wrapping, pagination, field results, or PDF-page changes
- **Validation evidence:** checks required before delivery

## Object identification

Use at least two independent selectors where practical:

- caption or displayed number
- paragraph text or nearby heading
- style ID
- table dimensions or cell structure
- bookmark/field relationship
- OOXML element type
- document order and context

Never apply “all tables”, “all equations”, “all italic text”, or similar broad edits unless the survey proves every matched object is in scope.

## Editing rules

- Invoke and follow the installed `docx` skill.
- Edit the existing DOCX package or copied document; never reconstruct the manuscript.
- Preserve run-level formatting and relationships when replacing text.
- Inspect fields and bookmarks before changing numbering or references.
- Treat display equations and inline notation separately.
- Avoid “update all fields” unless explicitly approved and regression-tested.
- Record newly discovered issues instead of expanding scope silently.

## Completion

Complete only after the copied DOCX passes structural, content, and visual checks, the master `*_format_audit.md` records complete results and residual risks, and `AGENTS.md` concisely identifies the report, new baseline, status, and next task.
