import psutil
from exporters.BonsaiExporter import BonsaiExporter

class BonsaiExporterMEM(BonsaiExporter):
    def __init__(self, name="MEM", opt={}):
        super().__init__(name)
        self.opt = {
            "include_swap": False,
            "detailed": False
        }

        self.opt.update(opt)


    def get_metrics(self):
        metrics = {
            "percent": psutil.virtual_memory().percent,
        }

        
        if(self.opt["detailed"]):
            metrics["mem_used"] = psutil.virtual_memory().used
            metrics["mem_free"] = psutil.virtual_memory().free
            
            if(self.opt["include_swap"]):
                metrics["swap_percent"] = psutil.swap_memory().percent
                metrics["swap_used"] = psutil.swap_memory().used
                metrics["swap_free"] = psutil.swap_memory().free

        return metrics

    
    