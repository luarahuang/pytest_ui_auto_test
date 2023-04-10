import sys
sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import pytest
import allure
from basepage.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


base_url = 'http://47.107.116.139/phpwind/'
login_btn = (By.ID,"J_sidebar_login")
username_input = (By.ID,"J_u_login_username")
pwd_input = (By.ID,"J_u_login_password")
submit = (By.CSS_SELECTOR,'#J_u_login_form > div > dl:nth-child(6) > dd > button')



class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    '''定位到登录按钮，点击打开登录界面'''
    @allure.step('打开登录界面')
    def switch_loginpage(self):
        self.ele_click(login_btn)
        #self.driver.switch_to.window()
        return self.get_title()
    
    @allure.step('输入用户名、密码登录')
    def login(self,user,pwd):
        self.send_keys(username_input,user)
        self.send_keys(pwd_input,pwd)
        self.ele_click(submit)
        time.sleep(2)



