import os
import pyttsx3


while True:
	print("chat with me with your requirements:" , end='')
	a=input()

	if (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("control" in a) and ("panel" in a)):
	  os.system("Control")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("task" in a) and ("manager")):
	  os.system("taskmgr")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("system" in a) and (("configuration" in a) or ("config" in a))):
	  os.system("msconfig")
	
	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("system" in a) and (("information" in a) or ("info" in a))):
	  os.system("msinfo32")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("paint" in a):
	  os.system("mspaint")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("wordpad" in a):
	  os.system("wordpad")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and( ("notepad" in a) or ("editor" in a)):
	  os.system("notepad")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("media" in a) and ("player" in a)):
	  os.system("wmplayer")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("edge" in a):
	  os.system("msedge")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("firefox" in a):
	  os.system("firefox")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("chrome" in a):
	  os.system("chrome")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("Notepad++" in a):
	  os.system("Notepad++")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("word" in a):
	  os.system("WINWORD")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("powerpoint" in a) or ("powerpnt" in a)):
	  os.system("POWERPNT")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("excel" in a):
	  os.system("EXCEL")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("msproject" in a):
	  os.system("WINPROJ")
	
	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("zoom" in a) or ("meeting" in a)):
	  os.system("Zoom")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("onenote" in a):
	  os.system("ONENOTE")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("msaccess" in a):
	  os.system("MSACCESS")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("outlook" in a):
	  os.system("OUTLOOK")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("skype" in a) or (("vedio"in a) and ("calling" in a))):
	  os.system("Skype")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("publisher" in a):
	  os.system("MSPUB")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and ("dropbox" in a):
	  os.system("Dropbox")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("virtual" in a) and ("box" in a)):
	  os.system("VirtualBox")

	elif (("run" in a) or ("lunch" in a) or ("execute" in a)) and (("android" in a) and ("studio" in a)):
	  os.system("studio64")

	elif  ("exit" in a)  or ("quit" in a):
	  pyttsx3.speak("thank you")
	  break

	else:
	  pyttsx3.speak("something is missing")
	  print("doesn't support")