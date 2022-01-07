from time import sleep
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

client_id = ''
client_secret = ''
current_track = ''
SCOPE = "user-read-playback-state"

# while(True):
    # Check if current song is new

token = util.prompt_for_user_token("basketballer820", client_id=client_id, client_secret=client_secret, scope=SCOPE, redirect_uri="http://localhost:8080")
sp = spotipy.Spotify(auth=token)
while(True):
    pt = sp.current_user_playing_track()
    ct = (pt.get('item')).get('uri')
    if ct != current_track:
        current_track = ct
        syncing = sp.audio_analysis((pt.get('item')).get('uri'))
        print("song changed")

print()
