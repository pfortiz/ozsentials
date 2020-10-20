import subprocess

def memUsage(pid):
    __name__ = "memUsage:"
#    cmd = ["ps", "-p {}".format(pid), "u"]
#    cmd3 = ["ps", " --help", "all".format(pid)]
    cmd2 = ["ps -u --pid {}".format(pid)]
    proc = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
    lines = proc.stdout.readlines()
    parts = lines[-1].split()
    return float(parts[3])

