setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
agr <- read.csv("Yield.csv")
agr_ols <- aov(Yield ~ Treatments, data = agr)
anova(agr_ols)

# Tukey's test
TukeyHSD(agr_ols)