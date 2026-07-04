# generate_bibliomatrix.R
# Input: factuality_clinical_ts_bangla_215refs.bib
# Output: bibliometrix CSVs and plots for review paper.

# install.packages("bibliometrix")
library(bibliometrix)

bibfile <- "factuality_clinical_ts_bangla_215refs.bib"
M <- convert2df(file = bibfile, dbsource = "generic", format = "bibtex")

results <- biblioAnalysis(M, sep = ";")
sink("bibliometrix_summary.txt")
print(summary(results, k = 20))
sink()

annual <- annualScientificProduction(M)
write.csv(annual, "annual_scientific_production.csv", row.names = FALSE)

# Keyword co-occurrence network
NetMatrix <- biblioNetwork(M, analysis = "co-occurrences", network = "keywords", sep = ";")
write.csv(as.matrix(NetMatrix), "keyword_cooccurrence_matrix.csv")

# Author collaboration network
CollabMatrix <- biblioNetwork(M, analysis = "collaboration", network = "authors", sep = ";")
write.csv(as.matrix(CollabMatrix), "author_collaboration_matrix.csv")

# Co-citation network where references are present in imported source records
# This is most useful after importing Scopus/Web of Science records with cited references.
# CocitMatrix <- biblioNetwork(M, analysis = "co-citation", network = "references", sep = ";")
# write.csv(as.matrix(CocitMatrix), "cocitation_matrix.csv")

png("annual_scientific_production.png", width = 1800, height = 1200, res = 200)
plot(annual, main = "Annual Scientific Production")
dev.off()

png("three_field_plot.png", width = 2200, height = 1400, res = 200)
threeFieldsPlot(M, fields = c("AU", "DE", "SO"), n = c(15, 15, 15))
dev.off()
