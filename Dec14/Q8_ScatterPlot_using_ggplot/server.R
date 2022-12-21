

library(shiny)
setwd("C:/Kaustubh Vaibhav/Advance Analystics/Datasets")
boston <- read.csv("Boston.csv")
library(ggplot2)


shinyServer(function(input, output) {
  
  output$scatter <- renderPlot({
    df <-boston[,c(input$num_x,input$num_y)]
    colnames(df) <-c('col1','col2')
    ggplot(data=df,aes(x=col1,y=col2))+
      geom_point()+
    plot(df[,1],df[,2],xlab = input$num_x, ylab = input$num_y)
    
    
    
    
  })
  
})
