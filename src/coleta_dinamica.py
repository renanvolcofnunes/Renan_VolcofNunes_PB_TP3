from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://infovis.sei.ba.gov.br/juventudes/"

BASE = Path(__file__).resolve().parent.parent
ARQUIVO = BASE / "data" / "processed" / "painel_juventudes_trabalho.txt"

def coletar_dados():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        WebDriverWait(driver, 30).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        texto = driver.execute_script("return document.body.innerText")

        if not texto:
            texto = driver.execute_script("return document.body.textContent")

    finally:
        driver.quit()

    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO.write_text(texto, encoding="utf-8")

    print("Coleta concluída.")
    print("Caracteres coletados:", len(texto))
    print("Arquivo:", ARQUIVO)

if __name__ == "__main__":
    coletar_dados()