import time
from ultralytics import YOLO
import subprocess
import openai
import cv2
import threading
import os
from gtts import gTTS
import speech_recognition as sr
from translate import Translator
from gpiozero import Button

button = Button(2)

openai.api_key = ""

def speak(text, voice='ml', speed=150, pitch=50):
    tts = gTTS(text=text, lang='ml')
    tts.speed = speed
    tts.save('speech.mp3')
    os.system('mpg321 speech.mp3')
        
def takecommand(language='ml'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("കേൾക്കുകയാണ്...")
        try:
            audio = r.listen(source, timeout=2)
            print("തിരിച്ചറിയുന്നു...")
            query = r.recognize_google(audio, language=language)
            print(f"ഉപയോക്താവ് പറഞ്ഞത്: {query}\n")
        except sr.UnknownValueError:
            speak('ക്ഷമിക്കണം, ഞാൻ അറിയാനാകുകയില്ല. ദയവായി വീണ്ടും പരീക്ഷിക്കുക.')
            query = 'error'
        except sr.RequestError as e:
            speak(f'ക്ഷമിക്കണം, സ്പീച് ഗ്രഹണ സേവനത്തിൽ ഒരു പിശക് സംഭവിച്ചു. {e}')
            query = 'error'
    return query
    
def chat():
    query = takecommand()
    if query!='error':
        
        translator = Translator(to_lang='en', from_lang='ml')
        translated = translator.translate(query)
        
        question = (
            translated
        )
        output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"
        },
        {"role": "user", "content": question}
        ])
        response = output['choices'][0]['message']['content'].strip()
        
        translator = Translator(to_lang='ml', from_lang='en')
        translated = translator.translate(response)
        speak(translated)

while True:
    button.wait_for_press()
    chat()
