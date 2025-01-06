import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from auth import authenticate

sp = authenticate()

def search_playlist(p_id, search, display=False):
    playlist_id = p_id
    results = sp.playlist(playlist_id)
    
    offset = 0
    
    length = 0
    while True:
        response = sp.playlist_items(playlist_id,
                                     offset=offset,
                                     fields='items.track.name',
                                     additional_types=['track'])
    
        if len(response['items']) == 0:
            break
    
        if display:
            pprint(response['items'])
        
        for item in response['items']:
            if search.upper() in item['track']['name'].upper():
                print(p_id)
                print(item['track']['name'].upper())
                return p_id
            
        offset = offset + len(response['items'])
        length += len(response['items'])    
    
    if display:
        print("Number of tracks in playlist:", length)
    
    return None