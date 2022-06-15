from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Tablets:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver


# click the tablet category
    def tablets_category(self):
        return self.driver.find_element(By.ID,"tabletsImg").click()
# add tablet to cart and reture to main page
    def add_to_cart_tablet(self):
        self.driver.find_element(By.CSS_SELECTOR,'img[id="16"]').click()
        self.driver.find_element(By.NAME,"save_to_cart").click()
        sleep(2)

    def add_quantity_tablet_to_cart(self):
        self.driver.find_element(By.CLASS_NAME,"plus").click()
        sleep(2)
        self.driver.find_element(By.NAME,"save_to_cart").click()








