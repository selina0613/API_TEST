import os
import configparser

config_path = os.path.join( os.path.dirname(__file__), '..', 'conf/config.ini') #获取文件路径

cfg = configparser.ConfigParser()
cfg.read(config_path, encoding='UTF-8')
print(cfg.get('default', 'URL'))
print(cfg.get('path', 'CASE_DATA_PATH'))