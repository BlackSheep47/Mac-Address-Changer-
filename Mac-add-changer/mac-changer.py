# Mac Address Changer 

import subprocess # for more info https://docs.python.org/3/library/subprocess.html
subprocess.call("ifconfig eth0 down", shell=True) #system command using subprocess (change ip for if for linux)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)

