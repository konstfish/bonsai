from BonsaiClient import BonsaiClient
import importlib
from BonsaiConfigLoader import BonsaiConfigLoader

import sys, getopt

if __name__ == "__main__":
    # read command arguments
    config = 'config.yaml'
    opts, args = getopt.getopt(sys.argv[1:],"hc:",["help","config="])
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print ('main.py --config <path to config>')
            sys.exit()
        elif opt in ("-c", "--config"):
            config = arg

    # read config file
    b = BonsaiConfigLoader(config_name=config)

    # create exporter using config file
    exporter = b.create()
