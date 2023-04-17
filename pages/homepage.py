print(__name__)
import sys
sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
from basepage.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

input_name = (By.NAME,'keyword')

class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    '''首页查询栏输入查询条件'''
    def page_search(self,content):
        self.send_keys_and_enter(input_name,content)


    