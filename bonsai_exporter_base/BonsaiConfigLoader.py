import yaml
import json

class BonsaiConfigLoader:
    def __init__(self, config_name='config.yaml'):
        with open(config_name, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.Loader)


    def __repr__(self):
        return json.dumps(self.config, indent=2)