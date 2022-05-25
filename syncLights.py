from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

client_id = ''
client_secret = ''
current_track = ''
SCOPE = "user-read-playback-state"
redirect_uri = 'http://localhost:8080'

auth_manager = SpotifyOAuth(scope=SCOPE, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth_manager=auth_manager)
while(True):
    pt = sp.current_user_playing_track()
    ct = (pt.get('item')).get('uri')
    if ct != current_track:
        current_track = ct
        syncing = sp.audio_analysis((pt.get('item')).get('uri'))
        print("song changed")


