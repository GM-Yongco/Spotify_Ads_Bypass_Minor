# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume

# ========================================================================
# MAIN 
# ========================================================================

def show_all_device_names():
	devices = AudioUtilities.GetSpeakers()
	print(devices)

	# for i in range(devices.GetCount()):
	# 	dev = devices.Item(i)
	# 	print(dev.GetDisplayName())

def get_session(name = "Spotify.exe"):
	# if return for loop is not desirable
	# chnage in the future if possible

	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		if session.Process and (session.Process.name() == name):
			volume =  session._ctl.QueryInterface(ISimpleAudioVolume)
			return volume

def is_session_mute(name = "Spotify.exe"):
	volume = get_session(name)
	return volume.GetMute()

def main():
	is_session_mute()

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")

# if another device plays the audio
#  the fix is just to make that device your default audio player