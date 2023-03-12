# basic exporter class
class BonsaiExporter:
    def __init__(self, name):
        self.name = name

    def get_metrics(self) -> dict:
        raise NotImplementedError
