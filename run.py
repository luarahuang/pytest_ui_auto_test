# -*- coding:utf-8 -*-
# 作者：hxx
# 时间：2023/3/31
# 功能：批量执行测试用例，并生成Allure测试报告

import os
from pathlib import Path
import shutil
import pytest
from util.time import formattime



class TestRun:
    def test_run_default(self):
        # 测试用例
        case = ["./cases/test_homepage.py"]

        # allure-json存放路径
        allure_json = "result/"
        if not os.path.exists(allure_json):
            os.makedirs(allure_json)


        #allure-report存放路径，生成时间目录
        # base_report_path = 'report/'
        # report_path = Path(base_report_path,'Report'+formattime("%Y%m%d-%H%M"))
        # if not os.path.exists(report_path):
        #     os.makedirs(report_path)


        # 定义PyTest运行参数
        param_list = ["-s", "-v", "-rA", "--alluredir={}".format(allure_json),'--clean-alluredir']
        param_list.extend(case)

        # 执行用例，并生成测试报告
        pytest.main(param_list)
        #将environment.properties文件添加到result目录下
        if os.path.exists('environment.properties'):
            shutil.copy('environment.properties',os.path.join(allure_json,'environment.properties'))

        #将categories.json文件添加到result目录下
        if os.path.exists('categories.json'):
            shutil.copy('categories.json',os.path.join(allure_json,'categories.json'))

        #生成allure报告
        #os.system("allure generate {} -o {} --clean".format(allure_json,report_path))


if __name__ == '__main__':
    TestRun().test_run_default()
