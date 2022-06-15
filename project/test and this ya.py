from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from general_class import general
from TABLETS_Class import Tablets
from speakers_class import Speakers
from cart_page_class import cart_page_class

service_chrome = Service(r"E:\chromedriver\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/#/")

main_bar=general(driver)
tablets=Tablets(driver)
speakers=Speakers(driver)
cart_page_class=cart_page_class(driver)

driver.implicitly_wait(10)


tablets.tablets_category()
sleep(2)
tablets.add_to_cart_tablet()
main_bar.main_page()
speakers.speakers_category()
sleep(2)
speakers.add_speaker_to_cart()
main_bar.main_page()
main_bar.cart()
cart_page_class.click_edit_first_item()
#sleep(2)
speakers.add_quantity_speakers_to_cart()
cart_page_class.quantity_finder_first()
#cart_page_class.click_edit_secend_item()
#tablets.add_quantity_tablet_to_cart()




