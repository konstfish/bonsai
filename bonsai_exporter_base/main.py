from BonsaiClient import BonsaiClient
import importlib
from BonsaiConfigLoader import BonsaiConfigLoader

import sys, getopt

if __name__ == "__main__":
    config = 'config.yaml'
    opts, args = getopt.getopt(sys.argv[1:],"hc:",["help","config="])
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print ('main.py --config <path to config>')
            sys.exit()
        elif opt in ("-c", "--config"):
            config = arg

    b = BonsaiConfigLoader(config_name=config)
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