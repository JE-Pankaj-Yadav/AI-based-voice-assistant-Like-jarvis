import speech_recognition as sr
from requests import get
from PhoneNumer import Phonenumber_location_tracker
from bs4 import BeautifulSoup
import pywhatkit as kit
import pyautogui
import instaloader
import speedtest
import smtplib
import psutil
import pyttsx3
import PyPDF2
import Display
import subprocess
import webbrowser
import random
import wikipedia
import pyjokes
import openai
from apikey import api_data
import datetime
import time
import sys
import os
from subprocess import call
import application

openai.api_key = api_data
import keyboard
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from VA_GUI import Ui_MainWindow

completion = openai.Completion()
global weather, netspeed, battery, IP_Address
weather = Display.temperature()
if "error" in weather.lower() or "could not" in weather.lower():
    weather = "Weather information currently unavailable"
netspeed = Display.InternetSpeed()
battery = Display.Battery_condition()
IP_Address = Display.IP()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.taskExecution()

    # commands controller
    def taskExecution(self):
        self.wish()
        self.condition()
        self.InternetSpeed()
        self.say("Hello boss I am your assistant. please tell me how can i help you")
        while True:
            self.query = self.take_command().lower()
            commonds = self.query
            commond = commonds.split()

            if (
                ("your name" in self.query)
                or ("my name" in self.query)
                or ("college name" in self.query)
                or ("what can you do" in self.query)
                or ("your age" in self.query)
                or ("date" in self.query)
                or ("joke" in self.query)
                or ("are you single" in self.query)
                or ("are you there" in self.query)
                or ("tell me something" in self.query)
                or ("thank you" in self.query)
                or ("in your free time" in self.query)
                or ("i love u" in self.query)
                or ("can you hear me" in self.query)
                or ("do you ever get tired" in self.query)
            ):
                self.Fun(self.query)

            elif (
                (("hi" in self.query) and len(self.query) == 2)
                or (
                    (("hai" in self.query) or ("hey" in self.query))
                    and len(self.query) == 3
                )
                or (("hello" in self.query) and len(self.query) == 5)
            ):
                self.comum(self.query)

            elif ("today" in self.query) or ("day" in self.query):
                day = self.Cal_day()
                self.say("Today is " + day)

            # Wikipedia search...
            elif "wikipedia" in self.query:
                self.W_S(self.query)

            elif "time" in self.query:
                self.Clock_time(self.query)

            elif ("flipkart" in self.query) or ("amazon" in self.query):
                self.shopping(self.query)

            elif (
                ("where i am" in self.query)
                or ("where we are" in self.query)
                or ("locaiton" in self.query)
            ):
                self.locaiton()

            elif ("instagram profile" in self.query) or (
                "profile on instagram" in self.query
            ):
                self.Instagram_Pro()

            elif (
                ("take screenshot" in self.query)
                or ("screenshot" in self.query)
                or ("take a screenshot" in self.query)
            ):
                self.scshot()

            elif ("read pdf" in self.query) or ("pdf" in self.query):
                self.pdf_reader()

            elif ("volume up" in self.query) or ("increase volume" in self.query):
                pyautogui.press("volumeup")
                self.say("volume increased")

            elif ("volume down" in self.query) or ("decrease volume" in self.query):
                pyautogui.press("volumedown")
                self.say("volume decreased")

            elif ("volume mute" in self.query) or ("mute the sound" in self.query):
                pyautogui.press("volumemute")
                self.say("volume muted")

            elif (
                ("create a new contact" in self.query)
                or ("add a new contact" in self.query)
                or ("add new contact" in self.query)
            ):
                self.AddContact()

            elif ("display all the contacts" in self.query) or (
                "display all the contact" in self.query
            ):
                self.Display()

            elif (
                ("track" in self.query)
                or ("track a mobile number" in self.query)
                or ("track a mobile phone" in self.query)
            ):
                self.say("Boss please enter the mobile number with country code")
                location, servise_prover, lat, lng = Phonenumber_location_tracker()
                self.say(
                    f"Boss the mobile number is from {location} and the service provider for the mobile number is {servise_prover}"
                )
                self.say(
                    f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}"
                )
                self.say("Boss location of the mobile number is saved in Maps")
                # try:
                # except:
                #     self.say("Boss an unexpected error occured couldn't track the mobile number")

            elif "music" in self.query:
                try:
                    song_dir = "C:/Users/py035/OneDrive/Music"
                    songs = os.listdir(song_dir)
                    print(songs)
                    x = len(songs)
                    y = random.randint(0, x)
                    os.startfile(os.path.join(song_dir, songs[y]))
                except:
                    self.say("Boss an unexpected error occured")

            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                self.say(f"your IP address is {ip}")

            elif ("send a message" in self.query) or ("send a whatsapp" in self.query):
                self.whatsapp()

            elif "send email" in self.query:
                self.verifyMail()

            elif (
                ("temperature" in self.query)
                or ("weather" in self.query)
                or ("check weather" in self.query)
            ):
                self.temperature()

            elif "internet speed" in self.query:
                self.InternetSpeed()

            elif ("you can sleep" in self.query) or ("sleep now" in self.query):
                self.say("Okay boss, I am going to sleep you can call me anytime.")
                break

            elif ("wake up" in self.query) or ("get up" in self.query):
                self.say("boss, I am not sleeping, I am in online, what can I do for u")

            elif ("good bye" in self.query) or ("get lost" in self.query):
                self.say("Thanks for using me boss, have a good day")
                break

            elif ("system condition" in self.query) or (
                "condition of the system" in self.query
            ):
                self.say("checking the system condition")
                self.condition()

            elif (
                ("tell me news" in self.query)
                or ("the news" in self.query)
                or ("todays news" in self.query)
            ):
                self.say("Please wait boss, featching the latest news")
                self.news()

            elif ("shutdown the system" in self.query) or (
                "down the system" in self.query
            ):
                self.say("Boss shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")

            elif (
                ("password" in self.query)
                or ("Wi-Fi password" in self.query)
                or ("crack Wi-Fi password" in self.query)
                or ("wifi" in self.query)
                or ("Wi-Fi" in self.query)
                or ("internet password" in self.query)
            ):
                self.get_wifi_passwords()

            elif "restart the system" in self.query:
                self.say("Boss restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                self.say("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

            elif ("slides" in self.query) or ("canva" in self.query):
                self.edit(self.query)

            elif commond.count("bye") > 0 or commond.count("ok") > 0:
                self.say("Thanks for using me boss, have a good day")
                break

            elif (
                ("youtube" in self.query)
                or ("wikipedia" in self.query)
                or ("google" in self.query)
                or ("chrome" in self.query)
            ):
                self.sitess(self.query)

            elif ("open" in self.query) or ("opening" in self.query):
                application.applicaton_open(self.query)

            elif ("close" in self.query) or ("closing" in self.query):
                application.close_application(self.query)

            elif "remember that" in self.query:
                self.say("Boss! What should I remember")
                data = self.take_command()
                self.say("You said me to remember that" + data)
                remember = open("remember_data.txt", "w")
                remember.write(data)
                remember.close()

            elif "do you remember anything" in self.query:
                remember = open("remember_data.txt", "r")
                self.say("You told me to remember that" + remember.read())

            # openai questions!
            elif self.query != "pass":
                prompt = self.query
                response = completion.create(
                    prompt=prompt, engine="gpt-3.5-turbo-instruct", max_tokens=80
                )
                answer = response.choices[0].text.strip()
                self.say(answer)

    # All functions.......

    # Communication commands
    def comum(self, command):
        print(command)
        if (
            ("hi" in command)
            or ("hai" in command)
            or ("hey" in command)
            or ("hello" in command)
            or ("hay" in command)
        ):
            self.say("Hello boss what can I help for u")
        else:
            self.No_result_found()

    # wikipedia Search commands
    def W_S(self, command):
        try:
            target1 = command.replace("search for", "")
            target1 = target1.replace("in wikipedia", "")
            target1 = target1.replace("wikipedia", "")
            print("searching....")
            info = wikipedia.summary(target1, 2)
            self.say("According to wikipedia " + info)
        except:
            self.No_result_found()

    # clock commands
    def Clock_time(self, command):
        time = datetime.datetime.now().strftime("%I:%M %p")
        self.say("Current time is " + time)

    # no result found
    def No_result_found(self):
        self.say("Boss I couldn't understand, could you please say it again.")

    # Photo shops
    def edit(self, command):
        print(command)
        if "slides" in command:
            self.say("opening your google slides")
            webbrowser.open("https://docs.google.com/presentation/")
        elif "canva" in command:
            self.say("opening your canva")
            webbrowser.open("https://www.canva.com/")
        else:
            self.No_result_found()

    # Shopping links
    def shopping(self, command):
        if "flipkart" in command:
            self.say("Opening flipkart online shopping website")
            webbrowser.open("https://www.flipkart.com/")
        elif "amazon" in command:
            self.say("Opening amazon online shopping website")
            webbrowser.open("https://www.amazon.in/")
        else:
            self.No_result_found()

    # location
    # important link: https://get.geojs.io/v1/ip/geo/47.9.92.134.json
    def locaiton(self):
        self.say("Wait boss, let me check")
        try:
            IP_Address = get("https://api.ipify.org").text
            url = "https://get.geojs.io/v1/ip/geo/" + IP_Address + ".json"
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data["city"]
            state = geo_data["region"]
            country = geo_data["country"]
            tZ = geo_data["timezone"]
            longitude = geo_data["longitude"]
            latidute = geo_data["latitude"]
            org = geo_data["organization_name"]
            self.say(
                f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country"
            )
            self.say(
                f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}'s network "
            )
        except Exception as e:
            self.say(
                "Sorry boss, due to network issue i am not able to find where we are."
            )
            pass

    # Instagram profile
    def Instagram_Pro(self):
        self.say("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        self.say("Boss would you like to download the profile picture of this account.")
        cond = self.take_command()
        if ("download" in cond) or ("yes" in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name, profile_pic_only=True)
            self.say("I am done boss, profile picture is saved in your main folder. ")
        else:
            pass

    # ScreenShot
    def scshot(self):
        self.say("Boss, please tell me the name for this screenshot file")
        name = self.take_command()
        self.say("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"E://DIPLOMA FINAL YEAR PROJECT/screenshot/{name}.png")
        self.say("I am done boss, the screenshot is saved in main folder.")

    # Fun commands to interact with jarvis
    def Fun(self, command):
        print(command)
        if "your name" in command:
            self.say("My name is assistant")
        elif "my name" in command:
            self.say("your name is Pankaj")
        elif "college name" in command:
            self.say(
                "you are studing in Vikas Instituteof Engineering and Technology, in diploma in Computer Science"
            )
        elif "what can you do" in command:
            self.say(
                "I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes"
            )
        elif "your age" in command:
            self.say("I am very young that u")
        elif "date" in command:
            self.say(
                "Sorry not intreseted, I am having headache, we will catch up some other time"
            )
        elif "are you single" in command:
            self.say("No, I am in a relationship with wifi")
        elif "joke" in command:
            self.say(pyjokes.get_joke())
        elif "are you there" in command:
            self.say("Yes boss I am here")
        elif "tell me something" in command:
            self.say(
                "boss, I don't have much to say, you only tell me someting i will give you the company"
            )
        elif "thank you" in command:
            self.say("boss, I am here to help you..., your welcome")
        elif "in your free time" in command:
            self.say("boss, I will be listening to all your words")
        elif "i love u" in command:
            self.say("I love you too boss")
        elif "can you hear me" in command:
            self.say("Yes Boss, I can hear you")
        elif "do you ever get tired" in command:
            self.say("It would be impossible to tire of our conversation")
        else:
            self.No_result_found()

    # PDF reader
    def pdf_reader(self):
        self.say("Boss tall the name of the pdf which you want to read")
        # n = input("Enter the pdf name: ")
        n = self.take_command()
        n = f".\Documents\{n}.pdf"
        with open(n, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Get the number of pages in the PDF
            num_pages = len(pdf_reader.pages)

            # Iterate through all pages and extract text
            text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        self.say(text)

    # Add contacts
    def AddContact(self):
        self.say(f"Boss, Enter the contact details")
        name = input("Enter the name :").lower()
        number = input("Enter the number :")
        NumberFormat = f'"{name}":"+91{number}"'
        ContFile = open("Contacts.txt", "a")
        ContFile.write(f"{NumberFormat}\n")
        ContFile.close()
        self.say(f"Boss, Contact Saved Successfully")

    # Search Contact
    def SearchCont(self, name):
        with open("Contacts.txt", "r") as ContactsFile:
            for line in ContactsFile:
                if name in line:
                    print("Name Match Found")
                    s = line.split('"')
                    return s[1], s[3], True
        return 0, 0, False

    # Display all contacts
    def Display(self):
        ContactsFile = open("Contacts.txt", "r")
        count = 0
        for line in ContactsFile:
            count += 1
        ContactsFile.close()
        ContactsFile = open("Contacts.txt", "r")
        self.say(f"Boss displaying the {count} contacts stored in our data base")
        for line in ContactsFile:
            s = line.split('"')
            print("Name: " + s[1])
            print("Number: " + s[3])
        ContactsFile.close()

    # Wish
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        print(t)
        if (hour >= 0) and (hour <= 12) and ("AM" in t):
            self.say(f"Good morning boss, its {day} and the time is {t}")
        elif (hour >= 12) and (hour <= 16) and ("PM" in t):
            self.say(f"good afternoon boss, its {day} and the time is {t}")
        else:
            self.say(f"good evening boss, its {day} and the time is {t}")

    # calender day
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday",
        }
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            global Day
            Day = day_of_the_week.upper()
        return day_of_the_week

    # Whatsapp
    def whatsapp(self):
        import pyautogui as p

        try:
            p.press("win")
            time.sleep(2)
            p.write("Whatsapp")
            time.sleep(2)
            p.press("enter")
            self.say("Boss! Who do you want to send the message to?")
            p.write(self.take_command())
            p.hotkey("ctrl", "1")
            time.sleep(5)
            self.say("Boss! You say whatever message you want to send.")
            p.write(self.take_command())
            time.sleep(2)
            p.press("enter")
        except:
            self.say("Error occured, please try again")

    # Whatsapp
    # def whatsapp(self,command):
    #     try:
    #         command = command.replace('send a message to','')
    #         command = command.strip()
    #         name,numberID,F = self.SearchCont(command)
    #         if F:
    #             print(numberID)
    #             self.say(f'Boss, what message do you want to send to {name}')
    #             message = self.take_command()
    #             hour = int(datetime.datetime.now().hour)
    #             min = int(datetime.datetime.now().minute)
    #             print(hour,min)
    #             if "group" in command:
    #                 kit.sendwhatmsg_to_group(numberID,message,int(hour),int(min)+1)
    #             else:
    #                 kit.sendwhatmsg(numberID,message,int(hour),int(min)+1)
    #             self.say("Boss message have been sent")
    #         if F==False:
    #             self.say(f'Boss, the name not found in our data base, shall I add the contact')
    #             AddOrNot = self.take_command()
    #             print(AddOrNot)
    #             if ("yes" in AddOrNot) or ("add" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
    #                 self.AddContact()
    #             elif("no" in AddOrNot):
    #                 self.say('Ok Boss')
    #     except:
    #         print("Error occured, please try again")

    # Mail verification
    def verifyMail(self):
        try:
            self.say("what should I say?")
            content = self.take_command()
            self.say("To whom do u want to send the email?")
            to = self.take_command()
            self.SendEmail(to, content)
            self.say("Email has been sent to " + str(to))
        except Exception as e:
            print(e)
            self.say("Sorry sir I am not not able to send this email")

    # Email Sender
    def SendEmail(self, to, content):
        print(content)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("YOUR_MAIL_ID", "PASWORD")
        server.sendmail("YOUR_MAIL_ID", to, content)
        server.close()

    # Weather forecast
    def temperature(self):
        IP_Address = get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/" + IP_Address + ".json"
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data["city"]
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        self.say(f"Current {search} is {temp}")

    # Internet speed
    def InternetSpeed(self):
        self.say("Wait a few seconds boss, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl / (1000000)  # converting bytes to megabytes
        up = st.upload()
        up = up / (1000000)
        self.say(
            f"Boss, we have {round(dl,2)} MB/s second downloading speed and {round(up,2)} MB/s uploading speed"
        )
        if dl > 6 and up > 5:
            self.say(
                "Boss! Your internet connection is good, your work can be done easily."
            )
        else:
            self.say(
                "Boss! Your internet connection is not good, your problem is addiction."
            )

    # System condition
    def condition(self):
        usage = str(psutil.cpu_percent())
        self.say("CPU is at" + usage + " percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        self.say(f"Boss our system have {percentage} percentage Battery")
        if percentage >= 75:
            self.say(f"Boss we could have enough charging to continue our work")
        elif percentage >= 40 and percentage <= 75:
            self.say(
                f"Boss we should connect out system to charging point to charge our battery"
            )
        elif percentage >= 15 and percentage <= 30:
            self.say(
                f"Boss we don't have enough power to work, please connect to charging"
            )
        else:
            self.say(
                f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon"
            )

    # News
    def news(self):
        MAIN_URL_ = "https://newsapi.org/v2/top-headlines?country=in&apiKey=788adadf046a4edca528fe47b28b8a6d"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings = []
        seq = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "tenth",
        ]  # If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar["title"])
        for i in range(len(seq)):
            self.say(f"Todays {seq[i]} news is: {headings[i]}")
        self.say("Boss I am done, I have read most of the latest news")

    # get_wifi_passwords
    def get_wifi_passwords(self):
        self.say("Wait a few seconds boss")
        wifi_data = []
        data = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )
        profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]
        for profile in profiles:
            try:
                results = (
                    subprocess.check_output(
                        ["netsh", "wlan", "show", "profile", profile, "key=clear"]
                    )
                    .decode("utf-8")
                    .split("\n")
                )
                password = [
                    b.split(":")[1].strip() for b in results if "Key Content" in b
                ][0]
                wifi_data.append((profile, password))
            except (subprocess.CalledProcessError, IndexError):
                wifi_data.append((profile, ""))

        for name, password in wifi_data:
            self.say(f"{name:<30}| {password}")

    # site
    def sitess(self, command):
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["chrome", "https://www.google.com"],
        ]
        for site in sites:
            if site[0] in self.query:
                self.say(f"Opening {site[0]} sir...")
                webbrowser.get("chrome").open_new_tab(site[1])
        self.say("Boss! Do you want keyboard access to type queries through voice?")
        type = self.take_command()
        if (
            ("yes" in type)
            or ("keyboard" in type)
            or ("access keyboard" in type)
            or ("keyboard access" in type)
        ):
            keyboard.write()
        else:
            self.No_result_found()

    # function that will take the commands  to convert voice into text
    def take_command(self):
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
            return "pass"
        return query

    def say(self, text):
        engine = pyttsx3.init()
        Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        # Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty("voice", Id)
        engine.setProperty("rate", 120)
        engine.say(text)
        print(text)
        global GUI_data
        GUI_data = text
        engine.runAndWait()


sartExecution = MainThread()


class Main(QMainWindow):
    cpath = ""

    def __init__(self, paths):
        self.cpath = paths
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("./images\iran man.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(".\images\INTIATING SYSTEM.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        sartExecution.start()

    def showTime(self):
        current_date = QDate.currentDate()
        label_time = datetime.datetime.now().strftime("%I:%M %p")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(GUI_data)
        self.ui.textBrowser_2.setText(netspeed)
        self.ui.textBrowser_3.setText(label_date)
        self.ui.textBrowser_4.setText(label_time)
        self.ui.textBrowser_5.setText(Day)
        self.ui.textBrowser_6.setText(weather)
        self.ui.textBrowser_7.setText(IP_Address)
        self.ui.textBrowser_9.setText(f"Battery \n {battery}%")


current_path = os.getcwd()
app = QApplication(sys.argv)
jarvis = Main(paths=current_path)
jarvis.show()
exit(app.exec_())
