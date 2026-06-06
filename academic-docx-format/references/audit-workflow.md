# Strict Academic DOCX Audit

## Purpose

Create a read-only, evidence-backed audit that becomes the master status record for later formatting work.

## Establish the formatting contract

Use requirements in this priority order:

1. Explicit user instructions
2. Target journal or school requirements and supplied template
3. Existing project decisions recorded in `AGENTS.md` and approved reports
4. Common academic and scientific publishing conventions

Separate explicit requirements from inferred conventions. Flag conflicts and ask the user to decide.

## Audit layers

1. **Package and privacy:** core properties, author identity, comments, tracked changes, custom XML, lock or temporary files.
2. **Page and sections:** paper size, margins, section breaks, columns, headers, footers, page numbering, line numbering.
3. **Typography:** styles, direct formatting, fonts, sizes, paragraph spacing, line spacing, indentation, widow/orphan behavior.
4. **Scientific notation:** editable equations, numbering, inline variables, italics, roman functions/subscripts, superscripts, units, symbols.
5. **Tables, figures, and captions:** object classification, numbering, caption style, references, widths, borders, page breaks, image quality.
6. **Fields and references:** `SEQ`, `REF`, `PAGEREF`, `TOC`, bookmarks, hyperlinks, citation coverage, reference-list continuity.
7. **Final artifacts:** DOCX/PDF agreement, metadata, filenames, package completeness.

Do not classify objects solely by visual appearance. For example, Word tables may be data tables, equation-layout tables, or invisible layout devices.

## Master report contract

Create or update one independent Markdown report, normally named `*_format_audit.md`, as the single source of truth. Never use `AGENTS.md` as this report. Include:

- target file and baseline identity
- requirements sources and interpreted contract
- status overview with stable issue IDs
- detailed location and structural evidence
- recommended correction and expected scope
- risk, dependencies, and explicit non-goals
- user decisions
- execution and validation status

Use `../assets/format-audit-report.template.md` when starting a new report.

## Stop condition

An audit-only task ends after the report is written and summarized. Do not modify the DOCX, even for obvious defects.
