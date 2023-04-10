import sys
sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import pytest
from basepage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

subjects = (By.CSS_SELECTOR,'#J_posts_list > tbody > tr:nth-child(1) > td.subject > p.title > a:nth-child(3)')
reply_content_input = (By.XPATH,'//*[@id="J_reply_quick_ta"]')
reply_submit = (By.XPATH,'//*[@id="J_reply_quick_btn"]')

class PostReply(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    '''选择列表中的第一条'''
    def post_selected(self):
        self.find_ele(subjects)
        self.ele_click(subjects)
        time.sleep(2)

    def post_reply(self,reply_content):
        self.find_ele(reply_content_input)
        self.send_keys(reply_content_input,reply_content)
        time.sleep(2)
        self.ele_click(reply_submit)
        time.sleep(2)



