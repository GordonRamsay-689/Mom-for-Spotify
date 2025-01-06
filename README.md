Finds songs when you don't know where you put them.

Searches through all of the authenticated users playlists and returns
a list of [playlist_id, playlist_name].

Useful for Spotify users with multi-folder structures.

## Instructions

1. Install spotipy and authenticate Spotify Web API: https://spotipy.readthedocs.io/en/2.25.0/#installation
2. Export environment variables as:
```
export SPOTIFY_CLIENT_ID="YOUR_CLIENT_ID"
export SPOTIFY_CLIENT_SECRET="YOUR_CLIENT_SECRET"
```
3. Run the search_all module:
```
python3 search_all.py
```
4. Search for a track.