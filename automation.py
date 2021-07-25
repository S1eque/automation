from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome("C:\chromedriver")
   
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    browser.execute_script("window.scrollBy(0, 100);")
    x = browser.find_element_by_id('input_value').text
    result = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_id('solve').click()
    
   
    

finally:
    time.sleep(15)
    browser.quit()

