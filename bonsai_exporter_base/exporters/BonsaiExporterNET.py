import psutil
from exporters.BonsaiExporter import BonsaiExporter

# network exporter class implemeting psutil
class BonsaiExporterNET(BonsaiExporter):
    def __init__(self, name="NET", opt={}):
        super().__init__(name)
        self.opt = {
            "interfaces": []
        }

        self.opt.update(opt)


    def get_metrics(self):
        metrics = {}
        stat = psutil.net_io_counters(pernic=True)
        for interface in self.opt["interfaces"]:
            if(interface in stat):
                metrics[interface] = {}
                metrics[interface]["bytes_sent"] = stat[interface].bytes_sent
                metrics[interface]["bytes_recv"] = stat[interface].bytes_recv

        return metrics

    
    