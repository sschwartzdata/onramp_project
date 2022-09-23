    """
    This script allows the user to pull data from Spotify's API
    using the spotipy package.
    
    This script uses the users Spotify Client ID, Client Secret and 
    Redirect URI specified in their environmentals.
    """
# importind packages
import spotipy
from spotipy.oauth2 import SpotifyOAuth

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)




artist()

# Get Spotify catalog information about an artist’s albums
artist_albums()