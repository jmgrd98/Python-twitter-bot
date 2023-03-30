import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())

url = 'https://twitter.com/i/flow/login'

browser = webdriver.Chrome(service=service)
browser.get(url)

# espera até que o campo de nome de usuário seja carregado
input_usuario = None
while input_usuario is None:
    try:
        input_usuario = browser.find_element(By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
    except:
        time.sleep(1)

input_usuario.send_keys('joaodantas_dev')
button_usuario = browser.find_element(By.XPATH, '//*[@id="page-container"]/div/div[1]/form/div[2]/button')
button_usuario.click()

# espera até que o campo de senha seja carregado
input_senha = None
while input_senha is None:
    try:
        input_senha = browser.find_element(By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
    except:
        time.sleep(1)

input_senha.send_keys('iloveganjah98')
button_senha = browser.find_element(By.XPATH, '//*[@id="page-container"]/div/div[1]/form/div[2]/button')
button_senha.click()

# espera até que a página seja carregada
time.sleep(5)

# exemplo de postagem de tweet
tweet_input = browser.find_element(By.XPATH, "//div[@aria-label='Tweetar']//div[@role='textbox']")
tweet_input.send_keys("Hello, world!")
tweet_input.submit()

# espera até que a página seja carregada após a postagem do tweet
time.sleep(5)

# fecha o navegador
browser.quit()