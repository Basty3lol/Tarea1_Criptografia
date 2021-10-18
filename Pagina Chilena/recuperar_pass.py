import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string

driver = webdriver.Chrome()

def change_password(user):
    driver.get("https://mybox.cl/iniciar-sesion")

    driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/section/form/section/div[3]/a').click()

    usr = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/section/form/input')
    usr.clear()
    usr.send_keys(user)

    driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/section/form/button').click()

change_password("basty3lol@gmail.com")