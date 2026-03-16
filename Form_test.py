from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_formulario_contacto():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        #Entrar a una pagina con formulario
        driver.get("https://karaokeivan.com/index.php/login/")
        driver.maximize_window()
        print("Navegador abierto en la zona de pruebas")

        #Encontrar campos por NAME o ID y escribir (Simulando ser un usuario)
        #En esta web los IDs son "user_login" y "user_pass"
        user_input = driver.find_element(By.ID, "user_login")
        pass_input = driver.find_element(By.ID, "user_pass")

        user_input.send_keys("FakeUser") # Escribimos el usuario
        pass_input.send_keys("FakePassword") # Escribimos la clave
        print("Campos completados automaticamente")

        #Simular el click en el boton de login
        #Buscamos el boton su tipo "submit"
        boton_login = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        boton_login.click()
        print("Click en el boton de ingresar")

        #VALIDACION
        #Le damos tiempo a que cargue
        time.sleep(2) 
        #Verificamos si aparecio el mensaje de exito
        mensaje_error = driver.find_element(By.CSS_SELECTOR, "div.pmpro_message").text
        if "no está registrado en este sitio" in mensaje_error:
            print("Mensaje de error detectado correctamente (La pagina detecto que el usuario no existe)")
        else:
            print("El mensaje de error no es el esperado")

    except Exception as e:
        print(f"Hubo un error durante el test: {e}")
    
    finally:
        driver.quit()
        print("Sesion finalizada")

if __name__ == "__main__":
    test_formulario_contacto()
