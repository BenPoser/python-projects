import pyaudio
import wave
import speech_recognition as sr
from commands import Commander
from gtts import gTTS
import pyglet
import time
import os

'''
def tts(text, lang):
    file = gTTS(text=text, lang="en")
    filename = '/tmp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)
'''

running = True

# Defining chunks, opening file as binary, instantiate pyaudio class
def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

# Creating data stream, opening file with arguments - format/channels/framerate
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

# Reading it continuously then terminating
    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()


# Getting the computer to hear us including audio cues
def initSpeech():
    print("Listening...")

    play_audio("./audio/start.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("./audio/end.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Does not compute.")

    print("Your command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye", "good-by"]:
        global running
        running = False

    cmd.discover(command)

while running == True:
    initSpeech()
