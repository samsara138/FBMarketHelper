from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys

#PATH=$PATH:/mnt/e/Programming/Sources/Python/Web_Automation
#https://www.programcreek.com/python/index/8077/selenium.webdriver.common.by.By

#wait commands
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def smart_interaction(driver,byFunc,data,sendKey='',click=False,threashold = 5,bufferWait = 0.5):
    '''
    @input
    driver: The web WebDriver
    byFunc: e.g By.ID, By.XPATH, ref = https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
    data: name of data for byFunc
    sendKey: enter if sending a string to the element
    click: set to True if clicking the element
    threashold: Total number of time waiting before report error
    bufferWait: Time wait between each access attempt
    '''
    if(sendKey != '' and click):
        sys.stderr.write("ERROR: Cannot sendkey and click\n")

    loopCount = int(threashold / bufferWait)
    for i in range(loopCount):
        try:
            e = driver.find_element(byFunc,data)
            if(sendKey != ''):
                e.send_keys(sendKey)
            elif(click):
                e.click()
            return e
        except:
            pass
        time.sleep(bufferWait)
    return False
