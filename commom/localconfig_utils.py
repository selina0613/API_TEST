#方式二：
import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', 'conf/config.ini')

class LocalconfigUtils():
    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding='UTF-8')

    @property     #把方法变为属性方法
    def URL(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path', 'CASE_DATA_PATH')
        return case_data_path_value

local_config = LocalconfigUtils()   #创建一个对象

if __name__ == '__main__':
    print(local_config.CASE_DATA_PATH)