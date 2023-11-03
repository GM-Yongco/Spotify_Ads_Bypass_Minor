# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

import time

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# ========================================================================
# SPOTIFY API 
# ========================================================================

ID = open("./REFERENCES/client_ID.txt", "r").read()
SECRET = open("./REFERENCES/client_secret.txt", "r").read()
REDIRECT_URI = open("./REFERENCES/redirect_uri.txt", "r").read()

default_scope = "user-read-currently-playing"
default_client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 
			client_secret   = SECRET, 
			scope           = default_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)

def redefine_client():
	new_client = spotipy.Spotify(
	auth_manager = SpotifyOAuth(
			client_id       = ID, 
			client_secret   = SECRET, 
			scope           = default_scope, 
			redirect_uri    = REDIRECT_URI
		)
	)
	return new_client

def current_playing_song(client = default_client)->str:

	result = client.currently_playing()
	return_val = "ad"

	if(str(result) == 'None'):
		return_val = "None"
	elif(result['currently_playing_type'] != "track"):
		return_val = result['currently_playing_type']

		# recently learned that 'currently playing type can be'
		# track, episode, or ad andmaybe theres more kinds
		# ¯\_(ツ)_/¯ 

	else:
		return_val = str(result['item']['name'])

	
	return return_val

# ========================================================================
# PYCAW
# ========================================================================

# add decorator for every function group for excpetions

def get_session(name = "Spotify.exe"):
	# if return for loop is not desirable
	# chnage in the future if possible

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
# TIME 
# ========================================================================

def time_current()->str:
	now = time.strftime("%y/%m/%d %H:%M", time.localtime())
	return f"\n{now}"

# ========================================================================
# TEXT LOG
# ========================================================================

def log(x:str, path = "./log.txt"):
	try:
		file = open(path, "a")
		file.write(f"\n{x}")
		file.close
	except Exception as error:
		print("An exception occurred at function 'log' :", error)

	print(x)

# ========================================================================
# MAIN 
# ========================================================================

def main_loop():
	time_delta = 5
	time_total = 0
	
	spotify_client = redefine_client()

	while(True):
		the_song = current_playing_song(spotify_client)
		log(f"Time check: {time_total:5}\tSong: {the_song}")

		if(the_song == "ad"):
			set_sesssion_mute()
		elif(is_session_mute()):
			set_sesssion_unmute()

		time.sleep(time_delta)
		time_total += time_delta

def main():
	log(time_current())

	i = 1
	while(i<5):
		# we basically just wait for the timeout error
		try:
			main_loop()
		except Exception as error:
			log(time_current())
			log(f"exeption number {i}")
			log(f"An exception occurred at function 'main' :{error}")
		i += 1

if __name__ == '__main__':
	log("\nSTART ----------------------------------------")
	main()

	log("\nEND ------------------------------------------")