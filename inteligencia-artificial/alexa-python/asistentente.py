import speech_recognition as sr 
import pyttsx3 as tts
import pywhatkit
import os
import datetime as time

usuario = 'Luis'
name='eva'
listener = sr.Recognizer()

engine = tts.init()

voiceList = engine.getProperty('voices')
engine.setProperty('voice', voiceList[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec 

def run():
    rec = listen()

    #SALUDOS 
    if 'buenos' in rec:
        print(rec +usuario)
        talk(rec + usuario)
    if 'buenas' in rec:
        if 'tardes' in rec:
            print(rec +usuario)
            talk(rec + usuario)
        else:
            print(rec+usuario)
            talk(rec+ usuario)
    
    #COMANDOS
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("reproduciendo: "+ music)
        talk("reproduciendo: "+ music)
        pywhatkit.playonyt(music)

    if 'hora' in rec:
        hora = time.datetime.now().strftime('%I:%M %p')
        
        print("Son las: " + hora)
        talk("Son las: " + hora)

    #if 'abre' in rec:
    #     program='C:\Program Files\Google\Chrome\Application\chrome.exe'
    #     os.system(program)

run()