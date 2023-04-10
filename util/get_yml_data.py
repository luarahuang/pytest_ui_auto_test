import yaml
from pathlib import Path
import os
import pytest

class GetYamlData:  
    def get_yaml_data(self):
        #获取yml配置文件的路径
        project_rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(project_rootdir,'config','config.yml')

        #解析yml配置文件
        if not os.path.exists(config_path):
            raise FileNotFoundError("配置文件%s不存在！" % config_path)
        else:
            with open(config_path) as f:
                yaml_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        return yaml_config


if __name__ == '__main__':
    yaml_config = GetYamlData().get_yaml_data()
    print(yaml_config['login_url'])
    print(yaml_config['loginuser']['username'])
