import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())

def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()

tweet = 'Mais um dia sem o Bolsonaro preso.'


driver = webdriver.Chrome()

driver.get("https://twitter.com/login")

time.sleep(1)

email_xpath = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input'
password_xpath = ''

input_email = driver.find_element(By.XPATH, email_xpath)
input_email.send_keys(email)

button_email = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
button_email.click()

input_password = driver.find_element(By.XPATH, '')


