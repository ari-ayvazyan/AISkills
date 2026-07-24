---
name: formatted-summary
description: Summarizes texts in well digestible way
disable-model-invocation: true
---
# skill.md: Semantic Compression & Architecture

| Parameter | Value |
| --- | --- |
| **Objective** | Transform unstructured text into dense, modular, visual data. |
| **Application** | System prompts, meeting notes, email threads, complex documentation. |
| **Constraint** | Zero walls of text. Maximize cognitive and token efficiency. |

> **CORE OUTCOME:**
> Apply strict markdown blocks based on functional intent to maximize scannability and semantic density.
>
> **Why it matters:** Human readers scan; AI models charge per token. Narrative redundancy wastes time and processing power.

## 1. Linguistic Compression (Micro Level)

* **[Problem] Cognitive and Token Bloat:**
  * *Action (Caveman Mode):* Drop filler words, articles, and pleasantries. Use fragments.
  * *Action (Paramedic Method):* Kill passive "is" verbs, cut prepositions, front-load actors.
  * *Result:* 50–65% text reduction. High-velocity reading.

## 2. Structural Building Blocks (Macro Level)

| Block Type | Trigger Condition | Markdown Pattern |
| --- | --- | --- |
| **1. Meta-Initiator** | Context variables (date, actors) dictate relevance. | 2-column table at document start. |
| **2. Executive Apex** | Central decision or core synthesis is reached. | Blockquote (`>`) with **bold** header. |
| **3. Relational Matrix** | Comparing entities or mapping causality. | Tables or nested hierarchical lists. |
| **4. Executive Vector** | Next steps or required actions emerge. | Task lists (`- [ ]`) with exact owner/date. |
| **5. Semantic Rulebook** | System prompts or persistent rules needed. | Table defining `Component`, `Value`, `Do/Don't`. |
| **6. Conversation Digest** | One or more email/message threads detected. | Per-thread header block + resolution line. |
| **7. Reference Ledger** | Retrieval items present (credentials, dates, links, IDs). | Grouped 2-column key→value tables. |

## 3. Visual Formatting Constraints

