#config/config_manager.py
import yaml
import os

class ConfigManager:
    @staticmethod
    def get_config():
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
