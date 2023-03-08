import docker
from exporters.BonsaiExporter import BonsaiExporter

class BonsaiExporterDOCKER(BonsaiExporter):
    def __init__(self, name="DOCKER", opt={}):
        super().__init__(name)
        self.opt = {}

        self.opt.update(opt)

        self.client = docker.from_env()


    def get_metrics(self):
        metrics = {
            "containers": {}
        }

        for container in self.client.containers.list():
            metrics["containers"][container.name] = {
                "status": container.status
            }
            stats = container.stats(stream=False)
            metrics["containers"][container.name]["cpu_percent"] = stats['cpu_stats']['cpu_usage']['total_usage'] / stats['cpu_stats']['system_cpu_usage'] * 100
            metrics["containers"][container.name]["memory_usage"] = stats['memory_stats']['usage']

        return metrics
        