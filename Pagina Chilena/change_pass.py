import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string

letters = string.ascii_letters+"0123456789"+"ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"+"ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز"

driver = webdriver.Chrome()

def change_password(user,password_ant):
    driver.get("https://mybox.cl/iniciar-sesion")
    try:
        usr = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div[1]/input')
        usr.clear()
        usr.send_keys(user)
        psswrd = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/div/input')
        psswrd.clear()
        psswrd.send_keys(password_ant)

        click = driver.find_element_by_xpath('//*[@id="submit-login"]').click()
    except:
        print("hubo un error")

    driver.find_element_by_xpath('/html/body/main/header/div[2]/div[1]/div/div/div[3]/div/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="identity-link"]').click()
    psswrd = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[4]/div[1]/div/input')
    psswrd.clear()
    psswrd2 = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[5]/div[1]/div/input')
    psswrd2.clear()
    password = "".join(random.choice(letters) for i in range(5))
    psswrd.send_keys(password_ant)
    psswrd2.send_keys(password)

    driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/div/div[2]/form/footer/div/div[2]/button').click()
    print("Contrseña Nueva:",password)

change_password("basty3lol@gmail.com","12345")