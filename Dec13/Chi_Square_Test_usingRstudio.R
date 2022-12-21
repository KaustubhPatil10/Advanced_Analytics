setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
housing <- read.csv("Housing.csv")

# table is used as crosstab in spyder. 
ctab <- table(housing$gashw, housing$prefarea)
chisq.test(ctab)
