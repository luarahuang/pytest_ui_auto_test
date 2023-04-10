#from selenium.webdriver.common.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

import time
import logging
from util.logger import GetLogger


class BasePage(object):
    def __init__(self,driver):
        self.logger = GetLogger().log_handlers()
        self.driver = driver

    # def chromedriver(self,browser = 'Chrome'):
    #     if self.browser.lower() == 'chrome':
    #         self.chrome_options = Options()
    #         self.chrome_options.add_experimental_option("detach", True)
    #         self.driver = webdriver.Chrome(options=self.chrome_options)
    #     else:
    #         raise ValueError('Unsupported browser type: {}'.format(browser))
    #     return self.driver
        
    def wait_ele_visible(self,locator,time=0.3,frequncy=0.5):
        '''等待元素可见，否则抛出异常'''
        try:
            WebDriverWait(self.driver,time,frequncy).until(EC.visibility_of_element_located(locator))
            self.logger.info('等待xx元素出现'.format(locator))
        except TimeoutException :
            self.logger.error('无法找到xx元素'.format(locator))
            raise TimeoutException('找不到该元素！')
            

    def find_ele(self,locator):
        try:
            self.wait_ele_visible(locator)
            ele = self.driver.find_element(*locator)
            self.logger.info('定位到了{}元素'.format(ele))
            return ele
        except Exception as e:
            raise e

    def find_eles(self,locator):
        self.driver.find_elements(*locator)[0]
        
    def send_keys(self,locator,content):
        ele = self.find_ele(locator)
        ele.send_keys(content)
        self.logger.info('输入的内容为：{}'.format(content))


    def send_keys_and_enter(self,locator,content):
        ele = self.find_ele(locator)
        ele.send_keys(content)
        ele.send_keys(Keys.ENTER)

    def ele_click(self,locator):
        self.find_ele(locator).click()

    def ele_selected_click(self,locator):
        self.driver.find_elements(*locator)[0].click()

    def get_title(self):
        return  self.driver.title
    
    # def switch_new_window(self):
    #     self.driver.

    def swith_to_iframe(self,locator):
        iframe = self.find_ele(locator)
        self.driver.switch_to.frame(iframe)

    def get_ele_text(self,locator):
        return self.find_ele(locator).text
        
