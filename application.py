import pyautogui as p
import speech_recognition as sr
import time
import subprocess
import pyttsx3
import keyboard


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
        engine.setProperty("rate", 140)
        engine.say(text)
        print(text)
        global GUI_data
        GUI_data=text
        engine.runAndWait()

system_application=['Calculator','Calendar','Camera','Clock','Cortana','Dolby Audio','file explorer','Excel','Family','Google Chrome','Chrome',"Edge",'Game bar','Feedback Hub','Mail','Maps','Media Player','Microsoft Office','Microsoft Clipchamp','Microsoft Edge','Microsoft Store','Microsoft To Do','News','Notepad','OneDrive','OneNote','Outlook','Paint','Phone Link','Photos','PowerPoint','PyCharm','Python','Quick Assist','Settings','Snipping Tool','Solitaire & Casual Games','Sound Recorder','Sticky Notes','Terminal','Tips','Visual Studio Code','Weather','WhatsApp','Windows Back up','Windows Security','Windows Tools','WinRAR','Word','XAMPP','Xbox','Zoom','vs code']

def applicaton_open(query):
    for app in range(0,len(system_application)):
        if system_application[app].lower() in query.lower():
            say(f"Opening {system_application[app]} sir...")
            p.press('win')
            time.sleep(2)
            p.write(system_application[app])
            time.sleep(3)
            p.press('enter')
    
    say('Boss! Do you want keyboard access to type queries through voice?')
    disistion=take_command()
    disistion=disistion.lower()
    if('yes' in disistion) or ('keyboard' in disistion):
        keyboard.Whatsapp_key()

    # if system_application not in query:
    #     say("This application is not available in your system...")


system_application_close={'Calculator':'CalculatorApp.exe','Calendar':'msedgewebview2.exe','Camera':'WindowsCamera.exe','Clock':'Time.exe','Cortana':'Cortana.exe','Dolby Audio':'DAXUIDolbyAudio.exe','file explorer':'explorer.exe','Excel':'EXCEL.exe','Edgs':'','Family':'FamilyHub.exe','Google Chrome':'chrome.exe','Chrome':'chrome.exe',"Edge":'msedge.exe','Game bar':'GameBar.exe','Feedback Hub':'PilotshubApp.exe','Mail':'msedgewebview2.exe','Map':'Maps.exe','Media Player':'Microsoft.Media.Player.exe','Microsoft Office':'EXCEL.exe','Microsoft Clipchamp':'Clipchamp.exe','Microsoft Edge':'msedge.exe','Microsoft Store':'WinStore.App.exe','Microsoft To Do':'Todo.exe','News':'msedgewebview2.exe','Notepad':'Notepad.exe','OneDrive':'explorer.exe','OneNote':'ONENOTE.exe','Outlook':'olk.exe','Paint':'mspaint.exe','Phone Link':'PhoneExperienceHost.exe','Photos':'PhotosApp.exe','PowerPoint':'POWERPNT.EXE','PyCharm':'pycharm64.exe','Python':'WindowsTerminal.exe','Quick Assist':'QuickAssist.exe','Settings':'SystemSettings.exe','Snipping Tool':'SnippingTool.exe','Solitaire & Casual Games':'Solitaire.exe','Sound Recorder':'spoolsv.exe','Sticky Notes':'StickyNotesStub.exe','Terminal':'WindowsTerminal.exe','cmd':'WindowsTerminal.exe','Tips':'WhatsNew.Store.exe','Visual Studio Code':'Code.exe','vs Code':'Code.exe','Weather':'Microsoft.Msn.Weather.exe','WhatsApp':'WhatsApp.exe','Windows Back up':'WindowsBackupClient.exe','Windows Security':'SecHealthUI.exe','Windows Tools':'explorer.exe','WinRAR':'WinRAR.exe','Word':'WINWORD.EXE','XAMPP':'xampp-control.exe','Xbox':'XboxGameBarSpotify.exe','Zoom':'Zoom.exe'}



def close_application(query):
    try:
        for name,value in system_application_close.items():
            if name.lower() in query.lower():
                subprocess.run(['taskkill', '/F', '/IM', value], check=True)
                say(f"{name} has been closed successfully.")
    except subprocess.CalledProcessError:
        say(f"Failed to close {name}.")






            

