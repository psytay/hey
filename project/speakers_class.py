from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Speakers:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

#click the speakers category
    def speakers_category(self):
        return self.driver.find_element(By.ID,"speakersImg").click()

    def add_speaker_to_cart(self):
        self.driver.find_element(By.ID,"25").click()
        self.driver.find_element(By.NAME,"save_to_cart").click()
        sleep(2)
    def add_quantity_speakers_to_cart(self):
        self.driver.find_element(By.CLASS_NAME,"plus").click()
        self.driver.find_element(By.NAME, "save_to_cart").click()




