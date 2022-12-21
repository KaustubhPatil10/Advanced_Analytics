library(shiny)
setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
cars93 <- read.csv("Cars93.csv")
shinyServer(function(input, output) {
  output$barplot <- renderPlot({
    barplot(cars93[,input$num_var],
         main=paste("Barplot of ",  input$num_var))
    
  })
  
})
