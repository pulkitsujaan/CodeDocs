from pygame import mixer 

# Starting the mixer 
mixer.init() 

# Loading the song 
mixer.music.load("Dil Ka Telephone - Dream Girl.mp3") 

# Setting the volume 
mixer.music.set_volume(0.5) 

print("\n\nPress 'pl' to play\n'p' to pause\n'r' to resume") 
print("\nPress 'e' to exit the program")
# infinite loop 
while True: 
	 
	query = input("choice:") 
	
	if query == "pl": 

		# Playing the music 
		mixer.music.play()
	if query == 'p': 

		# Pausing the music 
		mixer.music.pause()	 
	elif query == 'r': 

		# Resuming the music 
		mixer.music.unpause() 
	elif query == 'e': 

		# Stop the mixer 
		mixer.music.stop() 
		break
