# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

import time

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

# ========================================================================
# SPOTIFY API 
# ========================================================================

ID = open("./REFERENCES/client_ID.txt", "r").read()
SECRET = open("./REFERENCES/client_secret.txt", "r").read()
REDIRECT_URI = open("./REFERENCES/redirect_uri.txt", "r").read()

custom_scope = "user-read-currently-playing"
current_playing_client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 
			client_secret   = SECRET, 
			scope           = custom_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)

def current_playing_song():

	result = current_playing_client.currently_playing()
	return_val = "currently_playing_type is an ad"

	if(str(result) == 'None'):
		return_val = "None"
	elif(result['currently_playing_type'] == 'ad'):
		return_val = "ad"
	else:
		return_val = str(result['item']['name'])

	return return_val

# ========================================================================
# PYCAW
# ========================================================================

def get_session(name = "Spotify.exe"):
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		if session.Process and (session.Process.name() == name):
			volume =  session._ctl.QueryInterface(ISimpleAudioVolume)
			return volume

def set_sesssion_mute(name = "Spotify.exe"):
	volume = get_session(name)
	volume.SetMute(1, None)

def set_sesssion_unmute(name = "Spotify.exe"):
	volume = get_session(name)
	volume.SetMute(0, None)

def is_session_mute(name = "Spotify.exe"):
	volume = get_session(name)
	return volume.GetMute()

# ========================================================================
# MAIN 
# ========================================================================

def main():
	time_delta = 5
	time_total = 0
	
	while(True):
		the_song = current_playing_song()

		if(the_song == "ad"):
			set_sesssion_mute()
		elif(is_session_mute()):
			set_sesssion_unmute()

		print(f"Time check: {time_total:5}\tSong: {the_song}")

		time.sleep(time_delta)
		time_total += time_delta

if __name__ == '__main__':
	print("\nSTART ----------------------------------------")
	main()

	print("\nEND ------------------------------------------")