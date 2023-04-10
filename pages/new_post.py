import sys
sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import pytest
import allure

from basepage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

new_post_btn = (By.XPATH,'//*[@id="J_head_forum_post"]')
category = (By.XPATH,'//*[@id="J_forum_list"]/li')
topic = (By.XPATH,'//*[@id="J_forum_ul"]/li[1]')
comfirm_btn = (By.XPATH,'//*[@id="J_head_forum_sub"]')
post_title_input = (By.NAME,'atc_title')
post_content_input = (By.CSS_SELECTOR,'body')
content_submit = (By.XPATH,'//*[@id="J_post_sub"]')
content_ifram = (By.CSS_SELECTOR,'#mainForm > div > nav > nav > div > div.cc.mb10 > div.cm > div > div > div.wind_editor_body > iframe')
title = (By.CSS_SELECTOR,'#J_post_title')

class NewPost(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    '''点击发帖，选择版本，进入发帖界面'''
    @allure.step('选择topic打开发帖界面')
    def open_new_post(self):
        self.ele_click(new_post_btn)
        self.ele_click(category)
        self.ele_click(topic)
        time.sleep(2)
        self.ele_click(comfirm_btn)
        time.sleep(2)

    '''输入标题和内容，发帖'''
    @allure.step('输入内容发帖')
    def new_post(self,title,content):
        self.send_keys(post_title_input,title)
        self.swith_to_iframe(content_ifram)
        self.send_keys(post_content_input,content)
        self.driver.switch_to.default_content()
        self.ele_click(content_submit)

    def get_post_title(self):
        return self.get_ele_text(title)
