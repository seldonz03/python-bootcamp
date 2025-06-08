def add(song, playlist):
    playlist.append(song)
    print(playlist)

def remove(song, playlist):

    playlist.pop(song)
    print(playlist)

def play(playlist):
	"""Print the first song in the playlist (if any) and remove"""
	print(playlist[0])



def show_all(playlist):
	"""Print all contents in the playlist"""
	print(playlist[:])


def playlist_app():
	"""Ask user what command they want to do"""
	playlist = []
	finish = False
	# Let user select action to do

	# Let user select action to do
	while not finish:
		user_choice = input("Select command: ")
		if user_choice == "add":
			new_song = input("Enter song name: ")
		elif user_choice == "remove":
			new_song = input("Enter title name: ")
			remove(new_song,playlist)
		elif user_choice == "play":
			new_song = input("Enter song name: ")
			play(playlist)
		elif user_choice == "elif":
			new_song = input("Enter song name: ")
			show_all(playlist)
		else:
			if user_choice == "exit":
				finish = True


playlist_app()

