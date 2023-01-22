from BonsaiClient import BonsaiClient
import importlib
from BonsaiConfigLoader import BonsaiConfigLoader


if __name__ == "__main__":
    b = BonsaiConfigLoader()
    exporter = b.create()

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