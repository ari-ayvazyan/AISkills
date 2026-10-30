# Write rules

Tree of Markdown files under the knowledge root.

## Steps
1. Search first. Exists -> leave. Extends or contradicts -> edit that bullet in place, never keep both
2. Most fitting topic file; new one only when none fits
3. Bullet: telegraphic keywords, trigger -> rule, normally under 10 words. Grows only for exact names, values, order; keep those verbatim. No inferable reasons, method, evidence. Fold related points
4. Changed topic file -> `updated` = today
5. Other topic needed to apply this one -> `See:` link
6. Added, moved, removed -> parent `_index.md` in sync
7. `python <this skill>/scripts/kb_check.py <knowledge root>` -> fix every error, also older ones

Interrupted before checker passes -> say so; learnings may not be saved.

## Limits
- Topic file: max 30 bullets. Full -> split by subject into newly named files, update parent index, lose no bullet
- Index: max 30 entries, each under 25 words, subject not details. Full -> group into subfolders, each with `_index.md`
- Slug (topic file name): unique across tree, lowercase-with-hyphens; check before creating
- Links: slug, never path; moves break nothing

## Formats
Topic file `<slug>.md`:

    ---
    updated: YYYY-MM-DD
    keywords: synonyms, related terms absent from bullets
    sources: ingested from, URLs or short names, no personal data; omit if none
    ---
    - trigger -> rule

    See: [[other-slug]]

Index `_index.md`, one line per child:

    - [[slug]] - what this topic covers
    - [folder/](folder/_index.md) - what this branch covers
