import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# dir = os.path.dirname('C:\Drivers')
# chrome_driver = dir + '\chromedriver.exe'

# driver = webdriver.Chrome()


class TwitterBot:
    def __init__(self, username):
        self.username = username
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.bot = webdriver.Chrome(options=options)
        self.bot.implicitly_wait(30)
        self.bot.maximize_window()

    def login(self):
        bot = self.bot
        bot.get('https://apps.exxat.com/Fusion/Account/Login')
        # time.sleep(5)
        # email = bot.find_element_by_name('Username')
        email = bot.find_element(By.NAME,"Username")
        email.clear()
        email.send_keys(self.username)
        time.sleep(2)
        email.send_keys(Keys.RETURN)
        time.sleep(2)
        email = bot.find_element(By.ID,"i0116")
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)

ed = TwitterBot('vikram.singh@exxat.com')
ed.login()