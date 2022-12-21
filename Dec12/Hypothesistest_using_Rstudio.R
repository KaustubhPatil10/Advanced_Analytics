setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
pg = read.csv("PlantGrowth.csv")

t.test(pg$weight, mu = 6, alternative = 't')
t.test(pg$weight, mu = 6, alternative = 'g')
t.test(pg$weight, mu = 6, alternative = 'l')

mean(pg$weight-6)/(sd(pg$weight)/sqrt(30))

co2<- read.csv("CO2.csv")
t.test(co2$uptake, mu =30, alternative ='t')
t.test(co2$uptake, mu =30, alternative ='g')
t.test(co2$uptake, mu =30, alternative ='l')

bartlett.test(co2$uptake ~ co2$Treatment)

indo<- read.csv("Indometh.csv")
t.test(indo$conc, mu =0.30, alternative ='t')
t.test(indo$conc, mu =0.30, alternative ='g')
t.test(indo$conc, mu =0.30, alternative ='l')