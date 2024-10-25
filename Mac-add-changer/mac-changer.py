# Mac Address Changer 

import subprocess # for more info https://docs.python.org/3/library/subprocess.html

subprocess.call("ifconfig", shell=True) # show present network card present 

print("Choose your network card !!")

networkcard = input("Enter your Network card name: ") # select you network card for example wlan0 eth0 etc

subprocess.call(f"ifconfig {networkcard} down", shell=True) # system command using subprocess (change ip for if for linux)

Macaddress = input("Enter your custom Mac Address: ")

subprocess.call(f"ifconfig {networkcard} hw ether {Macaddress}", shell=True)

subprocess.call(f"ifconfig {networkcard} up", shell=True)



