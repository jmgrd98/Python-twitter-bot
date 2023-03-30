import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def account_info():
    with open('account_info.txt' 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()

tweet = 'Mais um dia sem o Bolsonaro preso.'

Options = Options()
Options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://twitter.com/login")