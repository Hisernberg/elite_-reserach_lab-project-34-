# Systematic Review v2 Package

Prepared for: **Factuality preservation in clinical/medical text simplification with low-resource Bangla healthcare NLP evidence map**.

## Main files

- `systematic_review_workbook_v2.xlsx` — dashboard, search log, Top-80 corpus, model table, PRISMA, RoB, GRADE, gap map.
- `selected_top80_corpus.bib` — Overleaf-ready BibTeX for the analytical corpus.
- `overleaf_main_skeleton.tex` — JBI/Elsevier-style LaTeX skeleton.
- `top80_selected_corpus.csv` — final v2 selected study table.
- `search_strategy_boolean_ready.md` — database-specific Boolean strings.
- `search_log_boolean_counts_template.csv` — exact place to enter hit counts after running database searches.
- `prisma_counts_template.csv` and `prisma_flow_mermaid_template.md` — editable PRISMA workflow.
- `model_comparison_table.csv` — model/method comparison with parameters/open status.
- `dataset_inventory.csv` — dataset/resource table.
- `gap_rq_matrix.csv` — gap-to-RQ-to-future-work map.
- `data_extraction_top80_template.csv`, `risk_of_bias_top80_template.csv`, `grade_sof_template.csv`.

## Important note on counts

This package does **not** fabricate database hit counts. The workbook contains target PRISMA counts for a 400+ to 80 workflow and exact columns for locked database counts. After you run each database query, paste the official hit counts and exported file names into `Search_Log_PRISMA`.

## Corpus rule

The v2 analytical corpus selects 80 peer-reviewed records from the prior 215-record library using these filters:

1. 2020–2025.
2. Peer-reviewed journal or full-length conference.
3. Preprint-only records removed.
4. Methodology anchors and model-backbone-only records kept outside the analytical corpus.
5. Lower-tier working notes/weak short proceedings excluded from the top 80.
6. DOI/ACL/PMID/stable URL retained for traceability.

Generated: 2026-07-05T16:51:17
