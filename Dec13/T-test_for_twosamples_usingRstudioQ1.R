setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
soporific <- read.csv("Soporific.csv")

library(tidyr)
sop1 <- soporific %>% pivot_longer(c(Drug.A, Drug.B),
                                   names_to="Drug",
                                   values_to = "Effect")
bartlett.test(sop1$Effect ~ sop1$Drug)
t.test(sop1$Effect ~  sop1$Drug)


############################################
