import psutil
from exporters.BonsaiExporter import BonsaiExporter

# disk exporter class implemeting psutil
class BonsaiExporterDISK(BonsaiExporter):
    def __init__(self, name="DISK", opt={}):
        super().__init__(name)
        self.opt = {
            "disks": [],
            "detailed": False
        }

        self.opt.update(opt)


    def get_metrics(self):
        metrics = {
        }
        for disk in self.opt["disks"]:
            metrics[disk] = {}
            metrics[disk]["used_percent"] = psutil.disk_usage(disk).percent
            if(self.opt["detailed"]):
                metrics[disk]["used"] = psutil.disk_usage(disk).used
                metrics[disk]["free"] = psutil.disk_usage(disk).free

        return metrics

    
    