from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random


driver = webdriver.Chrome()

def registrar(correo):
    driver.get("https://mybox.cl/iniciar-sesion?create_account=1")

    user = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[3]/div[1]/input')
    user.clear()
    user.send_keys(correo)

    nombre = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[1]/div[1]/input')
    nombre.clear()
    nombre.send_keys("Bastian")

    apellido = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[2]/div[1]/input')
    apellido.clear()
    apellido.send_keys("Castro")

    password = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[4]/div[1]/div/input')
    password.clear()
    password.send_keys("12345")

    driver.find_element_by_xpath('/html/body/main/section/div[2]/div/section/section/section/form/footer/div/div[2]/button').click()


registrar("caferep433@wii999.com")