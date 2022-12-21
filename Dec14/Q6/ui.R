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
      tabsetPanel(
        tabPanel("Histogram",plotOutput(outputId = "hist")),
        tabPanel("BoxPlot",plotOutput(outputId = "box")),
        tabPanel("Data",dataTableOutput(outputId = "tbl"))
  )
      
      
    )
  )
))
















