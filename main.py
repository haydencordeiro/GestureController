import random
import os
import json
import serial
# from serial import Serial 
import time
import pyautogui
import psutil




ug=[]
try:
    ser = serial.Serial('/dev/ttyACM1', 9600)
except:
    ser = serial.Serial('/dev/ttyACM0', 9600)

#ag=['moodle','snap_windows','maximize','change_tab','open_apps','screenshot','open_apps_win']


def checkIfProcessRunning(processName):
# Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def Load():
	global ug
	try:
	  with open("data/ug.json", 'r') as f:
	      ug = json.load(f)
	except:
		ug=[-1,-1]

def CallFunction(par):
	print(par)
	if(par=='moodle'):
		os.system('python3 functions/moodle.py')
	if(par=="change_tab"):
		pyautogui.hotkey('alt', 'tab')
	if(par=="snap_windows"):
		pyautogui.hotkey('winleft','left')
	if(par=="maximize"):
		pyautogui.hotkey('winleft','up')
	if(par=="open_apps"):
		os.system('python3 functions/openapps.py')
	if(par=="open_apps_win"):
		os.system('python3 functions/openappswin.py')
	if(par=="back_one_page"):
		pyautogui.hotkey('alt','esc')
		# pyautogui.press('browserback')
	if(par=='screenshot'):
		pyautogui.screenshot(r"screenshots/screenshot"+str(random.randrange(0,1000,23))+".png")



def VLC(i):
	vlc=['volume_up','Play/Pause','volume_down','fast_foward','rewind']
	if(vlc[i]=='volume_up'):
		pyautogui.press('up')
	if(vlc[i]=='Play/Pause'):
		pyautogui.press('space')



# Load()
# print('start',ug[0])
# CallFunction(ug[0])
while True:
	Load()
	thing = ser.readline().decode()
	a=int(thing)
	if checkIfProcessRunning('VLC'):
		VLC(a)
	else:	
		CallFunction(ug[a])