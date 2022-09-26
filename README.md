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
|   |   ├── data_pull.py                 # Test files (alternatively `spec` or `tests`)
|   |   ├── db_connection.py             # Test files (alternatively `spec` or `tests`)
│   ├── db_files                # Contains final database file
|   |   ├── spotify.db                   # SQLite Spotify database files
│   ├── helper_functions        # Contains all custom functions and sql queries used in etl.py
|   |   ├── db_views.py                  # Contains the function used to create the views in spotify.db
|   |   ├── load.py                      # Contains the function used to load data into spotify.db
|   |   ├── sql_queries.py               # Contains all SQL queries for the project
│   └── test                    # Unit and data validation tests
└── ...

```


## ELT Pipeline
Extract, transform, load (ETL) is the general procedure of copying data from one or more sources into a destination system which represents the data differently from, or in a different context than, the sources.

### Extracting, Transforming, and Loading the Data

The ETL pipeline extracts data from Spotify's API four times using the package spotipy. The flow of the ETL pipeline is:
- Extract
  - Use personally selected artist to pull all required information about each artist
    -  Create a list of the artist's ids
  - Use artist id list to pull all albums created by each artist
  - Remove duplicate albums including remixes and region variants
    -  Create a list of the album's ids
  - Use cleaned list of album ids to pull information for all tracks on each album
    - Create a list of the track's ids
  - Use list of track ids to pull all track feature information
- Transform
- Load
  - Create a connection to the database
  - Drop tables if they exist
  - Create tables
  - use load.py to load data into spotify.py
- Analysis
  - Create views in spotipy.bd using create_view.db
  - Create data visualizations using matplotlib and seaborn packages


Running the the ELT pipline:
- Insure the following python packages are installed
  -   \<spotipy\>
  -   \<spotipy.oauth2\>
  -   \<pandas\>
  -   \<sqlite3\>
  -   \<matplotlib\>
  -   \<seaborn>\
- Insure that you have a developer account with Spotify and you have the following environmental settings defined on your local computer
  - \<SPOTIPY_CLIENT_ID >\
  - \<SPOTIPY_CLIENT_SECRET>\
  - \<SPOTIPY_REDIRECT_URI>\
- Run \<python etl.py\>
    - Data will be extracted from the Spotify's API files and transformed and loaded into the spotipy.db.
