

library(shiny)


shinyUI(fluidPage(
  
  
  titlePanel("BOXPLOT"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = "num_var",
                  label = "Select a variable",
                  choices=list("crim","zn","indus",
                               "nox","rm","medv","age"))
    ),
    
    
    mainPanel(
      plotOutput(outputId = "hist"),
      plotOutput(outputId = "box")
    )
  )
))
















