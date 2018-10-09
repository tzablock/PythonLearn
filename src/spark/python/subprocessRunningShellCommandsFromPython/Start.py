import subprocess
# just run command on shell
subprocess.call("ls",shell=True)
# take output of command in shell
output = subprocess.check_output("ls",shell=True)
print("Our output is: ",output)