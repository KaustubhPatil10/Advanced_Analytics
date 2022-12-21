setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
plaque <- read.csv("Plaque.csv")

library(tidyr)
plaque <- read.csv("plaque.csv")
#View(plaque)


plaq_pivot <- pivot_wider(plaque, id_cols = c("Id","product"),
            names_from = "trt", values_from = "score")


P1 <- subset(plaq_pivot, product== "P1")
t.test(P1$Before, P1$After, paired = T, alternative = 'g')

P2 <- subset(plaq_pivot, product== "P2")
t.test(P2$Before, P2$After, paired = T, alternative = 'g')

P3 <- subset(plaq_pivot, product== "P3")
t.test(P3$Before, P3$After, paired = T, alternative = 'g')
# View(P3)