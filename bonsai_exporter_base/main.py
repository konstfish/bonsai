from BonsaiClient import BonsaiClient
import importlib
from BonsaiConfigLoader import BonsaiConfigLoader

b = BonsaiConfigLoader()

print(b)

for exporter in b.config['exporters']:
    b.config['exporters'][exporter]['class'] = getattr(getattr(__import__("exporters." + exporter), exporter), exporter)

if __name__ == "__main__":
    exporters = []
    for exporter in b.config['exporters']:
        exporters.append(b.config['exporters'][exporter]['class'](opt=b.config['exporters'][exporter]['options']))
        print("Initialized Exporter", exporter)

    BonsaiClient(b.config['bonsai_server'], jobname=b.config['jobname'], rate=b.config['rate'], exporters=exporters)


"""
from exporters.BonsaiExporterCPU import BonsaiExporterCPU
from exporters.BonsaiExporterMEM import BonsaiExporterMEM
from exporters.BonsaiExporterNET import BonsaiExporterNET
from exporters.BonsaiExporterDISK import BonsaiExporterDISK
"""

"""
BonsaiClient(b.config['bonsai_server'], jobname=b.config['jobname'], rate=b.config['rate'], exporters=[

    BonsaiExporterCPU(opt={
        "individual_cores": True,
        "core_count": True,
        "core_count_logical": False
    }),
    BonsaiExporterMEM(opt={
        "include_swap": False,
        "detailed": True
    }),
    BonsaiExporterNET(opt={
        "interfaces": ["ensdfs0"]
    }),
    BonsaiExporterDISK(opt={
        "disks": ['/'],
        "detailed": True
    }),
])
"""