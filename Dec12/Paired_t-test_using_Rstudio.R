setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
anorexia <- read.csv("anorexia.csv")

cont <- subset(anorexia, Treat== "Cont")

t.test(cont$Prewt, cont$Postwt, mu=0, paired = T, alternative ="l")

cbt <- subset(anorexia, Treat== "CBT")
t.test(cbt$Prewt, cbt$Postwt, mu=0, paired = T, alternative ="l")

ft <- subset(anorexia, Treat== "FT")
t.test(ft$Prewt, ft$Postwt, mu=0, paired = T, alternative ="l")