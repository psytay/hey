from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from general_class import general
from TABLETS_Class import Tablets
from speakers_class import Speakers
from cart_page_class import cart_page_class

class AOS_UnitTests(TestCase):
    def setUp(self):
        service_chrome = Service(r"E:\chromedriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get('https://www.advantageonlineshopping.com/#/')
        self.driver.maximize_window()
        # In case an element is not found on the page,
        # will try again for 10 seconds, before we get an error message
        self.driver.implicitly_wait(10)
        # giving all the classes import objects
        self.main_bar=general(self.driver)
        self.tablets=Tablets(self.driver)
        self.speakers=Speakers(self.driver)
        self.cart_page=cart_page_class(self.driver)


    def test_Quantity_items_in_cart(self):
        """this test is checking that the quantity after editing the items indeed save and correct"""
        self.tablets.tablets_category()
        sleep(2)
        self.tablets.add_to_cart_tablet()
        self.main_bar.main_page()
        self.speakers.speakers_category()
        sleep(2)
        self.speakers.add_speaker_to_cart()
        self.main_bar.main_page()
        self.main_bar.cart()
        self.cart_page.click_edit_first_item()
        sleep(2)
        self.speakers.add_quantity_speakers_to_cart()
        self.cart_page.click_edit_secend_item()
        sleep(2)
        self.tablets.add_quantity_tablet_to_cart()
        sleep(5)
        self.asser

    def tearDown(self):
        self.driver.close()









