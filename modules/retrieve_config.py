import os
import json


def retrieve_config(filename):
    
    home = os.path.expanduser("~/Desktop/scripts/dyte-vit-2022-rohanailoni")
    path = os.path.join(home, filename)

    if not os.path.exists(path):
        return {}

    f = open(path, "r")
    config = json.load(f)
    f.close()
    
    return config