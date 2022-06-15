from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class cart_page_class:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
    def click_edit_first_item(self):
        self.driver.find_element\
            (By.CSS_SELECTOR,'a[href="#/product/25?color=55CDD5&quantity=1&pageState=edit&warranty="]').click()

    def click_edit_secend_item(self):
        self.driver.find_element\
            (By.CSS_SELECTOR,'a[href="#/product/16?color=414141&quantity=1&pageState=edit&warranty="]').click()


    def quantity_finder_first(self):
        self.driver.find_element(By.LINK_TEXT,"2")
