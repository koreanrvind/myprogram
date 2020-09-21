import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:" + str(e))

    return said


pyttsx3.speak("hello, how can I help you?")
print("chat with me with your requirements : "  , end='')
text =get_audio()
if (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("Control" in text) or ("control" in text)) and (("Panel" in text) or ("panel" in text)):
	pyttsx3.speak("okay, here is your control panel")
	os.system("Control")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("Task" in text) or ("task" in text)) and (("manager" in text ) or ("manager" in text )):
	pyttsx3.speak("okay, here is your task manager")
	os.system("taskmgr")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("System" in text) or ("system" in text)) and (("Configuration" in text) or ("configuration" in text) or ("config" in text)):
	pyttsx3.speak("okay, here is your system configuration") 
	os.system("msconfig")    

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("system" in text) and (("information" in text) or ("info" in text))):
	pyttsx3.speak("okay, here is your system information")
	os.system("msinfo32")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("paint" in text):
	pyttsx3.speak("okay, here is your paint")
	os.system("mspaint") 
elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("wordpad" in text):
	pyttsx3.speak("okay, here is your wordpad")
	os.system("wordpad")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("Notepad" in text) or ("notepad" in text) or ("Editor" in text) or ("editor" in text)):
	pyttsx3.speak("okay, here is your notepad")
	os.system("notepad")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("media" in text) and ("player" in text)):
	pyttsx3.speak("okay, here is your media player")
	os.system("wmplayer")    

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("edge" in text):
	pyttsx3.speak("okay, here is your microsoft edge")
	os.system("msedge")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("firefox" in text):
	pyttsx3.speak("okay, here is your firefox")
	os.system("firefox")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("Chrome" in text)or ("chrome" in text)):
	pyttsx3.speak("okay, here is your chrome")
	os.system("chrome")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("word" in text):
	pyttsx3.speak("okay, here is your word")
	os.system("WINWORD")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("powerpoint" in text) or ("powerpnt" in text)):
	pyttsx3.speak("okay, here is your powerpoint")
	os.system("POWERPNT")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("powerpoint" in text) or ("powerpnt" in text)):
	pyttsx3.speak("okay, here is your powerpoint")
	os.system("POWERPNT")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("msproject" in text):
	pyttsx3.speak("okay, here is your msproject")
	os.system("WINPROJ")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("zoom" in text) or ("meeting" in text)):
	pyttsx3.speak("okay, here is your zoom")
	os.system("Zoom")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("onenote" in text):
	pyttsx3.speak("okay, here is your onenote")
	os.system("ONENOTE")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("msaccess" in text):
	pyttsx3.speak("okay, here is your msaccess")
	os.system("MSACCESS")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("outlook" in text):
	pyttsx3.speak("okay, here is your outlook")
	os.system("OUTLOOK")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and (("skype" in text) or (("vedio"in text) and ("calling" in text))):
	pyttsx3.speak("okay, here is your skype")
	os.system("Skype")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("publisher" in text):
	pyttsx3.speak("okay, here is your publisher")
	os.system("MSPUB")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ("dropbox" in text):
	pyttsx3.speak("okay, here is your dropbox")
	os.system("Dropbox")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ((("Virtual" in text) or ("virtual" in text)) and (("box" in text) or ("box" in text))):
	pyttsx3.speak("okay, here is your virtual box")
	os.system("VirtualBox")

elif (("open" in text) or ("Open" in text) or ("Run" in text) or ("run" in text) or ("Launch" in text) or ("launch" in text) or ("Execute" in text) or ("execute" in text)) and ((("Android" in text) or ("android" in text)) and (("Studio" in text) or ("studio" in text))):
	pyttsx3.speak("okay, here is your android studio")
	os.system("studio64")

else:
	pyttsx3.speak("something is missing")
	print("doesn't support")
