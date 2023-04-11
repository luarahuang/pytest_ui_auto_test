#import sys
#sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import pytest
import allure
from pages.new_post import NewPost

title = '发表帖子 - phpwind 9.0 - Powered by phpwind'
post_title = 'newpost666'
post_body = '66666666'

@allure.feature('发帖测试')
class TestNewPost:
    @allure.story('打开发帖界面')
    @allure.severity("normal")
    @pytest.mark.webtest
    def test_new_post001(self,init_browser):
        new_post = NewPost(init_browser)
        new_post.open_new_post()
        assert new_post.get_title() == title

    @allure.story('输入内容发帖')
    @allure.severity("normal")
    @pytest.mark.webtest
    def test_newpost002(self,init_browser):
        new_post = NewPost(init_browser)
        new_post.new_post(post_title,post_body)
        assert new_post.get_post_title() == post_title


if __name__ == '__main__':
    pytest.main(['-v','./cases/'])
    
