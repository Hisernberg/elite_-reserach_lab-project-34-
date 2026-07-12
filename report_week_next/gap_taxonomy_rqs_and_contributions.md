# Gap Taxonomy and Review Questions — v2

## Review questions

- **RQ1.** What methods have been used for patient-facing medical/clinical text simplification and explanation generation from 2020–2025?
- **RQ2.** How do studies define and evaluate factuality, faithfulness, medical accuracy, and hallucination?
- **RQ3.** Which datasets support medical simplification, lay summarization, jargon explanation, clinical NLI, and Bangla healthcare NLP?
- **RQ4.** What evidence supports multilingual or low-resource transfer to Bangla?
- **RQ5.** How rigorous are human evaluation, clinician review, and reproducibility practices?
- **RQ6.** What architecture is justified for a factually safe Bangla clinical simplification system?

## Gaps

### G1 — No expert-validated Bangla clinical simplification corpus

Evidence to extract: Rows with Bangla direct resources; construction=synthetic/paraphrase/summarization/NER, not simplification

Mapped RQ: RQ3/RQ4

Future solution: Build BnClinSimp-Expert with clinician + lay validation.

### G2 — Factuality often reduced to overlap/entity preservation

Evidence to extract: Factuality_Mechanism in top-80 corpus; count lexical/NER vs NLI/graph/human

Mapped RQ: RQ2

Future solution: Clinical fact graph preservation + relation/attribute scoring.

### G3 — No relation-level Bangla medical NLI benchmark

Evidence to extract: Medical NLI papers and Bangla NLI resources; mark medical vs general-domain

Mapped RQ: RQ2/RQ4

Future solution: 500-pair Bangla MedNLI pilot with contradiction categories.

### G4 — Synthetic/automatic simplification data can introduce semantic drift

Evidence to extract: Dataset construction column; synthetic vs expert-validated

Mapped RQ: RQ3/RQ5

Future solution: Use synthetic data only after NER/NLI/clinician filtering.

### G5 — Graph/RAG grounding is rarely tested in low-resource simplification

Evidence to extract: RAG/KG and constrained-decoding rows; Bangla relevance column

Mapped RQ: RQ1/RQ4

Future solution: KG-RAG + graph-constrained beam search in Bangla.

### G6 — Human evaluation is underpowered and rarely patient-centered

Evidence to extract: Human evaluation fields: raters, expertise, kappa, patient comprehension

Mapped RQ: RQ5

Future solution: Clinician + patient evaluation with kappa and power justification.

### G7 — Search terminology is fragmented across simplification, lay summary, explanation, health literacy

Evidence to extract: Search log returns by query; overlap/deduplication

Mapped RQ: RQ1/RQ3

Future solution: Use 9-query block strategy + citation chasing.

