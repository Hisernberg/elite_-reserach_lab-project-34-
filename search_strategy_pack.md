# Search strategy pack

## S1 Clinical simplification + factuality

```text
("clinical text" OR "clinical note*" OR "electronic health record*" OR "discharge summar*" OR
 "pathology report*" OR "radiology report*" OR "medical report*" OR "biomedical abstract*" OR
 "patient education" OR "consumer health")
AND
("text simplif*" OR "sentence simplif*" OR "lay summar*" OR "plain language" OR
 "patient-friendly" OR "jargon definition" OR "explanation generation" OR "readability-controlled")
AND
(factuality OR faithfulness OR hallucination OR "medical accuracy" OR consistency OR contradiction
 OR entailment OR "natural language inference" OR NLI OR "constrained decoding" OR "entity preservation")
```

## S2 Bangla / Bengali / Indic healthcare NLP

```text
("Bangla" OR "Bengali" OR "bn" OR "Indic" OR "South Asian" OR "low-resource")
AND
("clinical" OR "medical" OR "biomedical" OR "healthcare" OR "consumer health" OR "health literacy")
AND
("NLP" OR "named entity recognition" OR NER OR "summarization" OR "question answering" OR
 "machine translation" OR "text simplification" OR paraphrase OR "language model")
```

## S3 RAG / graph / NLI factuality bridge

```text
("retrieval augmented generation" OR RAG OR GraphRAG OR "knowledge graph" OR ontology OR UMLS OR SNOMED)
AND
("medical" OR "clinical" OR biomedical OR healthcare)
AND
(factuality OR faithfulness OR hallucination OR "natural language inference" OR NLI OR safety)
```

## S4 General simplification benchmark and metrics

```text
("text simplification" OR "sentence simplification" OR "lexical simplification")
AND
(SARI OR BLEU OR ROUGE OR BERTScore OR readability OR "human evaluation" OR factuality)
AND
(transformer OR T5 OR BART OR mT5 OR LLM OR "large language model")
```

## Database notes

- ACL Anthology: use exact terms and export BibTeX per result page.
- PubMed/PubMed Central: add `[tiab]` and MeSH terms where possible.
- Scopus: `TITLE-ABS-KEY(...)`, document type Article + Conference Paper.
- Google Scholar: use only for snowballing and record date/query manually.
