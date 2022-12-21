setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
plant <- read.csv("PlantGrowth.csv")
plant_ols <- aov(weight ~ group, data = plant)
anova(plant_ols)

# Tukey's test
TukeyHSD(plant_ols)