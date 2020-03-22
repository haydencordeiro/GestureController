import eel
import json
import os




eel.init('web')


ug=[-1,-1]
def Save():
	global ug
	with open("data/all_user_data.json", 'r') as f:
		d = json.load(f)
	d['ug']=ug
	with open("data/all_user_data.json", 'w') as k:
		json.dump(d, k, indent=2) 

@eel.expose
def Index0(param1):
    global ug
    print('here')
    ug[0]=param1
    Save()
    print(ug)

@eel.expose
def Index1(param1):
    global ug
    ug[1]=param1
    Save()
    print(ug)

@eel.expose
def moodleLogin(p1,p2):
	moodleInfo=['','']
	moodleInfo[0]=str(p1)
	moodleInfo[1]=str(p2)
	with open("data/all_user_data.json", 'r') as f:
		d = json.load(f)
	d['moodleInfo']=moodleInfo
	with open("data/all_user_data.json", 'w') as k:
		json.dump(d, k, indent=2) 

@eel.expose
def multi_apps(string1):
	print(string1)
	with open("data/all_user_data.json", 'r') as f:
		d = json.load(f)
	d['multi_apps']=string1
	with open("data/all_user_data.json", 'w') as k:
		json.dump(d, k, indent=2) 


    

@eel.expose
def end():
	os.system('python3 main.py')
	

eel.start('index.html')


