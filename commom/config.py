import os
from commom.config_utils import ConfigUtils

config_path = os.path.join( os.path.dirname(__file__), '..', 'conf/config.ini') #获取文件路径

configUtils = ConfigUtils(config_path)

URL = configUtils.read_value('default', 'URL')
CASE_DATA_PATH = configUtils.read_value('xpath', 'CASE_DATA_PATH')