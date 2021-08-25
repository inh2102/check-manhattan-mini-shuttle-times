#!/usr/bin/env python
# coding: utf-8

# In[130]:


import logging
import time
from datetime import datetime
import os
now=datetime.now()
date_time=now.strftime("%m%d%I%M")
cwd = os.getcwd()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import sys
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 800))
# display.start()
csmart_user = 'isaac.horwitz@columbia.edu'
csmart_pass = 'abc123jack'

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_css_selector(css):
    try:
        driver.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_id(the_id):
    try:
        driver.find_element_by_id(the_id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(class_name):
    try:
        driver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True

def random_wait():
    import random
    num = random.randint(1,3)
    time.sleep(num)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
op = Options()
op.add_argument("--headless")
op.add_argument("window-size=1080x1020")
#set download directory path
p = {"download.default_directory":"../data/raw","safebrowsing.enabled":"false"}
op.add_experimental_option("prefs", p)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
driver.get("https://www.manhattanministorage.com/login-register")

while not check_exists_by_css_selector('#Email'):
    time.sleep(random_wait())
username = driver.find_element_by_css_selector('#Email')
username.send_keys(csmart_user)

password = driver.find_element_by_css_selector('#Password')
password.send_keys(csmart_pass)

login = driver.find_element_by_css_selector('.btn-wrapper .btn-wide')
login.click()

time.sleep(6)

shuttle = driver.find_element_by_css_selector('#main-content li:nth-child(5) a')
shuttle.click()


# In[138]:


driver.execute_script("window.scrollTo(0,500)")
driver.execute_script("window.scrollTo(0,500)")
time.sleep(5)
address = driver.find_element_by_css_selector('.padding-right:nth-child(1) .ng-invalid')
address.send_keys('85 Kenmare St')

code = driver.find_element_by_css_selector('.padding-left .ng-invalid')
code.send_keys('10012')


# In[139]:


loop = 0
for i in range(3,20):
    calendar = driver.find_element_by_css_selector('.fa-calendar')
    calendar.click()
    time.sleep(5)
    if loop==0:
        sep = driver.find_elements_by_class_name('ngb-dp-arrow')[1]
        sep.click()
    time.sleep(3)
    days = driver.find_elements_by_class_name('day-on-calendar')
    day = days[i]
    txt = day.text
    day.click()
    done = driver.find_element_by_css_selector('.btn-default')
    done.click()
    loop+=1
    time.sleep(10)
    driver.execute_script("scrollBy(0,-10000);")
    if "Sorry, we have no availability" in driver.page_source:
        driver.execute_script("window.scrollTo(0,500)")
        driver.execute_script("window.scrollTo(0,500)")
        print("No time on Sep." + " " + txt)
        next
    else:
        print("Found a time on Sep." + " " + txt)
        break
        driver.close()

