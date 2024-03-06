import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

with open("credentials.json","r") as file:
    credentials = json.load(file)

client_id = credentials["client_id"]
client_secret = credentials["client_secret"]


import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="Desmond Bai" 
    )
)
user_id = sp.current_user()["id"]
print(f"user_id:{user_id}")
