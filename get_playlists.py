import os
import spotipy
from auth import authenticate
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

sp = authenticate()

def get_playlists(display=False):
    results = []
    offset = 0
    length = 0
    
    while True:
        response = sp.current_user_playlists(limit=100, offset=offset)
        results.extend(response['items'])
        
        length += len(response['items'])
        
        if response['next'] is None:
            break
        
        offset += len(response['items'])
        
        
    
    playlist_ids = [] 
    for playlist in results:
        if display:
            print(playlist['name'])
        playlist_ids.append(playlist['id'])
        
    if display:
        print(length)
        
    return playlist_ids

if __name__ == '__main__':   
    playlist_ids = get_playlists(display=True)