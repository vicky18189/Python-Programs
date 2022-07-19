from time import sleep
from selenium import webdriver

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com')
        sleep(2)

InstaBot('vicky18189@gmail.com','Ankur_89')