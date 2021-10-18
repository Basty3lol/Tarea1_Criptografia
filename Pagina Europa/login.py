from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import string
from itertools import product

driver = webdriver.Chrome()

def login(user,password):
    driver.get("https://www.coolmod.com/login/")
    try:
        usr = driver.find_element_by_xpath('//*[@id="inputEmail"]')
        usr.clear()
        usr.send_keys(user)
        psswrd = driver.find_element_by_xpath('//*[@id="inputPassword"]')
        psswrd.clear()
        psswrd.send_keys(password)

        driver.find_element_by_xpath('//*[@id="formLogin"]/div[7]/button').click()
    except:
        print("hubo un error")

login("basty3lol@gmail.com","aaaaaA1$")