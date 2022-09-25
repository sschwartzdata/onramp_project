"""
This script allows the user to pull data from Spotify's API
using the spotipy package.
    
This script uses the users Spotify Client ID, Client Secret and
Redirect URI specified in their environmentals.
"""
# importing packages
import spotipy
# from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


# Establishing list of artists

search_artists = ["Wild Child", "Tessa Violet", "Halsey", "OK Go",
                  "Regina Spektor", "Modest Mouse", "The Killers",
                  "the GazettE", "Dolly Parton", "Ed Sheeran",
                  "The Vaccines", "Bloc Party", "Simple Plan",
                  "Creedence Clearwater Revival", "Miike Snow",
                  "Adele", "Grace VanderWaal", "Simple Plan",
                  "blink-182", "MIYAVI"]

# List of columns for the dataframes

# df_artist
artist_table_columns = ['artist_id', 'artist_name', 'external_url',
                        'genre', 'image_url', 'followers', 'popularity',
                        'type', 'artist_uri']

# df_album
album_table_columns = ['album_id', 'album_name', 'external_url',
                       'image_url', 'release_date', 'total_tracks',
                       'type', 'album_uri', 'artist_id']

# df_track
track_table_columns = ['track_id', 'song_name', 'external_url', 'duration_ms',
                       'explicit', 'disc_number', 'type', 'song_uri',
                       'album_id']

# df_track_feature
track_feature_table_columns = ['track_id', 'danceability', 'energy',
                               'instrumentalness', 'liveness', 'loudness',
                               'speechiness', 'tempo', 'type', 'valence',
                               'song_uri']

# Creating the dataframes
df_artist = pd.DataFrame(columns=artist_table_columns)
df_album = pd.DataFrame(columns=album_table_columns)
df_album_nodup = pd.DataFrame(columns=album_table_columns)
df_track = pd.DataFrame(columns=track_table_columns)
df_track_feature = pd.DataFrame(columns=track_feature_table_columns)


# Pulling the information for all artists in search_artists
def artist_data_pull(artist_list):
    for artist in artist_list:

        # Requesting results for each artist in list where type is "artist"
        result = sp.search(q=artist, type="artist")

        # Selecting all data within 'items' in the pulled data
        item = result['artists']['items']

        # Creating a list of required data to enter into artist_df
        new_row = [item[0]['id'],  # artist id
                   item[0]['name'],  # artist name
                   item[0]['external_urls']['spotify'],  # external url
                   item[0]['genres'][0],  # selecting the first genres
                   item[0]['images'][0]['url'],  # selection the first image
                   item[0]['followers']['total'],  # followers
                   item[0]['popularity'],  # populatrity
                   item[0]['type'],  # type
                   item[0]['uri']]  # artist uri

        # Inserting pulled data into last row of artist_df
        df_artist.loc[len(df_artist.index)] = new_row


# Get Spotify catalog information about an artist’s albums
def pull_artist_albums(artist_ids):

    for artist_id in artist_ids:
        # Requesting results for each artist_id in list where type is "album"
        results = sp.artist_albums(artist_id, album_type='album')

        # Selecting all data within 'items' in the pulled data
        items = results['items']

        # Pulling all of the albums from the artist
        for i in range(len(items)):
            new_row = [items[i]['id'],  # alumb id
                       items[i]['name'],  # album name
                       items[i]['external_urls']['spotify'],  # external url
                       items[i]['images'][0]['url'],  # first image result
                       items[i]['release_date'],  # release date
                       items[i]['total_tracks'],  # number of tracks
                       items[i]['type'],  # album type
                       items[i]['uri'],  # album uri
                       artist_id]  # artist id

            # Inserting pulled data into last row of album_df
            df_album.loc[len(df_album.index)] = new_row


# Removing redundant albums
def remove_album_dups(df_album):
    # removing albums with same names
    df_album_nodup = df_album.drop_duplicates(subset=['album_name'])

    # removing redundant albums based on key words
    to_remove = ['Remix', 'remix', 'Version', 'version', 'Delux',
                 'Edition', 'Live', 'Mix', 'Tour', 'Remaster', 'Anthology']
    for words in to_remove:
        df_album_nodup = df_album_nodup[df_album_nodup["album_name"].str.contains(words) == False]

        removed_rows = len(df_album.index) - len(df_album_nodup.index)

    print(f"A total of {removed_rows} duplicate albums have been removed.")
    return df_album_nodup


# Get Spotify catalog information on tracks
def get_tracks(album_ids):
    """ This function searches for the artists name given that
    was given as an argument and returns the first result. If there
    are no result, nothing is returned"""
    for album_id in album_ids:
        results = sp.album_tracks(album_id)
        # Selecting all data within 'items' in the pulled data
        item = results['items']

        for i in range(len(item)):
            new_row = [item[i]['uri'],  # song uri
                       item[i]['name'],  # song name
                       item[i]['external_urls']['spotify'],
                       item[i]['duration_ms'],  # duration in ms
                       item[i]['explicit'],  # is explicit
                       item[i]['disc_number'],  # disc number
                       item[i]['type'],  # track type
                       item[i]['uri'],  # track uri
                       album_id]  # album id

            # Inserting pulled data into last row of track_df
            df_track.loc[len(df_track.index)] = new_row


# Get Spotify catalog information on song features
def get_track_info(track_ids):

    for track_id in track_ids:

        result = sp.audio_features(track_id)[0]

        try:
            new_row = [track_id,  # track's id
                       result['danceability'],  # danceability
                       result['energy'],  # enegy level
                       result['instrumentalness'],  # instramental level
                       result['liveness'],  # liveness level
                       result['loudness'],  # loudness level
                       result['speechiness'],  # speah level
                       result['tempo'],  # track's tempo
                       result['type'],  # track type
                       result['valence'],  # valence
                       result['uri']]  # tracks uri

        except Exception as e:
            print("There was an issue with a track.")
            print(e)
        df_track_feature.loc[len(df_track_feature.index)] = new_row


def null_varification():
    final_dfs = [(df_artist, 'df_artist'),
                 (df_album_nodup, 'df_album_nodup'),
                 (df_track, 'df_track'),
                 (df_track_feature, 'df_track_feature')]

    for df, df_name in final_dfs:
        print(f"Count total NULL in {df_name} : \n\n",
              df.isnull().sum().sum())



def main():
    """
    - Pulls artist information from predetermined list

    - Pulls info for all artists' albums

    - Removes duplicated albums

    - Pulls all tracks for albums

    - Pulls all feature information for each track

    - Reports the number of nulls for each dataframe
    """
    print("Populating artist_df.")
    artist_data_pull(search_artists)

    artist_ids = df_artist["artist_id"].to_list()
    print("Populating album_df.")
    pull_artist_albums(artist_ids)

    print("Removing duplicate albums.")
    df_album_nodup = remove_album_dups(df_album)

    album_ids = df_album_nodup["album_id"].to_list()
    print("Populating track_df.")
    get_tracks(album_ids)

    track_ids = df_track["track_id"].tolist()
    print("Populating track_feature_df.")
    get_track_info(track_ids)

    print("Starting data check.")
    null_varification()

    print("Data pull and verification is complete!")

    return df_artist, df_album_nodup, df_track, df_track_feature


if __name__ == "__main__":
    main()
