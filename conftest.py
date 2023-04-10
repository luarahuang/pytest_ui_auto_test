
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login import LoginPage
import logging
from util.logger import GetLogger
from util.get_yml_data import GetYamlData
import os




logger = GetLogger().log_handlers()

yml_config = GetYamlData().get_yaml_data()
homepage_url = yml_config['login_url']
username = yml_config['loginuser']['username']
pwd = yml_config['loginuser']['pwd']


'''session级别生成一个webdriver'''
@pytest.fixture(scope='session',autouse=True)
def init_browser():
    # global driver
    # if browser.lower() == 'chrome':
    #     chrome_options = Options()
    #     chrome_options.add_experimental_option("detach", True)
    #     driver = webdriver.Chrome(options=chrome_options)
    # else:
    #     raise ValueError('Unsupported browser type: {}'.format(browser))
    # return driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    logger.info('------ 打开浏览器并最大化------')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(2)
    '''所有测试用例执行完后，关闭浏览器'''
    yield driver
    logger.info('------- 所有用例执行完毕，关闭浏览器！---------')
    driver.quit()


@pytest.fixture(scope='session',autouse=True)
def open_homepage_and_login(init_browser):
    '''打开一个driver后，session级别登录'''
    init_browser.get(homepage_url)
    logger.info('--------- 打开网页首页：{} ----------'.format(homepage_url))
    login_page = LoginPage(init_browser)
    login_page.switch_loginpage()
    login_page.login(username,pwd)
    logger.info("------ 登录成功，用户：{},密码：{} --------".format(username,pwd))

@pytest.fixture(scope='class',autouse=True)
def open_homepage(init_browser):
    '''每次用例之前重新打开首页'''
    init_browser.get(homepage_url)

#将log输出到log文件
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s >>> %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename=os.path.join(os.getcwd(), 'mylog.log'),
#                     filemode='a')






