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
drop_table_track_feature  = "DROP TABLE IF EXISTS track_feature"

# Creating tables

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artist (
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

album_table_create = ("""
    CREATE TABLE IF NOT EXISTS album (
        album_id       varchar(50)  PRIMARY KEY
        , album_name   varchar(255)
        , external_url varchar(100)
        , image_url    varchar(100)
        , release_date date
        , total_tracks int
        , type         varchar(50)
        , album_uri    varchar(100)
        , artist_id    varchar(50)
        ;""")

track_table_create = ("""
    CREATE TABLE IF NOT EXISTS track (
        track_id       varchar(50)  PRIMARY KEY
        , song_name    varchar(255)
        , external_url varchar(100)
        , duration_ms  int
        , explicit     boolean
        , disc_number  int
        , type         varchar(50)
        , song_uri     varchar(100)
        , album_id     varchar(50)
        ;""")

track_feature_table_create = ("""
    CREATE TABLE IF NOT EXISTS track_feature (
        track_id            varchar(50)  PRIMARY KEY
        , daceablility      double
        , energy            double
        , instrumentalness  double
        , liveness          double
        , loudness          double
        , speechiness       double
        , tempo             double
        , type              varchar(50)
        , valence           double
        , song_uri          varchar(100)
        ;""")

# Insert data into tables

artist_table_insert = ("""
    INSERT INTO artist (artist_id, artist_name, external_url,
    genre, image_url, followers, popularity, type, artist_uri)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    ;""")

album_table_insert = ("""
    INSERT INTO album (album_id, album_name, external_url,
    image_url, release_date, total_tracks, type, album_uri,
    artist_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    ;""")

track_table_insert = ("""
    INSERT INTO track (track_id, song_name, external_url,
    duration_ms, explicit, disc_number, type, song_uri,
    album_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    ;""")

track_feature_table_insert = ("""
    INSERT INTO track_feature (track_id, daceablility, energy,
    instrumentalness, liveness, loudness, speechiness, tempo,
    type, valence, song_uri)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
    ;""")



# QUERY LISTS

create_table_queries = [artist_table_create, album_table_create, track_table_create, track_feature_table_create]
drop_table_queries = [drop_table_artist, drop_table_album, drop_table_track, drop_table_track_feature]
