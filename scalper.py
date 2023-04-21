from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge("C:\Program Files\msedgedriver.exe")
import time
driver.maximize_window()


id = driver.find_element_by_id
get = driver.get
get(' # amazon link')
buyButton = False

while not buyButton:
    try:

        id('buybox-see-all-buying-choices')
        print('out of stock. LOL')

        time.sleep(1)
        driver.refresh()
        
    except:

        id('buy-now-button')
        print('button')
        id('buy-now-button').click()
        buyButton = True

id('ap_email').send_keys("dawishwishub@gmail.com")
id('continue').click()

id('ap_password').send_keys("daawiit21")
id('signInSubmit').click()
