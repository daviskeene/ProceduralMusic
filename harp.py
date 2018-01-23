# Called the harp because it generates the music to play.
# Each note will be a specific instance of a wave file.
# Markovify is used to generate a markov chain that, when trained, will allow for the creation of new music.

import markovify
from pygame import mixer
import time
import random

with open("/home/davis/ProceduralMusic/notes/corpus.txt") as file:
    text = file.read()

basic_model = markovify.Text(text)

notes = basic_model.make_sentence()

mixer.init()

for i in notes:
    if i != " " and i != "#":
        print(i)
        string = "notes/"+i+".wav"
        sound = mixer.Sound(string)
        sound.play()
        time.sleep(random.random())