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
    search = search.upper()
    first_char = search[0]

    while True:
        response = sp.playlist_items(playlist_id,
                                     offset=offset,
                                     fields='items.track.name',
                                     additional_types=['track'])

        playlists = response['items']

        if not playlists:
            break
        
        for playlist in playlists:
            offset += 1

            current = playlist['track']['name']
            
            if not current:
                continue

            current = current.upper()
            
            if first_char != current[0]:
                continue

            if search in current:
                print("Matched:", current)
                return p_id        
    
    if display:
        print("Number of tracks in playlist:", length)
    
    return None