import os
import spotipy
from auth import authenticate
from spotipy.oauth2 import SpotifyOAuth

import get_playlists
import get_playlist_tracks

sp = authenticate()

def search_all():
    ''' Returns a list of lists containing playlist id and playlist_name'''
    p_ids = get_playlists.get_playlists()
    
    num_playlists = len(p_ids)
    print("num playlists:", num_playlists)
    
    results = []
    query = input("Enter track name: ")
    for n, p_id in enumerate(p_ids):
        print(f"searching playlist {n} of {num_playlists}")
        result = get_playlist_tracks.search_playlist(p_id, query)
        if result:
            playlist = sp.playlist(result)
            playlist_name = playlist["name"]
            
            print("Found in", playlist_name)
            print("ID:", p_id)

            results.append([result, playlist_name])
            
    return results
    
if __name__ == '__main__':
    results = search_all()

    if results:
        print("Found in following playlists.\n-----------")
    else:
        print("Not found in any playlist.")
        
    for result in results:
        print(result[1], f"\nPlaylist ID: {result[0]}\n")