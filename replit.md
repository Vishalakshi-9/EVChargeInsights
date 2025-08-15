# Overview

This is an EV Charging Industry Analysis application that generates comprehensive consulting-style reports analyzing the electric vehicle charging market. The system performs strategic business analysis using frameworks like Porter's Five Forces and SWOT analysis, collecting data from various web sources and generating professional HTML reports with visualizations.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Application Structure
The application follows a modular architecture with four main components:
- **Data Collection Layer** (`data_collector.py`) - Handles web scraping and data gathering from industry sources
- **Analysis Engine** (`analysis_engine.py`) - Implements business analysis frameworks and competitive intelligence
- **Report Generation** (`report_generator.py`) - Creates professional HTML reports using Jinja2 templating
- **Orchestration Layer** (`main.py`) - Coordinates the entire analysis workflow

## Data Processing Pipeline
The system implements a sequential processing pipeline:
1. **Data Collection** - Scrapes industry data from Wikipedia and other sources using trafilatura
2. **Analysis** - Processes collected data through strategic frameworks
3. **Visualization** - Generates charts and graphs using matplotlib
4. **Report Generation** - Compiles results into professional HTML reports

## Template System
Uses Jinja2 templating engine for dynamic HTML report generation with:
- Professional CSS styling with CSS variables for theming
- Responsive design with Font Awesome icons
- Chart.js integration for interactive visualizations
- Modular template structure for maintainability

## File Organization
The application creates a structured directory layout:
- `static/` - CSS stylesheets and assets
- `templates/` - HTML template files
- `data/` - Raw collected data storage
- `exports/` - Generated reports
- `visualizations/` - Chart and graph outputs

## Logging and Error Handling
Implements comprehensive logging using Python's logging module with:
- File-based logging (`ev_analysis.log`)
- Console output for real-time feedback
- Structured error handling throughout the pipeline

# External Dependencies

## Web Scraping and Data Collection
- **requests** - HTTP client for web requests
- **BeautifulSoup** - HTML parsing and extraction
- **trafilatura** - Optimized web content extraction
- **urllib.parse** - URL manipulation utilities

## Data Analysis and Visualization
- **numpy** - Numerical computing for data analysis
- **matplotlib** - Chart generation and data visualization
- **matplotlib.patches** - Advanced chart formatting

## Report Generation and Templating
- **Jinja2** - Template engine for HTML report generation
- **Chart.js** (CDN) - Interactive client-side charts
- **Font Awesome** (CDN) - Professional icons and styling

## Data Sources
- **Wikipedia** - Primary source for industry and company information
- **Various industry websites** - Market data and competitive intelligence

## Python Standard Library
- **json** - Data serialization and configuration
- **logging** - Application logging and debugging
- **datetime** - Timestamp generation and date handling
- **os** - File system operations and directory management
- **re** - Regular expressions for data processing
- **time** - Rate limiting and request throttling