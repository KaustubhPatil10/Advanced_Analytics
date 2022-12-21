setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
rheum <- read.csv("Rheumatic.csv")

t.test(rheum$Before, rheum$After, paired = T, alternative = "l")
# or

t.test(rheum$After, rheum$Before, paired = T, alternative = "g")