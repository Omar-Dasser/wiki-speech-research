from gtts import gTTS 
import pyglet
import time, os
import pygame as pg
#from pydub import AudioSegment

#text = 'Hello omar , My name is RX and I am here to help'
def tts(text):
    file = gTTS(text = text, lang='en')
    filename = 'temp.mp3'

    file.save(filename)

def play_mp3(file, volume=0.8):
    freq = 22000     
    bitsize = -16    
    channels = 2     
    buffer = 2048    
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(file)
        print("Music file {} loaded!".format(file))
    except pg.error:
        print("File {} not found! ({})".format(file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        
        clock.tick(30)

#play_mp3(filename,0.8)

#music = pyglet.media.load('temp.mp3', streaming = False)

#music.play()

#time.sleep(music.duration)
#os.remove(filename)
