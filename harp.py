# Called the harp because it generates the music to play.
# Each note will be a specific instance of a wave file.
# Markovify is used to generate a markov chain that, when trained, will allow for the creation of new music.
import markovify
from pygame import mixer
import time
import random
with open("notes/corpus.txt") as file: # Reads the corups, aka the training data as a file and converts to plain text
    text = file.read()
basic_model = markovify.Text(text) # Markov chain model creation
notes = basic_model.make_sentence() # Generates a string of notes based on chain
mixer.init() # Start the pygame mixer, a property of the pygame library which allows for sounds to play
# For each note in the string, play the corresponding sound
for i in notes:
    if i != " " and i != "#": # Checks if the note is flat, or if there is no note
        if i!=".": # Checks if there's a period
            print(i) # Print the note
            sound = mixer.Sound("notes/"+i+".wav") # Set the sound equal to the sound Object belonging to the mixer lib
            sound.play() # Play the sound!
            time.sleep(random.random()+.2) # Wait a random amount of time in between to play the note, add +.2 second to avoid note overlap

# Obviously this is very basic, but with very little lines of code the computer was able to generate its own "music" from samples of real music!
# With a huge sample size then this will most likely be much better at generating notes, but the hard part comes when we have to decide how long to wait between notes.
# Melodies is a step up from this, with two players at the same time, but again this is a basic implimentation of something that took a long time to work out in Javascript.