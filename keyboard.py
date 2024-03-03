import pyautogui as p
import speech_recognition as sr
import datetime
import pyttsx3
import time


def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening ..... ")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 8)
        try:
            print("Recogizing .... ")
            query = r.recognize_google(audio, language="en-in")
            print(f"Pankaj Said: {query} \n")
        except:
            print("Say again...")
            return 'pass'
        return query

def say(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    # Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", Id)
    engine.setProperty("rate", 120)
    engine.say(text)
    print(text)
    engine.runAndWait()
        

def write():
    say('Boss! please ask your question?')
    p.write(take_command())
    time.sleep(2)
    p.press('enter')

def Whatsapp_key():
    say('Boss! Who do you want to send the message to?')
    p.write(take_command())
    p.hotkey('ctrl','1')
    time.sleep(5)
    say("Boss! You say whatever message you want to send.")
    p.write(take_command())
    time.sleep(2)
    p.press('enter')



