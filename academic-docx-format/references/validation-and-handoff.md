# Validation and Handoff

## Three-layer regression gate

### 1. Content invariance

- Compare paragraph and table text before and after.
- Confirm only approved text changed.
- Recheck captions, numbering, citations, and references affected by the task.
- Confirm object counts remain stable unless a count change was approved.

### 2. OOXML and package integrity

- Confirm the output remains a valid ZIP/DOCX package and opens with the `docx` skill tooling.
- Compare package part lists and relationships.
- Inspect fields, bookmarks, comments, tracked changes, equations, images, headers, footers, and core properties relevant to the task.
- Explain every changed package part.
- Scan for unintended identity data when anonymity matters.

### 3. Visual rendering

- Render DOCX to PDF and page images using the `docx` skill workflow.
- Inspect every changed page and representative unaffected pages.
- Check clipping, overlap, glyphs, wrapping, pagination, tables, equations, captions, headers, footers, page numbers, and line numbers.
- Treat rendering success as evidence, not proof; visually inspect the result.

## Final package check

Audit the DOCX, exported PDF, and submission directory together:

- required files and clear filenames
- no lock files, caches, or temporary artifacts
- Word/PDF page and content agreement
- metadata and anonymity
- expected supplementary files
- hashes or version identity where useful

## Handoff record

Update the master `*_format_audit.md` with the complete handoff record:

- previous and new baseline paths
- input/output hashes when available
- approved scope and actual changes
- validation commands and results
- known renderer differences
- unresolved issues and next task

Update `AGENTS.md` only with the master-report path, active baseline, a short validation/status summary, key risks, and next task.

Do not delete prior approved versions. When the user manually edits a file, treat the latest user-approved copy as a new baseline and resurvey before further repair.
