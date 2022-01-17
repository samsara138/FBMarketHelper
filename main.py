from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time
import pickle
import re
import json
import SeleniumHelper

#PATH=$PATH:/mnt/e/Programming/Sources/Python/Web_Automation
#https://www.programcreek.com/python/index/8077/selenium.webdriver.common.by.By
#https://selenium-python.readthedocs.io/locating-elements.html
#https://stackoverflow.com/questions/21713280/find-div-element-by-multiple-class-names

#wait commands

configData = {}

def get_headless_driver():
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--incognito')
	options.add_argument("disable-infobars")
	if(configData["Headless"]):
		options.add_argument('--headless')
	options.add_argument('window-size=1920x1080')
	driver = webdriver.Chrome(chrome_options=options)
	return driver

def login(driver):
	#Login
	SeleniumHelper.smart_interaction(driver,By.ID,"email",sendKey=configData["Email"])
	SeleniumHelper.smart_interaction(driver,By.ID,"pass",sendKey=configData["Password"])
	SeleniumHelper.smart_interaction(driver,By.ID,"loginbutton",click=True)

def goto_market(driver):
	#Find Marketplace
	XPATH = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input"
	SeleniumHelper.smart_interaction(driver,By.XPATH ,XPATH)
	soup = BeautifulSoup(driver.page_source, "html.parser")
	x = soup.find(string='Marketplace')
	for i in range(11):
		x = x.find_parent()
	classString = ' '.join(x["class"])
	cssStr = "div[class='" + classString + "']"
	SeleniumHelper.smart_interaction(driver,By.CSS_SELECTOR ,cssStr,click=True)

def find_and_send(driver):
	#Find is scammer exist
	message = configData["TargetMsg"]
	reply = configData["Respond"]

	XPATH = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div"
	SeleniumHelper.smart_interaction(driver,By.XPATH ,XPATH)
	time.sleep(2)
	soup = BeautifulSoup(driver.page_source, "html.parser")
	x = soup.find_all(string=re.compile(message))
	for hit in x:
		try:
			for i in range(12):
				hit = hit.find_parent()
			chatURL = "https://www.messenger.com" + hit["href"]
			driver.get(chatURL)
			reply += '\n'
			SeleniumHelper.smart_interaction(driver,By.XPATH ,"//div[@class='_1mf _1mj']",sendKey=reply)
			print("********************")
			print("*****GOT A HIT!*****")
			print("********************")
			return
		except:
			pass

def scrap(driver):
	driver.get('https://www.messenger.com')
	print("Logging in...")
	login(driver)
	print("Login complete")
	while(True):
		goto_market(driver)
		print("Checking message")
		find_and_send(driver)
		print("NEXT")
	input("Press anything to exit")

def load_json():
	global configData
	with open("config.json","r") as configFile:
		configData = json.load(configFile)

	print("********Data in config.json********")
	print("Your email:",configData["Email"])
	print("Your password:",configData["Password"])
	print("Hide browzer:",configData["Headless"])
	print("Checking for message:",configData["TargetMsg"])
	print("You will reply:",configData["Respond"])
	print("***********************************\n\n")

def main():
	load_json()
	driver = get_headless_driver()
	try:
		scrap(driver)
	except:
		with open("ErrorHTML.html","w") as f:
			f.write(driver.page_source)
	driver.close()

if __name__ == '__main__':
	main()
