import configparser

class ConfigUtils():
    def __init__(self,config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path)

    def read_value(self, section, key):
        value = self.cfg.get(section, key)
        return value
