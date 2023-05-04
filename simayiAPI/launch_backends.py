import yaml
from subprocess import Popen

conf_file = yaml.safe_load(open("backend_configuration.yaml"))
procs = []

for k in conf_file:
    folder = conf_file[k]["folder"]
    port = conf_file[k]["port"]
    command = f"python3 backend_node.py {folder} {port}"
    procs.append(Popen(command))

for p in procs:
    p.wait()