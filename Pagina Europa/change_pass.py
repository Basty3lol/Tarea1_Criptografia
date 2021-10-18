from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import string
from itertools import product
import random

driver = webdriver.Chrome()

letters_min = string.ascii_lowercase
letters_mayu = string.ascii_uppercase
numbers = "0123456789"
simbols = "$#%&/=?¿+-_"
extra = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"+"ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز"
def change_password(password_ant):
    driver.get("https://www.coolmod.com/login/")

    usr = driver.find_element_by_xpath('//*[@id="inputEmail"]')
    usr.clear()
    usr.send_keys("basty3lol@gmail.com")
    psswrd = driver.find_element_by_xpath('//*[@id="inputPassword"]')
    psswrd.clear()
    psswrd.send_keys(password_ant)

    driver.find_element_by_xpath('//*[@id="formLogin"]/div[7]/button').click()
    time.sleep(3)

    button = driver.find_element_by_xpath('//*[@id="coolbody"]/section/section/div[2]/div[3]/div/div/div[1]/div/div[2]/div[6]/button[1]')
    driver.execute_script("arguments[0].click();", button)

    password = "".join(random.choice(letters_min) for i in range(2))
    password = password + "".join(random.choice(letters_mayu) for i in range(2))
    password = password + "".join(random.choice(numbers) for i in range(2))
    password = password + "".join(random.choice(simbols) for i in range(2))

    psw = driver.find_element_by_xpath('/html/body/div[1]/section/section/div[2]/div[3]/div/div/div[1]/div/div[2]/div[4]/div/div[2]/input[1]')
    psw.clear()
    psw.send_keys(password)
    psw2 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div[2]/div[3]/div/div/div[1]/div/div[2]/div[5]/div/div[2]/input[1]')
    psw2.clear()
    psw2.send_keys(password)

    button2 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div[2]/div[3]/div/div/div[1]/div/div[2]/div[6]/button[2]')
    driver.execute_script("arguments[0].click();", button2)
    print("contraseña nueva:",password)

change_password("aaaaaA1$")