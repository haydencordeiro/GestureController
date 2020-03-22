from selenium import webdriver
from time import sleep
import json
try:
	with open("../data/all_user_data.json", 'r') as f:
	  cred = json.load(f)
	  cred=cred['moodleInfo']
	print(cred)
except :
	cred=['','']

def Moodle():
	driver = webdriver.Firefox()

	driver.get("https://moodle.dbit.in/login/index.php")
	driver.find_element_by_xpath('//*[@id="username"]').send_keys(cred[0])#218grejo0019
	driver.find_element_by_xpath('//*[@id="password"]').send_keys(cred[1])#grejojoby123
	driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
	driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[2]/ul[1]/li[2]/a').click()
	driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/div[1]/div[2]/div/div[3]/div[1]/h3/a').click()
	driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/div[3]/div[2]/div[1]/div[2]/div[1]/h3/a').click()
	driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/div[3]/div[2]/div/div[2]/div[1]/h3/a').click()
Moodle()