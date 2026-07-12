# Boolean Search Strategy Pack — v2

**Topic:** Factuality preservation in patient-facing medical/clinical text simplification with low-resource Bangla healthcare NLP evidence map.

**Corpus rule:** 2020–2025 analytical corpus. Include peer-reviewed journal articles and full-length top-tier conference papers. Exclude preprint-only arXiv records, non-archival demos/posters, and short weak conference papers, including ≤6-page IEEE conference papers unless they are a recognized top-tier full paper.

## Database execution order

1. ACL Anthology
2. PubMed / PubMed Central
3. Scopus
4. ScienceDirect
5. ACM Digital Library
6. IEEE Xplore
7. Google Scholar only for forward/backward citation chasing after database searches are locked

## Core search strings

### S1 — Core medical simplification + factuality

```text
("medical text simplification" OR "clinical text simplification" OR "biomedical text simplification" OR "lay summarization" OR "patient-friendly" OR "plain language") AND ("factuality" OR "faithfulness" OR "hallucination" OR "medical accuracy" OR "consistency" OR "entailment" OR "NLI") AND ("transformer" OR "T5" OR "BART" OR "GPT" OR "large language model" OR "LLM" OR "constrained decoding" OR "retrieval augmented")
```

Filters: 2020-2025; peer-reviewed journal OR full conference; exclude preprint-only; exclude short <=6-page IEEE conf.

### S2 — Medical jargon and lay explanation datasets

```text
("medical jargon" OR "lay definition" OR "consumer health vocabulary" OR "patient education") AND ("dataset" OR "corpus" OR "benchmark") AND ("NLP" OR "language model" OR "transformer")
```

Filters: 2020-2025; journal/full conference only

### S3 — Factuality / hallucination / faithfulness metrics

```text
("factuality" OR "faithfulness" OR "factual consistency" OR "hallucination") AND ("summarization" OR "text generation" OR "simplification" OR "NLG") AND ("metric" OR "evaluation" OR "benchmark" OR "human evaluation")
```

Filters: 2020-2025; top NLP venues/journals; exclude arXiv-only surveys unless peer-reviewed version exists

### S4 — Clinical / medical NLI

```text
("medical NLI" OR "clinical NLI" OR "MedNLI" OR "natural language inference") AND ("clinical" OR "medical" OR "biomedical" OR "health")
```

Filters: 2020-2025; peer-reviewed only

### S5 — Bangla / Bengali healthcare NLP

```text
("Bangla" OR "Bengali" OR "Indic") AND ("medical" OR "clinical" OR "healthcare" OR "consumer health") AND ("NLP" OR "NER" OR "summarization" OR "paraphrase" OR "translation" OR "question answering")
```

Filters: 2020-2025; peer-reviewed; include dataset papers; exclude generic sentiment-only unless health domain

### S6 — Multilingual / low-resource simplification

```text
("multilingual text simplification" OR "cross-lingual simplification" OR "low-resource text simplification" OR "translate then simplify") AND ("transformer" OR "mT5" OR "mBART" OR "LLM")
```

Filters: 2020-2025; ACL/EMNLP/NAACL/COLING/TACL/full journal

### S7 — RAG / KG / grounding for medical generation

```text
("retrieval augmented generation" OR "RAG" OR "knowledge graph" OR "GraphRAG" OR "grounded generation") AND ("medical" OR "clinical" OR "biomedical" OR "health") AND ("language model" OR "LLM" OR "generation")
```

Filters: 2020-2025; journal/full conference; preprint only excluded unless accepted

### S8 — Constrained / controlled decoding

```text
("constrained decoding" OR "controlled generation" OR "lexically constrained" OR "NeuroLogic" OR "plug and play language model") AND ("factuality" OR "simplification" OR "medical" OR "clinical" OR "text generation")
```

Filters: 2020-2025; top venues/journals

### S9 — Human evaluation / readability

```text
("human evaluation" OR "clinician evaluation" OR "patient comprehension" OR "readability") AND ("medical text" OR "clinical text" OR "health literacy") AND ("NLP" OR "language model" OR "simplification")
```

Filters: 2020-2025; journal/full conference; exclude editorials

## Platform syntax examples

### Scopus
```text
TITLE-ABS-KEY(("medical text simplification" OR "clinical text simplification" OR "lay summarization" OR "patient-friendly" OR "plain language")
AND ("factuality" OR "faithfulness" OR "hallucination" OR "medical accuracy" OR "entailment" OR "NLI")
AND ("transformer" OR "T5" OR "BART" OR "GPT" OR "large language model" OR "LLM"))
AND PUBYEAR > 2019 AND PUBYEAR < 2026
```

### PubMed
```text
(("clinical text"[tiab] OR "medical text"[tiab] OR "discharge summary"[tiab] OR "patient education"[tiab])
AND ("simplification"[tiab] OR "plain language"[tiab] OR "lay summary"[tiab])
AND ("factuality"[tiab] OR "faithfulness"[tiab] OR "hallucination"[tiab] OR "medical accuracy"[tiab]))
AND ("2020/01/01"[Date - Publication] : "2025/12/31"[Date - Publication])
```

### ACL Anthology
Use exact phrase + AND blocks in anthology search, then export BibTeX/RIS where available:
```text
"medical text simplification" factuality
"clinical text simplification" faithfulness
"medical simplification" "large language model"
"Bangla" "health" "NLP"
```

### IEEE Xplore command search
```text
(("All Metadata":"medical text simplification" OR "All Metadata":"clinical text simplification" OR "All Metadata":"patient-friendly")
AND ("All Metadata":"factuality" OR "All Metadata":"faithfulness" OR "All Metadata":"hallucination")
AND ("All Metadata":"large language model" OR "All Metadata":"transformer"))
```

### ACM Digital Library
```text
[All: "medical text simplification"] AND ([All: factuality] OR [All: faithfulness] OR [All: hallucination]) AND [Publication Date: (01/01/2020 TO 12/31/2025)]
```

## Count logging rule

Do not type counts into the manuscript from memory. Run each search, export RIS/BibTeX, then enter the exact hit count into `search_log_boolean_counts_template.csv` and the workbook sheet `Search_Log_PRISMA`. This avoids non-reproducible Google-style counts.
