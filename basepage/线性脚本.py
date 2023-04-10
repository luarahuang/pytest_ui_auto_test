#from selenium.webdriver.common.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://47.107.116.139/phpwind/")
driver.implicitly_wait(2)
driver.maximize_window()
search_input = driver.find_element(by=By.NAME, value='keyword')
#在定位到的输入框中输入内容并回车
search_input.send_keys('selenium'+Keys.ENTER)
time.sleep(2)
driver.quit()

