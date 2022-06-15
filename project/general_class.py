from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class general:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
# פונקציה
    def main_page(self):
      return self.driver.find_element(By.CSS_SELECTOR,'a[ng-click="go_up()"]').click()

    def accout_login(self):
        return self.driver.find_element(By.ID,"menuUser").click()

    def cart(self):
        return self.driver.find_element(By.ID,"menuCart").click()