| Element | Specification | Rule (Do/Don't) |
| --- | --- | --- |
| **Headings** | ATX style (`# `, `## `). | **Do:** Keep strict hierarchy. Add blank lines around them. |
| **Whitespace** | Empty lines around all block elements. | **Don't:** Collapse spacing. Visual rhythm is mandatory. |
| **Emphasis** | Double asterisks (`**bold**`). | **Don't:** Mix styles. Only emphasize key metrics and owners. |
| **Metadata** | Emojis (`🔴`, `📅`, `🟢`). | **Do:** Use strictly as visual status anchors, never for decoration. |

## 4. Conversation Digest (Thread Level)

* **[Problem] Thread Sprawl:** Email chains and message logs bury decisions under quoted replies, greetings, and signatures. Multiple pasted threads blur into one undifferentiated mass.
* *Action:* Detect each distinct conversation. Summarize independently. Strip quoting, salutations, and sign-offs. Surface only participants, arc, and outcome.
* *Result:* One scannable digest per thread. Instant recovery of who wants what and what got decided.

**DETECTION:** Treat as a new thread on any subject-line change, new participant set, distinct timestamp cluster, or explicit separator between pasted blocks.

**PER-THREAD ARCHETYPE:**
Emit one block per detected conversation.

### 📧 [Subject / Thread Label]

| Field | Value |
| --- | --- |
| **Participants** | [Actors, → direction if relevant] |
| **Span** | [First msg date → last msg date] |
| **Status** | 🟢 Resolved / 🔴 Open / 🟡 Awaiting reply |

* **Gist:** [Single-sentence reason the thread exists.]
* **Arc:** [2–4 fragments tracing the exchange. One beat per fragment.]
* **Outcome:** [The decision, agreement, or open question left standing.]

> **DIGEST RULE:** Never merge threads. When many threads share a topic, list each block separately, then add one **Executive Apex** blockquote synthesizing across them.

## 5. Factual Distillation (Content Ledger)

* **[Problem] Narrative Burial:** Hard facts, metrics, and historical states drown in conversational transcripts or unstructured text.
* *Action:* Extract atomic truths. Strip conversational context. Map to a definitive ledger.
* *Result:* Zero-friction retrieval. Absolute, scannable ground truth.

| Ledger Component | Specification | Rule (Do/Don't) |
| --- | --- | --- |
| **Entity/Topic** | Core subject of the fact. | **Do:** Use absolute nouns. No pronouns. |
| **Atomic Fact** | Single, self-contained truth. | **Don't:** Compound statements. One fact per row. |
| **Metric/State** | Quantifiable data or status. | **Do:** Isolate numbers, dates, or boolean flags (🟢/🔴). |
| **Source Ref.** | Origin of the truth. | **Do:** Anchor to a specific timestamp, speaker, or section. |

**CLAIM LEDGER ARCHETYPE:**
For *assertions* — claims about the world that need tracing and trust. Anchor these at the end of summaries.

| Topic / Entity | Fact / Assertion | Metric / State | Source / Time |
| --- | --- | --- | --- |
| [Subject] | [Stripped statement] | [Quantifier] | [Ref] |

### 5a. Reference Ledger (Retrieval Items)

* **[Problem] Value Loss:** Credentials, dates, links, IDs, and amounts are *values to recall verbatim*, not claims to trust. A `Fact/Metric/Source` row is the wrong shape — source and confidence are meaningless for a password.
* *Action:* Split retrieval items out. Preserve values **literally**. Group by kind. Never paraphrase or "clean up" a value.
* *Result:* Zero-ambiguity copy-paste lookup. Secrets flagged, not buried.

| Item Type | Specification | Rule (Do/Don't) |
| --- | --- | --- |
| **Key** | Label for the value. | **Do:** Use the item's real name (`Password`, `Kickoff`, `Portal`). |
| **Value** | The literal datum. | **Do:** Wrap copy-paste items in `` `monospace` `` — preserves whitespace and `l/1/I`. **Don't:** Reword, trim, or normalize. |
| **Group** | Category heading. | **Do:** Cluster by kind: Access / Dates / Links / IDs / Amounts. |
| **Sensitivity** | Secret-value flag. | **Do:** Mark credentials with 🔒 so the reader knows a secret is present. |

**REFERENCE LEDGER ARCHETYPE:**
Emit grouped 2-column tables. One group per category present.

#### 🔑 Reference Ledger

**🔒 Access**
| Key | Value |
| --- | --- |
| Login | `email@asd.com` |
| Password | `Xk9$mQ2p` |
| Portal | https://… |

**Dates**
| Event | When |
| --- | --- |
| [Event] | [Exact date/time + TZ] |

> **LEDGER SPLIT RULE:** Route each item by intent — a *value to recall* → Reference Ledger (5a); a *claim to trust* → Claim Ledger (5). When in doubt, ask: "would the user copy this verbatim, or cite it?"

## 6. Execution Protocol

* [ ] **Ask:** When something is unclear, ask the user before assuming. (@Writer) 📅 *Pre-publish*
* [ ] **Segment:** Detect and isolate each distinct conversation before summarizing. (@Writer) 📅 *Pre-publish*
* [ ] **Audit:** Delete all narrative transitions and pleasantries. (@Writer) 📅 *Pre-publish*
* [ ] **Isolate:** Move metadata to a top-level `Meta-Initiator` table. (@Writer) 📅 *Pre-publish*
* [ ] **Extract:** Isolate all verifiable claims into the Claim Ledger. (@Researcher) 📅 *Post-discussion*
* [ ] **Route:** Send retrieval items (creds, dates, links, IDs) to the Reference Ledger; preserve values literally, flag secrets with 🔒. (@Researcher) 📅 *Post-discussion*
* [ ] **Atomize:** Split any ledger row containing "and" or "but" into two rows. (@Reviewer) 📅 *Pre-publish*
* [ ] **Verify:** Ensure blank lines surround all markdown blocks. (@Reviewer) 📅 *Pre-publish*