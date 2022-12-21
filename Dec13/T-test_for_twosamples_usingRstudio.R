setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
puro <- read.csv("Puromycin.csv")

bartlett.test(puro$rate ~ puro$state)
t.test(puro$rate  ~  puro$state, var.equal = T)
