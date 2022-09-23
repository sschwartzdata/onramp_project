"""
    This file contains all of the queries that will be run in the sqlite database.
    These queries include
    * drop tables
    * create tables
"""

# Drop tables if they exist

drop_table_artist   = "DROP TABLE IF EXISTS artist"
drop_table_album    = "DROP TABLE IF EXISTS album"
drop_table_track    = "DROP TABLE IF EXISTS track"
drop_table_feature  = "DROP TABLE IF EXISTS track_feature"

# Creating tables

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        artist_id      varchar(50)  PRIMARY KEY
        , artist_name  varchar(255)
        , external_url varchar(100)
        , genre        varchar(100)
        , image_url    varchar(100)
        , followers    int
        , popularity   int
        , type         varchar(50)
        , artist_uri   varchar(100)
        ;""")