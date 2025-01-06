import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


def authenticate():
    CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
    CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
    
    manager = SpotifyOAuth(client_id=CLIENT_ID, 
                            client_secret=CLIENT_SECRET,
                            redirect_uri='http://localhost:8888/callback',
                            scope='user-library-read'
                            )
    
    sp = spotipy.Spotify(auth_manager=manager, retries=0)
    return sp