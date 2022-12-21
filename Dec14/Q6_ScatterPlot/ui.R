

library(shiny)


shinyUI(fluidPage(
  
  
  titlePanel("ScatterPloT"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = "num_x",
                  label = "Select x-axis a variable",
                  choices=list("crim","zn","indus",
                               "nox","rm","medv","age")),
      selectInput(inputId = "num_y",
                  label = "Select y-axis a variable",
                  choices=list("crim","zn","indus",
                               "nox","rm","medv","age"))
    ),
    
    
    mainPanel(
      plotOutput(outputId = "scatter")
    )
  )
))
















