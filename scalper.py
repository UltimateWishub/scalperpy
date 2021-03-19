from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge("C:\Program Files\msedgedriver.exe")
import time

id = driver.find_element_by_id
get = driver.get
get('https://www.amazon.com/gp/product/B08FC5L3RG')
buyButton = False

while not buyButton:
    try:

        id('buybox-see-all-buying-choices')
        print('out of stock. LOL')

        time.sleep(1)
        driver.refresh()
        
    except:

    

