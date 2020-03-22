import pyautogui
import time
import json
string1="hey"
try:
  with open("../data/all_user_data.json", 'r') as ma:
      string1 =json.load(ma)
      string1=string1['multi_apps']
except:
	string1=""


def openApp(p1):
	if(p1!=""):
		l=p1.split(',')
		print(l)
		for i in l:
			pyautogui.hotkey('winleft')
			pyautogui.write('{}\n'.format(i))
			time.sleep(3)

openApp(string1)
