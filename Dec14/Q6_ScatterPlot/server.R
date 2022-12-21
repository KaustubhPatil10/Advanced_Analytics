

library(shiny)
setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
boston <- read.csv("Boston.csv")
library(ggplot2)


shinyServer(function(input, output) {
  
  output$scatter <- renderPlot({
    df <-boston[,c(input$num_x,input$num_y)]
    plot(df[,1],df[,2],xlab = input$num_x, ylab = input$num_y)

    
    
    
  })
  
})
