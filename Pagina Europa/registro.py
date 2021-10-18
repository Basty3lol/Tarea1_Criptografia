from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import string
from itertools import product

driver = webdriver.Chrome()

def registro(user,password):
    driver.get("https://www.coolmod.com/login/")

    button = driver.find_element_by_xpath('//*[@id="coolbody"]/section/div/div/div[2]/div[8]/button')
    driver.execute_script("arguments[0].click();", button)

    driver.find_element_by_xpath('//*[@id="privacitycheck"]').click()

    usr = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    usr.clear()
    usr.send_keys(user)

    pass1 = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    pass1.clear()
    pass1.send_keys(password)

    pass2 = driver.find_element_by_xpath('//*[@id="inputPassword2"]')
    pass2.clear()
    pass2.send_keys(password)

    button2 = driver.find_element_by_xpath('//*[@id="formRegister"]/div[14]/button')
    driver.execute_script("arguments[0].click();", button2)

registro("caferep433@wii999.com","aaaaaA1$")