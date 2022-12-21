

library(shiny)


shinyUI(fluidPage(

    # Application title
    titlePanel("BARPLOT"),

    sidebarLayout(
        sidebarPanel(
            selectInput(inputId = "num_var",
            label = "Select a variable",
            choices = list("Price","MPG.highway",
                           "MPG.city","EngineSize",
                           "Horsepower","Fuel.tank.capacity"))
        ),
        mainPanel(
            plotOutput(outputId = "barplot")
        )
    )
))
