library(dplyr)
library(shiny)
library(bslib)
library(DT)
library(arrow)

batting_seasons <- arrow::read_parquet("data/batting_seasons.parquet") 

source("utils.R")

batting_basic <- batting_seasons |>
  select(demo_basic_cols, batting_basic_cols)

batting_adv <- batting_seasons |>
  select(demo_basic_cols, batting_adv_cols)

batting_xplus <- batting_seasons |>
  select(demo_basic_cols, batting_xplus_cols)

batting_swing <- batting_seasons |>
  select(demo_basic_cols, batting_swing_cols)

# Define UI
ui <- page_sidebar(
  title = "Blyjections - Borderline Random Numbers You Should Not Use AKA Very Shitty Statcast AKA Shitty FanGraphs with Graphs",

  div(
    style = "text-align: center; margin-bottom: 20px; color: #666;",
    paste("Last updated:", Sys.Date())
  ),

  # Sidebar with input controls
  sidebar = sidebar(
    h5("Player Filters"),
    selectInput(
      "team",
      "Team:",
      choices = c("All" = "all", sort(unique(batting_seasons$Team))),
      selected = "all"
    ),

    sliderInput(
      "war_range",
      "WAR Range:",
      min = min(batting_seasons$WAR, na.rm = TRUE),
      max = max(batting_seasons$WAR, na.rm = TRUE),
      value = c(
        min(batting_seasons$WAR, na.rm = TRUE),
        max(batting_seasons$WAR, na.rm = TRUE)
      ),
      step = 0.1
    ),

    sliderInput(
      "season_range",
      "Season Range:",
      min = min(batting_seasons$Season, na.rm = TRUE),
      max = max(batting_seasons$Season, na.rm = TRUE),
      value = c(
        min(batting_seasons$Season, na.rm = TRUE),
        max(batting_seasons$Season, na.rm = TRUE)
      ),
      step = 1,
      sep = ""
    ),
  ),

  # Main panel with tabbed output
  navset_card_tab(
    nav_panel(
      "Basic Stats",
      card_body(
        DT::dataTableOutput("basic_table")
      )
    ),

    nav_panel(
      "Advanced Stats",
      card_body(
        DT::dataTableOutput("adv_table")
      )
    ),

    nav_panel(
      "xStats & Plus",
      card_body(
        DT::dataTableOutput("xplus_table")
      )
    ),

    nav_panel(
      "Swing Stats",
      card_body(
        DT::dataTableOutput("swing_table")
      )
    ),

    nav_panel(
      "Blyjections",
      card_body(
        DT::dataTableOutput("blyjections_table")
      )
    )
  )
)

# Define server logic
server <- function(input, output, session) {
  
  # Helper function to apply filters to any dataset
  apply_filters <- function(data) {
    req(input$team, input$war_range, input$season_range)
    
    # Filter by team
    if (input$team != "all") {
      data <- data[data$Team == input$team, ]
    }

    # Filter by WAR range (only if WAR column exists)
    if ("WAR" %in% colnames(data)) {
      data <- data[
        !is.na(data$WAR) & 
        data$WAR >= input$war_range[1] & 
        data$WAR <= input$war_range[2],
      ]
    }

    # Filter by season range
    data <- data[
      data$Season >= input$season_range[1] & 
      data$Season <= input$season_range[2],
    ]

    return(data)
  }

  # Reactive data filtering for all datasets
  filtered_basic <- reactive({
    apply_filters(batting_basic)
  })
  
  filtered_adv <- reactive({
    apply_filters(batting_adv)
  })
  
  filtered_xplus <- reactive({
    apply_filters(batting_xplus)
  })
  
  filtered_swing <- reactive({
    apply_filters(batting_swing)
  })

  # Render the basic stats table
  output$basic_table <- DT::renderDataTable({
    data <- filtered_basic()

    DT::datatable(
      data,
      options = list(
        pageLength = 15,
        scrollX = TRUE,
        dom = 'frtip'
      ),
      rownames = FALSE,
      escape = FALSE
    )
  })
  
  # Render the advanced stats table
  output$adv_table <- DT::renderDataTable({
    data <- filtered_adv()

    DT::datatable(
      data,
      options = list(
        pageLength = 15,
        scrollX = TRUE,
        dom = 'frtip'
      ),
      rownames = FALSE,
      escape = FALSE
    )
  })
  
  # Render the xplus stats table
  output$xplus_table <- DT::renderDataTable({
    data <- filtered_xplus()

    DT::datatable(
      data,
      options = list(
        pageLength = 15,
        scrollX = TRUE,
        dom = 'frtip'
      ),
      rownames = FALSE,
      escape = FALSE
    )
  })
  
  # Render the swing stats table
  output$swing_table <- DT::renderDataTable({
    data <- filtered_swing()

    DT::datatable(
      data,
      options = list(
        pageLength = 15,
        scrollX = TRUE,
        dom = 'frtip'
      ),
      rownames = FALSE,
      escape = FALSE
    )
  })
}

# Run the application
shinyApp(ui = ui, server = server)
