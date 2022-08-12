import psutil


class BonsaiExporterCPU:
    def __init__(self, name="CPU", opt={}):
        self.name = name
        self.opt = {
            "individual_cores": False,
            "core_count": False,
            "core_count_logical": True
        }

        self.opt.update(opt)


    def get_metrics(self):
        metrics = {
            "percent": psutil.cpu_percent(),
        }

        if(self.opt["individual_cores"]):
            metrics["individual_cores"] = psutil.cpu_percent(percpu=True)
        
        if(self.opt["core_count"]):
            metrics["core_count"] = psutil.cpu_count(logical=self.opt["core_count_logical"])

        return metrics

    
    