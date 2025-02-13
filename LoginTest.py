import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configuración de ChromeDriver
service = Service(executable_path="D:/Test_Market/chromedriver.exe")
options = Options()
options.add_argument("--start-maximized")  # Abrir el navegador maximizado

# Iniciar el WebDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Abrir URL
    driver.get("https://dev.market.orion.global/es/")  
    
    # Esperar a que la página cargue
    time.sleep(2)

    button_login = driver.find_element(By.XPATH, "//a[contains(@href, '/auth/jwt/login/')]")
    
    button_login.click()
    
    input_correo = driver.find_element(By.XPATH, "//input[@id=':r0:']")
    input_correo.send_keys("cuentademoorionhub@gmail.com")

    input_clave = driver.find_element(By.XPATH, "//input[@id=':r1:']")
    input_clave.send_keys("12345678Fs")
    time.sleep(2)

    button_entrar = driver.find_element(By.XPATH, "//button[@id=':r2:']")
    button_entrar.click()

    time.sleep(5)

finally:
    # Cerrar el navegador
    driver.quit()
