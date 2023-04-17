#import sys
#sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import pytest
import allure

from pages.homepage import Homepage


homepage_title = '本站新帖 - phpwind 9.0 - Powered by phpwind'

@allure.feature('首页测试1')

class TestCase001:
    @pytest.mark.smoke
    @allure.story('首页搜索')
    @allure.severity("critical")
    @pytest.mark.parametrize('content',(1,2,3,4,5))
    def test_001(self,init_browser,content):
        hg_page = Homepage(init_browser)
        hg_page.page_search(content)
        assert 1 == 1

    @pytest.mark.function
    @allure.story('打开首页')
    @allure.severity("normal")
    def test_002(self):
        pass
        assert 1 == 1

    @pytest.mark.webtest
    @pytest.mark.skip(reason="该功能暂未实现，跳过测试。")
    @allure.story('首页测试3')
    @allure.severity("normal")
    def test_003(self):
        pass
        assert 1 == 1

    @pytest.mark.smoke
    @allure.story('首页测试4')
    @allure.severity("normal")
    def test004(self):
        pass
        assert 1 == 2
        
if __name__ == '__main__':
    pytest.main(['-v','./cases/test_homepage.py'])
    
