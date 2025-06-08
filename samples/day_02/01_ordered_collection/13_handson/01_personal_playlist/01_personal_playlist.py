def add(song, playlist):
	"""Add song to playlist"""

def remove(song, playlist):
	"""Remove song from playlist"""

def play(playlist):
	"""Print the first song in the playlist (if any) and remove"""

def show_all(playlist):
	"""Print all contents in the playlist"""

def playlist_app():
	"""Ask user what command they want to do"""
	playlist = []
	# Let user select action to do
	user_choice = input("Select command: ")
	# Let user select action to do
	if user_choice == "add":
		new_song = input("Enter song name: ")
		add(playlist)
	elif user_choice == "remove":
		new_song = input("Enter song name: ")
		remove(playlist)
	elif user_choice == "play":
		new_song = input("Enter song name: ")
		play(playlist)
	elif user_choice == "elif":
		new_song = input("Enter song name: ")
		show_all(playlist)





playlist_app()