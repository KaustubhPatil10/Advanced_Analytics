

library(shiny)
setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
boston <- read.csv("Boston.csv")
library(ggplot2)


shinyServer(function(input, output) {

    output$hist <- renderPlot({
     df <-data.frame(col1=boston[,input$num_var])
     ggplot(data=df,aes(x=col1))+
       geom_histogram(bins=20,color='black',fill='skyblue')+
       labs(x=input$num_var)



    })

})
