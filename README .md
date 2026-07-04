# Review reference library: Factuality in Clinical Text Simplification + Bangla Healthcare NLP

Generated: 2026-07-04

## Contents

This package contains an Overleaf/Zotero-ready reference library and bibliomatrix workbench for the review paper on **factuality preservation in patient-facing medical text simplification with a low-resource Bangla evidence map**.

## Main files

| File | Purpose |
|---|---|
| `factuality_clinical_ts_bangla_215refs.bib` | Master BibTeX screening-pool library with 215 records |
| `factuality_clinical_ts_bangla_core105.bib` | Smaller BibTeX file with 105 core/method/supporting/baseline records |
| `bibliomatrix_master_215.csv` | Master bibliomatrix with citation metadata, categories, factuality mechanism, Bangla relevance, and verification status |
| `bibliomatrix_master.xlsx` | Excel workbook with dashboard, master matrix, factuality matrix, Bangla matrix, tag matrix, DOI queue, and templates |
| `matrix_paper_x_factuality_mechanism.csv` | Binary matrix for factuality/faithfulness mechanisms |
| `matrix_paper_x_bangla_relevance.csv` | Binary matrix for direct/transferable Bangla relevance |
| `matrix_paper_x_controlled_tags.csv` | Binary matrix for controlled Zotero-style tags |
| `overleaf_elsarticle_starter.tex` | Minimal Elsevier/JBI-style Overleaf starter using the master `.bib` |
| `citation_key_groups.md` | Cite keys grouped by review section/category |
| `doi_verification_queue.csv` | DOI/stable-ID verification queue |
| `verify_dois_crossref.py` | Crossref DOI verification script for local use |
| `generate_bibliomatrix.R` | Bibliometrix R workflow |
| `search_strategy_pack.md` | Database search strings |
| `data_extraction_template.csv` | Extraction codebook template |
| `prisma_flow_counts_template.csv` | PRISMA flow count log |
| `risk_of_bias_template.csv` | RoB/NLP-bias extraction template |
| `grade_summary_of_findings_template.csv` | GRADE Summary of Findings template |

## Verification status summary

- Records total: 215
- DOI populated: 155
- ACL Anthology IDs: 88
- arXiv IDs: 31

- acl_id_stable_no_doi_field: 11
- arxiv_stable_no_doi: 23
- doi_present_needs_crossref_check: 26
- doi_structurally_verified_from_source: 129
- pmid_stable_no_doi: 1
- url_stable_no_doi: 25

DOI policy: DOI fields are populated only where a DOI or a formal DOI-like venue identifier was available. ACL Anthology, arXiv, PubMed/PMC, publisher, and dataset records are retained using stable URLs/IDs when a DOI is not available. Run `verify_dois_crossref.py` from a machine with internet access before final journal submission.

## Category counts

- 01_Core_Clinical_TS: 20
- 02_Adjacent_Multilingual_TS: 21
- 03_Adjacent_Bangla_NLP: 17
- 04_Factuality_Methods: 26
- 05_Constrained_Decoding: 12
- 06_RAG_KG_Medical: 18
- 07_Evaluation_Methods: 20
- 07_Medical_NLI: 14
- 08_Systematic_Review_Methods: 17
- 10_LLM_Backbones_LowResource: 20
- 11_Clinical_NLP_Datasets: 15
- 12_Clinical_Summarization_Health_Literacy: 15

## Overleaf usage

1. Upload `overleaf_elsarticle_starter.tex` and `factuality_clinical_ts_bangla_215refs.bib` to Overleaf.
2. Rename the `.tex` file to `main.tex` if desired.
3. Compile with pdfLaTeX + BibTeX.
4. Use `citation_key_groups.md` to select citation keys by section.

## Zotero usage

1. Import `factuality_clinical_ts_bangla_215refs.bib` into Zotero.
2. Create the collections listed in `zotero_collections.csv`.
3. Use `controlled_tags.csv` for controlled vocabulary tagging.
4. Run duplicate detection.
5. Attach PDFs and run the DOI verification queue.
6. Export with Better BibTeX after verification.

## Bibliomatrix usage

Open `bibliomatrix_master.xlsx` for a spreadsheet version or use the CSVs directly in R/VOSviewer.

- `matrix_paper_x_factuality_mechanism.csv`
- `matrix_paper_x_bangla_relevance.csv`
- `matrix_paper_x_controlled_tags.csv`

For Bibliometrix, run:

```r
source("generate_bibliomatrix.R")
```

For DOI checking, run:

```bash
python verify_dois_crossref.py factuality_clinical_ts_bangla_215refs.bib
```
