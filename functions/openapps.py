import pyautogui
import time
import json
import psutil
string1="hey"


try:
  with open("../data/all_user_data.json", 'r') as ma:
      string1 =json.load(ma)
      string1=string1['multi_apps']
      print(string1)
except:
	string1=""


def openApp(p1):
	if(p1!=""):
		l=p1.split(',')
		print(l)
		for i in l:
			a=True
			pyautogui.hotkey('winleft','a')
			pyautogui.write('{}\n'.format(i))
			time.sleep(5)		
					
				
openApp(string1)
