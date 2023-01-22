import yaml
import json

from BonsaiClient import BonsaiClient

class BonsaiConfigLoader:
    def __init__(self, config_name='config.yaml'):
        with open(config_name, 'r') as file:
            self.config = yaml.load(file, Loader=yaml.Loader)


    def __repr__(self):
        return json.dumps(self.config, indent=2)

    def create(self):
        for exporter in self.config['exporters']:
            self.config['exporters'][exporter]['class'] = getattr(getattr(__import__("exporters." + exporter), exporter), exporter)

        exporters = []
        for exporter in self.config['exporters']:
            exporters.append(self.config['exporters'][exporter]['class'](opt=self.config['exporters'][exporter]['options']))
            print("Initialized Exporter", exporter)

        certfile = None
        if('certificate' in self.config):
            certfile = self.config['certificate']

        return BonsaiClient(self.config['bonsai_server'], 
                            jobname=self.config['jobname'], 
                            rate=self.config['rate'], 
                            exporters=exporters, 
                            labels=self.config['labels'],
                            certfile=certfile
                            )

