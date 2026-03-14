from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_health_check(url):
    print(f"Iniciando Auditoria de UI en: {url}")
    
    # Configuracion del navegador (Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Ejecutar sin abrir la ventana (mas rapido y ahorra recursos)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        start_time = time.time()
        driver.get(url)
        
        #Comprobar tiempo de carga
        tiempo_carga = time.time() - start_time
        print(f"✅ Pagina cargada en {tiempo_carga:.2f} segundos.")

        #Comprobar titulo de la pagina
        titulo = driver.title
        print(f"✅ Titulo detectado: '{titulo}'")

        #Comprobar si existe un texto especifico en la pagina
        texto_a_buscar = "Tu texto aqui" # Cambia esto por el texto que quieras verificar
        texto = driver.find_elements(By.XPATH, f"//*[contains(text(), '{texto_a_buscar}')]")
        if len(texto) > 0:
         print(f"✅ {len(texto)} elementos con texto '{texto_a_buscar}' encontrado correctamente")
        else:
         print(f"❌ ERROR: La palabra ´{texto_a_buscar}´ no aparece en la pagina")

        #Comprobar si existen elementos clave
        #Si se quiere comprobar un elemento especifico se puede cambiar el "TAG_NAME" por el deseado
        #Ejemplo: form, label, button, etc. 
        elemento = driver.find_elements(By.TAG_NAME, "a")
        print(f"✅ Se encontraron {len(elemento)} elementos en la pagina.")
        #Comprobacion de resultados de "elementos clave"
        if len(elemento) > 0:
            print("🟢 Estado de la pagina: Correcto")
        else:
            print("🔴 Estado de la pagina: Posibles errores")

    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
    
    finally:
        driver.quit()
        print("Navegador cerrado.")

if __name__ == "__main__":
    # Prueba con tu portfolio o cualquier sitio web
    run_health_check("https://karaokeivan.com/")