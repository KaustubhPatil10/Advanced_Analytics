

library(shiny)
setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
cars93 <- read.csv("Cars93.csv")
library(ggplot2)


shinyServer(function(input, output) {
  
  output$scatter <- renderPlot({
    df <-cars93[,c(input$num_x,input$num_y,input$colour)]
    colnames(df) <-c('col1','col2','col3')
    ggplot(data=df,aes(x=col1,y=col2,color=col3))+
      geom_point()+
      labs(x=input$num_x,y=input$num_y,color=input$colour)
    
    
    
    
    
  })
  
})
