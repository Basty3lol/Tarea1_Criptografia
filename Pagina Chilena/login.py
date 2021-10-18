from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import string
from itertools import product

driver = webdriver.Chrome()

def login(user, password):
    driver.get("https://mybox.cl/iniciar-sesion")
    try:
        usr = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div[1]/input')
        usr.clear()
        usr.send_keys(user)
        psswrd = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/div/input')
        psswrd.clear()
        psswrd.send_keys(password)

        click = driver.find_element_by_xpath('//*[@id="submit-login"]').click()
    except:
        print("hubo un error")

login("basty3lol@gmail.com","12345")