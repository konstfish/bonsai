from BonsaiClient import BonsaiClient
from BonsaiExporterCPU import BonsaiExporterCPU
from BonsaiExporterMEM import BonsaiExporterMEM
from BonsaiExporterNET import BonsaiExporterNET
from BonsaiExporterDISK import BonsaiExporterDISK

BonsaiClient("http://10.0.1.108:4000/push", jobname="basic_exporter", rate=0.5, exporters=[
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
        "interfaces": ["en0"]
    }),
    BonsaiExporterDISK(opt={
        "disks": ['/'],
        "detailed": True
    }),
])