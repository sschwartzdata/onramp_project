# from helper_functions import data_pull
from helper_functions import db_connection
# from helper_functions.sql_queries import *
from classes.class_test import DataPull
# import pandas as pd
import spotipy
# from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def main():
    """
    Builds ETL pipeline for Sparkify Postgres database

    Connects to the Sparkify Postgres database and 
    populates the songs, artists, useres, time, and
    songplayed relations with data contained in JSON
    files located in the defined filepath.
    """

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    search_artists = ["Wild Child", "Tessa Violet", "Halsey", "OK Go",
                      "Regina Spektor", "Modest Mouse", "The Killers",
                      "the GazettE", "Dolly Parton", "Ed Sheeran",
                      "The Vaccines", "Bloc Party", "Simple Plan",
                      "Creedence Clearwater Revival", "Miike Snow",
                      "Adele", "Grace VanderWaal", "Simple Plan",
                      "blink-182", "MIYAVI"]
    spotify_data_pull = DataPull(sp)

    spotify_data_pull.artist_data_pull(search_artists)

    spotify_data_pull.pull_artist_albums()

    spotify_data_pull.remove_album_dups()
    spotify_data_pull.get_tracks()
    spotify_data_pull.get_track_info()

    db_connection()


if __name__ == "__main__":
    main()
