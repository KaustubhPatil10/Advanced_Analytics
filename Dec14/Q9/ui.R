

library(shiny)


shinyUI(fluidPage(
  
  
  titlePanel("ScatterPloT"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = "num_x",
                  label = "Select x-axis a variable",
                  choices=list("Price","MPG.city","MPG.highway",
                               "EngineSize","Horsepower","Fuel.tank.capacity")),
      selectInput(inputId = "num_y",
                  label = "Select y-axis a variable",
                  choices=list("MPG.city","Price","Horsepower",
                               "MPG.highway","Fuel.tank.capacity","EngineSize")),
      selectInput(inputId = "colour",
                  label = "Select colour",
                  choices=list("MPG.city","Price","Horsepower",
                               "MPG.highway","Fuel.tank.capacity","EngineSize"))
    ),
    
    
    mainPanel(
      plotOutput(outputId = "scatter")
    )
  )
))


































