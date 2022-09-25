# from helper_functions import data_pull
from helper_functions import load
from helper_functions import sql_queries
from helper_functions import db_views
from classes.data_pull import DataPull
from classes.db_connection import DatabaseGen
#from classes.load import DataLoad
# import pandas as pd
import spotipy
# from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials



def main():
    """
    Builds ETL pipeline for Sparkify Postgres database
    Connects to the Sparkify Postgres database and 
    populates the songs, artists, useres, time, and
    songplayed relations with data contained in JSON
    files located in the defined filepath.
    """
    # SET UP
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    database_path = r"db_files/spotify.db"

    search_artists = ["Wild Child", "Tessa Violet", "Halsey", "OK Go",
                      "Regina Spektor", "Modest Mouse", "The Killers",
                      "the GazettE", "Dolly Parton", "Ed Sheeran",
                      "The Vaccines", "Bloc Party", "Simple Plan",
                      "Creedence Clearwater Revival", "Miike Snow",
                      "Adele", "Grace VanderWaal", "Simple Plan",
                      "blink-182", "MIYAVI"]

    # EXTRACTION AND TRANSFORMATION

    spotify_data_pull = DataPull(sp)

    spotify_data_pull.artist_data_pull(search_artists)

    spotify_data_pull.pull_artist_albums()

    spotify_data_pull.remove_album_dups()
    spotify_data_pull.get_tracks()
    spotify_data_pull.get_track_info()

    # Dataframes

    df_artist = spotify_data_pull.return_artist()
    df_album_nodup = spotify_data_pull.return_album()
    df_track = spotify_data_pull.return_track()
    df_track_feature_nodup = spotify_data_pull.return_track_feature()

    # NULL AND DUPLICATE TEST
    # CREATING DATABASE
    # creating database generator object
    db_con = DatabaseGen(database_path)

    con = db_con.create_connection()
    db_con.drop_tables(con, sql_queries.drop_table_queries)
    db_con.create_tables(con, sql_queries.create_table_queries)

    # LOADING DATA TO DATABASE

    table_insert = [(df_artist, 'artist'), (df_album_nodup, 'album'),
                    (df_track, 'track'),
                    (df_track_feature_nodup, 'track_feature')]

    load.load_tables(con, table_insert)

    # CREATING VIEWS IN DATABASE
    db_views.create_views(con, sql_queries.create_view_queries)


if __name__ == "__main__":
    main()
