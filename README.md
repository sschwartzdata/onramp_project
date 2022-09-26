# Project : onramp_project
Project for final interview round of Onramp's Vanguard Data Engineer Apprenticeship 

## Description


## Requirements
Data requirements:
- [x] 20 artists of my choise
- [x] atleast 1000 rows of track data

Process
- [x] Extract and transform data from spotify
- [x] Create required tables in SQLite database
- [x] Load data into database
- [x] Create 3 required views
- [x] Create 2 other views
- [] Create 3 data visualization


Deliverables
- [x] Python Code for ETL pipeline
- [x] spotify.db file
  - [x] 5 views
- [] pdf with 3 data visualizations



## Project file structure


``` bash
.
├── Submissions                 # Test files (alternatively `spec` or `tests`)
│   ├── etl.py                  # Script to Extract, Transform and Load the data
│   ├── proof_of_concept.ipynb  # Documents the thought proccess for building the pipeline
│   ├── classes                 # Contains all custom classes used in etl.py
|       ├── data_pull.py                 # Test files (alternatively `spec` or `tests`)
|       ├── db_connection.py             # Test files (alternatively `spec` or `tests`)
│   ├── db_files                # Contains final database file
|       ├── spotify.db                   # SQLite Spotify database files
│   ├── helper_functions        # Contains all custom functions and sql queries used in etl.py
|       ├── db_views.py                  # Contains the function used to create the views in spotify.db
|       ├── load.py                      # Contains the function used to load data into spotify.db
|       ├── sql_queries.py               # Contains all SQL queries for the project
│   └── test                    # Unit and data validation tests
└── ...

```
