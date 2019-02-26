from gtts import gTTS
import PySimpleGUI as sg
import re
while True:
    text = sg.PopupGetText('Google TTS', 'Inserire frase grz prg')
    words = text.split()
    split = words[:4]
    file = '_'.join(split)+'.mp3'
    tts = gTTS(text, lang='it')
    tts.save(file)
    sg.Popup('File salvato come '+file)
