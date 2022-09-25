"""
    This file contains all of the queries that will be run in
    the sqlite database.
    These queries include
    * drop tables
    * create tables
"""

# Drop tables if they exist

drop_table_artist         = "DROP TABLE IF EXISTS artist"
drop_table_album          = "DROP TABLE IF EXISTS album"
drop_table_track          = "DROP TABLE IF EXISTS track"
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
        , artist_uri   varchar(100))
        """)

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
        , artist_id    varchar(50))
        """)

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
        , album_id     varchar(50))
        """)

track_feature_table_create = ("""
    CREATE TABLE IF NOT EXISTS track_feature (
        track_id            varchar(50)  PRIMARY KEY
        , danceability      double
        , energy            double
        , instrumentalness  double
        , liveness          double
        , loudness          double
        , speechiness       double
        , tempo             double
        , type              varchar(50)
        , valence           double
        , song_uri          varchar(100))
        """)

# Insert data into tables

artist_table_insert = ("""
    INSERT INTO artist (artist_id, artist_name, external_url,
    genre, image_url, followers, popularity, type, artist_uri)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT DO NOTHING
    """)

album_table_insert = ("""
    INSERT INTO album (album_id, album_name, external_url,
    image_url, release_date, total_tracks, type, album_uri,
    artist_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT DO NOTHING
    """)

track_table_insert = ("""
    INSERT INTO track (track_id, song_name, external_url,
    duration_ms, explicit, disc_number, type, song_uri,
    album_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT DO NOTHING
    """)

track_feature_table_insert = ("""
    INSERT INTO track_feature (track_id, daceablility, energy,
    instrumentalness, liveness, loudness, speechiness, tempo,
    type, valence, song_uri)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT DO NOTHING
    """)

# View Creation

query_longest_song = ("""
    CREATE VIEW IF NOT EXISTS top_artist_time (
    artist_name
    , duration_ms
    )
    AS
    SELECT a.artist_name
    , t.song_name
    , MAX(t.duration_ms)
    FROM artist AS a
    JOIN album AS al
        ON a.artist_id = al.artist_id
    JOIN track AS t
        ON al.album_id = t.album_id
    GROUP BY a.artist_name
    ORDER BY a.artist_name ASC
    """)

query_most_followers = ("""
    CREATE VIEW IF NOT EXISTS top_artist_followers (
    artist_name
    , followers
    )
    AS
    SELECT artist_name
        , followers
    FROM artist
    ORDER BY followers DESC
    """)

query_max_tempo = ("""
    CREATE VIEW IF NOT EXISTS top_songs_artist_tempo (
    artist_name
    , song_name
    , max_tempo
    )
    AS
    SELECT a.artist_name
        , t.song_name
        , MAX(tf.tempo)
    FROM artist AS a
    JOIN album AS al
        ON a.artist_id = al.artist_id
    JOIN track AS t
        ON al.album_id = t.album_id
    JOIN track_feature AS tf
        ON t.track_id = tf.track_id
    GROUP BY a.artist_name
    ORDER BY a.artist_name ASC
    """)

query_most_dance = ("""
    CREATE VIEW IF NOT EXISTS top_songs_artist_tempo (
    song_name
    , danceability
    )
    AS
    SELECT t.song_name
        , tf.danceability
    FROM track AS t
    JOIN track_feature AS tf
        ON tf.track_id = t.track_id
    ORDER BY tf.danceability DESC
    LIMIT 15
    """)

query_running_tempo = ("""
    CREATE VIEW IF NOT EXISTS top_songs_artist_tempo (
    artist_name,
    song_name,
    tempo
    )
    AS
    SELECT a.artist_name
        , t.song_name
        , tf.tempo
    FROM artist AS a
    JOIN album AS al
        ON a.artist_id = al.artist_id
    JOIN track AS t
        ON al.album_id = t.album_id
    JOIN track_feature AS tf
        ON t.track_id = tf.track_id
    WHERE tf.tempo BETWEEN 120 and 125
    ORDER BY tf.danceability DESC
    """)

# QUERY LISTS

create_table_queries = [artist_table_create, album_table_create,
                        track_table_create, track_feature_table_create]
drop_table_queries = [drop_table_artist, drop_table_album, drop_table_track,
                      drop_table_track_feature]
create_view_queries = [query_longest_song, query_most_followers,
                       query_max_tempo, query_most_dance, query_running_tempo]
