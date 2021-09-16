import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from time import ctime
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            erza_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-uk")
        except sr.UnknownValueError:
            erza_speak('Sorry, I did not get that')
        except sr.RequestError:
            erza_speak('sorry my speach service is down')
        return voice_data

def erza_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        erza_speak('My name is Erza')
    if 'what time is it' in voice_data:
        erza_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        erza_speak('here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('whast is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        erza_speak('here is the location of ' + location)
    if 'where are you from' in voice_data:
        import ipinfo
        handler = ipinfo.getHandler(access_token='2f0b7d20b933b2')
        details = handler.getDetails()
        erza_speak("I'm from " + details.country_name)
    if 'go to sleep' in voice_data:
        erza_speak('bye')
        exit()

time.sleep(1)
erza_speak('How can I help you?')
while 1:  
    voice_data = record_audio()
    respond(voice_data)