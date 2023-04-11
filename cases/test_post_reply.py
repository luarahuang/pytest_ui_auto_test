#import sys
#sys.path.append('/Users/luna/Documents/learning_python/testing/ui_phpwind')
import pytest
import allure
import logging
from pages.post_reply import PostReply

reply_content = '12345678'

class TestPostReply:
    @pytest.mark.webtest
    @allure.story('回帖')
    @allure.severity("critical")
    def test_post_reply001(self,init_browser):
        post_reply = PostReply(init_browser)
        post_reply.post_selected()
        post_reply.post_reply(reply_content)
        #logging.info("回复的内容为:{}".format(reply_content))


if __name__ == '__main__':
    pytest.main(['-v','./cases/test_post_reply.py'])
    
