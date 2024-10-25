# Mac Address Changer 

import subprocess # for more info https://docs.python.org/3/library/subprocess.html

#subprocess.call("ifconfig", shell=True)# show present network card present 
subprocess.call(["ipconfig"]) #This new list method for limit the user input command (User will not hijack the program by the list method)
print("Choose your network card !!")

networkcard = input("Enter your Network card name: ") # select you network card for example wlan0 eth0 etc

#subprocess.call(f"ifconfig {networkcard} down", shell=True) # system command using subprocess (change ip for if for linux)
subprocess.call(["ifconfig", networkcard,"down"]) #(User will not hijack the program by the list method)

Macaddress = input("Enter your custom Mac Address: ")

#subprocess.call(f"ifconfig {networkcard} hw ether {Macaddress}", shell=True)
subprocess.call(["ifconfig", networkcard, "hw", "ether", Macaddress]) #(User will not hijack the program by the list method)

#subprocess.call(f"ifconfig {networkcard} up", shell=True)
subprocess.call(["ifconfig", networkcard, "up"]) #(User will not hijack the program by the list method) limit user input 

print(f"Mac address successfully changed!! {Macaddress}")





