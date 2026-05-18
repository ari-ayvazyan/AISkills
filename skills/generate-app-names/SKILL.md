---
name: generate-app-names
description: Generates strategic product and application names using linguistic engineering. Trigger when invoked with /generate-app-names
disable-model-invocation: true
---

<essential_principles>

<principle name="name_as_strategic_asset">
A product name is not merely an identifier - it is a permanent anchor for brand equity, a self-sustaining marketing vehicle, and the primary point of contact between business and customer. The name carries the weight of first impressions, brand promise, and fundamental identity. Every naming decision must consider long-term scalability, emotional resonance, and competitive differentiation.
</principle>

<principle name="cognitive_fluency">
The human brain gravitates toward information requiring minimal cognitive effort. Names that are phonetically pleasing, simple, and intuitively understandable are more likely to be remembered and viewed positively. Research indicates names between 6-8 characters perform best in memory tests, providing sufficient distinctiveness while maintaining ease of recall.
</principle>

<principle name="sound_symbolism">
Specific sounds inherently convey meaning (the Bouba/Kiki effect). Strategic naming leverages these associations:
- **Plosives** (k, t, p, b, g): Strength, precision, impact, energy
- **Fricatives/Nasals** (m, n, l, s, f): Warmth, gentleness, comfort, fluidity
- **Long vowels** (/aɪ/ as in "sky"): Sophistication, luxury, expansiveness
- **Repetitive vowels** (/uː/ as in "oo"): Roundness, completeness, playfulness
</principle>

<principle name="differentiation_over_description">
Move away from descriptive names that become obstacles as companies evolve. Abstract or evocative names (Apple, Amazon, Virgin) allow long-term modifications and brand extensions. Differentiation should convey the "spirit" of the brand rather than its literal attributes.
</principle>

<principle name="smile_scratch_framework">
Evaluate all name candidates using these criteria:

**SMILE (Seek These):**
- **S**imple - Easy to spell and say
- **M**eaningful - Communicates brand essence
- **I**maginative - Unique and distinctive
- **L**ovable - Creates emotional connection
- **E**legant - Refined and appropriate

**SCRATCH (Avoid These):**
- **S**pelling challenged - Hard to spell correctly
- **C**opycat - Too similar to competitors
- **R**estrictive - Limits future growth
- **A**nnoying - Irritating pronunciation or meaning
- **T**ame - Forgettable, bland
- **C**urse of knowledge - Only insiders understand
- **H**ard to pronounce - Stumbles in conversation
</principle>

</essential_principles>

<intake>
What would you like to do?

1. **Generate names** - Full naming process with brainstorming and evaluation
2. **Evaluate existing names** - Apply SMILE/SCRATCH analysis to candidates
3. **Validate names** - Check trademark, cultural, and digital availability concerns
4. **Get naming strategy guidance** - Understand which naming approach fits your product

Provide context about your product/app if you have it, or wait for questions.
</intake>

<routing>
| Response | Workflow |
|----------|----------|
| 1, "generate", "create", "brainstorm", "new names" | `workflows/generate-names.md` |
| 2, "evaluate", "analyze", "review", "assess" | `workflows/evaluate-names.md` |
| 3, "validate", "check", "trademark", "cultural" | `workflows/validate-names.md` |
| 4, "strategy", "guidance", "which type", "approach" | Provide inline guidance from references |

**If user provides product context without selecting an option:**
- Infer intent from keywords
- If unclear, default to option 1 (generate names)

**After reading the workflow, follow it exactly.**
</routing>

<reference_index>
All domain knowledge in `references/`:

**Naming Strategies:** naming-strategies.md
- Descriptive, suggestive, evocative, abstract, hybrid, compound approaches
- Strategic advantages and risks of each type

**Linguistic Principles:** linguistic-principles.md
- Sound symbolism and phonaesthemes
- Cognitive fluency and memory optimization
- Emotional and associative triggers

**Ideation Methods:** ideation-methods.md
- Mind mapping, brainwriting, reverse brainstorming
- SCAMPER framework for name manipulation
- Portmanteau and word blending techniques

**Cultural Considerations:** cultural-considerations.md
- Global transferability strategies
- Cultural blunder prevention
- Linguistic and cultural vetting checklist
</reference_index>

<workflows_index>
| Workflow | Purpose |
|----------|---------|
| generate-names.md | Full strategic naming process from research to shortlist |
| evaluate-names.md | SMILE/SCRATCH analysis and scoring of candidates |
| validate-names.md | Trademark, digital, and cultural vetting |
</workflows_index>

<quick_reference>
**Naming Strategy Selection:**

| Strategy | Best For | Trademarkability | Marketing Investment |
|----------|----------|------------------|---------------------|
| Descriptive | B2B, niche functional | Low | Low |
| Suggestive | Tech, lifestyle, entertainment | Medium | Medium |
| Evocative | Premium, aspirational | High | Medium |
| Abstract/Invented | Global brands, innovative categories | Very High | High |
| Founder/Personal | Artisan, professional services | Medium | Low |
| Hybrid/Compound | Consumer apps, social platforms | High | Medium |

**Phonetic Quick Guide:**
- Need **strength/energy**: Use K, P, T, B, G sounds (Kodak, Google, FedEx)
- Need **warmth/comfort**: Use M, N, L, S sounds (Nestlé, Lululemon)
- Need **sophistication**: Use long vowels like /aɪ/ (Nike, Hyatt)
- Need **playfulness**: Use repetitive vowels /uː/ (Yahoo, Hulu)
</quick_reference>

<success_criteria>
A successful naming outcome includes:
- [ ] Clear understanding of product positioning and target audience
- [ ] 10-20 diverse name candidates generated
- [ ] Names evaluated against SMILE/SCRATCH criteria
- [ ] Top 3-5 candidates identified with strategic rationale
- [ ] Preliminary trademark and domain considerations noted
- [ ] Cultural/linguistic concerns flagged for global products
</success_criteria>
