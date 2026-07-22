---
name: formatted-summary
description: Summarizes texts in well digestible way
disable-model-invocation: true
---
# formatted-summary

Here is the restructured skill document, applying its own principles of semantic compression, visual hierarchy, and brevity:

# skill.md: Semantic Compression & Architecture

| Parameter | Value |
| --- | --- |
| **Objective** | Transform unstructured text into dense, modular, visual data.

 |
| **Application** | System prompts, meeting notes, complex documentation.

 |
| **Constraint** | Zero walls of text. Maximize cognitive and token efficiency.

 |

> **CORE OUTCOME:**
> Apply strict markdown blocks based on functional intent to maximize scannability and semantic density.
> **Why it matters:** Human readers scan; AI models charge per token. Narrative redundancy wastes time and processing power.
> 
> 

## 1. Linguistic Compression (Micro Level)

* **[Problem] Cognitive and Token Bloat:**
* *Action (Caveman Mode):* Drop filler words, articles, and pleasantries. Use fragments.


* *Action (Paramedic Method):* Kill passive "is" verbs, cut prepositions, front-load actors.


* *Result:* 50-65% text reduction. High-velocity reading.





## 2. Structural Building Blocks (Macro Level)

| Block Type | Trigger Condition | Markdown Pattern |
| --- | --- | --- |
| **1. Meta-Initiator** | Context variables (date, actors) dictate relevance.

 | 2-column table at document start.

 |
| **2. Executive Apex** | Central decision or core synthesis is reached.

 | Blockquote (`>`) with **bold** header.

 |
| **3. Relational Matrix** | Comparing entities or mapping causality.

 | Tables or nested hierarchical lists.

 |
| **4. Executive Vector** | Next steps or required actions emerge.

 | Task lists (`- [ ]`) with exact owner/date.

 |
| **5. Semantic Rulebook** | System prompts or persistent rules needed.

 | Table defining `Component`, `Value`, `Do/Don't`.

 |

## 3. Visual Formatting Constraints

| Element | Specification | Rule (Do/Don't) |
| --- | --- | --- |
| **Headings** | ATX style (`# `, `## `).

 | **Do:** Keep strict hierarchy. Add blank lines around them.

 |
| **Whitespace** | Empty lines around all block elements.

 | **Don't:** Collapse spacing. Visual rhythm is mandatory.

 |
| **Emphasis** | Double asterisks (`**bold**`).

 | **Don't:** Mix styles. Only emphasize key metrics and owners.

 |
| **Metadata** | Emojis (`🔴`, `📅`, `🟢`).

 | **Do:** Use strictly as visual status anchors, never for decoration.

 |

## 4. Execution Protocol

* [ ] **Ask:** When something is unclear, instead of assuming, ask the user before proceeding. (@Writer) 📅 *Pre-publish*
* [ ] **Audit:** Delete all narrative transitions and pleasantries (@Writer) 📅 *Pre-publish*
* [ ] **Isolate:** Move metadata to a top-level `Meta-Initiator` table (@Writer) 📅 *Pre-publish*
* [ ] **Verify:** Ensure blank lines surround all markdown blocks (@Reviewer) 📅 *Pre-publish*
[ ] Extract: Isolate all verifiable claims and data points from the narrative into the Content Ledger (@Researcher) 📅 Post-discussion
[ ] Atomize: Split any row in the ledger that contains an "and" or "but" into two distinct rows (@Reviewer) 📅 Pre-publish

Here is the extension to your skill document, matching your exact constraints for semantic compression, structural hierarchy, and formatting.

5. Factual Distillation (Content Ledger)

[Problem] Narrative Burial: Hard facts, metrics, and historical states drown in conversational transcripts or unstructured text.
Action: Extract atomic truths. Strip conversational context. Map to a definitive ledger.
Result: Zero-friction retrieval. Absolute, scannable ground truth.
Ledger ComponentSpecificationRule (Do/Don't)Entity/TopicCore subject of the fact.Do: Use absolute nouns. No pronouns.Atomic FactSingle, self-contained truth.Don't: Compound statements. One fact per row.Metric/StateQuantifiable data or status.Do: Isolate numbers, dates, or boolean flags (🟢/🔴).Source Ref.Origin of the truth.Do: Anchor to a specific timestamp, speaker, or section.
LEDGER ARCHETYPE:
Implement this structural block at the end of summaries to anchor discussed facts.
Topic / EntityFact / AssertionMetric / StateSource / Time[Subject][Stripped statement][Quantifier][Ref]