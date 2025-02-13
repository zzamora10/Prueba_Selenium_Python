import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración de ChromeDriver
        service = Service(executable_path="D:/Test_Market/chromedriver.exe")
        options = Options()
        options.add_argument("--start-maximized")  # Abrir el navegador maximizado

        # Iniciar el WebDriver
        cls.driver = webdriver.Chrome(service=service, options=options)

    def setUp(self):
        # Abrir URL antes de cada prueba
        self.driver.get("https://dev.market.orion.global/es/")  
        time.sleep(2)

    def test_successful_login(self):
        # Realizar el proceso de login
        button_login = self.driver.find_element(By.XPATH, "//a[contains(@href, '/auth/jwt/login/')]")
        self.assertTrue(button_login.is_displayed(), "El botón de entrar no es visible")
        button_login.click()

        input_correo = self.driver.find_element(By.XPATH, "//input[@id=':r0:']")
        input_correo.send_keys("cuentademoorionhub@gmail.com")

        input_clave = self.driver.find_element(By.XPATH, "//input[@id=':r1:']")
        input_clave.send_keys("12345678Fs")
        time.sleep(2)

        button_entrar = self.driver.find_element(By.XPATH, "//button[@id=':r2:']")
        button_entrar.click()

        # Esperar un poco a que la página cargue después del login
        time.sleep(5)

        # Validar que el login fue exitoso
        # Verificar si el URL cambió después del login
        expected_url = "https://dev.market.orion.global/es/subscription/"
        self.assertEqual(self.driver.current_url, expected_url, "Se ingreso a las subscription del usuario")

        #Habilitar Boton de usuario
        button_img = self.driver.find_element(By.XPATH, "//div[@class='MuiAvatar-root MuiAvatar-circular mui-1hkk74q']//img")
        button_img.click()
        time.sleep(5)
        #Validaciones del usuario logueado

        menu_usuario = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/h6")
        # Obtener el texto del elemento
        texto_obtenido = menu_usuario.text
        # El texto esperado
        texto_esperado = "Cuenta Demo"
        # Validar que el texto obtenido sea el esperado
        self.assertEqual(texto_obtenido, texto_esperado, f"El texto esperado era '{texto_esperado}' pero se encontró '{texto_obtenido}'")


        usuario = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/p")
        # Obtener el texto del elemento
        texto_obtenido = usuario.text
        # El texto esperado
        texto_esperado = "cuentademoorionhub@gmail.com"
        # Validar que el texto obtenido sea el esperado
        self.assertEqual(texto_obtenido, texto_esperado, f"El texto esperado era '{texto_esperado}' pero se encontró '{texto_obtenido}'")

    def tearDown(self):
        # Limpiar después de cada prueba si es necesario
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Cerrar el navegador después de ejecutar todas las pruebas
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
