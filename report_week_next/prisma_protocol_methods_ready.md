# PRISMA / Methods Protocol — v2 Ready Text

## Design

This review will be reported according to PRISMA 2020 and the search reporting will follow PRISMA-S. The synthesis is planned as SWiM because the included studies are expected to be heterogeneous in datasets, languages, architectures, and factuality metrics.

## Eligibility criteria

### Include
- Peer-reviewed journal articles or full-length conference papers.
- Publication year 2020–2025 for the analytical corpus.
- Clinical, biomedical, healthcare, or patient-facing text.
- Text simplification, lay summarization, explanation generation, factuality/faithfulness evaluation, medical NLI, constrained decoding, RAG/KG grounding, Bangla healthcare NLP, or transferable multilingual/low-resource method.
- DOI, ACL Anthology ID, PubMed/PMC ID, or stable publisher page.

### Exclude
- Preprint-only papers without accepted version.
- Posters, editorials, comments, non-archival demos, and research-in-progress notes.
- Short weak conference papers, especially ≤6-page IEEE conference papers unless top-tier and methodologically central.
- General-domain NLP papers with no clinical, factuality, multilingual, or Bangla transfer relevance.
- Duplicates, superseded arXiv versions, inaccessible full text after two requests.

## Screening

Two reviewers screen title/abstract independently. Disagreements are resolved by discussion or a third reviewer. Full-text screening uses the exclusion code list in the workbook. Cohen's kappa is reported after title/abstract and full-text screening.

## Extraction

The extraction sheet has 16 fields: citation, venue, task, architecture, dataset, language, factuality method, readability metric, human evaluation, baselines, risk of bias, Bangla relevance, and notes.

## Quality appraisal

Standard clinical tools are used only when appropriate. Ordinary NLP benchmark/model papers use the custom NLP-Bias tool with domains for leakage, baseline strength, metric validity, human evaluation rigor, statistical testing, reproducibility, and clinical expert involvement.

## Synthesis

The results are grouped by factuality mechanism, language/resource setting, and evaluation rigor. GRADE certainty is rated for factuality preservation, readability improvement, patient comprehension, Bangla transferability, and reproducibility.
