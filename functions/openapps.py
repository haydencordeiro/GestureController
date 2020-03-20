import pyautogui
import time
import json
string1="hey"
try:
  with open("data/multi_apps.json", 'r') as ma:
      string1 =json.load(ma)
except:
	string1=""


def openApp(p1):
	if(p1!=""):
		l=p1.split(',')
		print(l)
		for i in l:
			pyautogui.hotkey('winleft','a')
			pyautogui.write('{}\n'.format(i))
			time.sleep(3)

openApp(string1)
