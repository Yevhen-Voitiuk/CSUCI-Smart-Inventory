import subprocess
import tkinter

serialNumber = subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()
print(serialNumber)
userName = subprocess.check_output('whoami').decode().split('\\')[1].strip()
print(userName)
computerName = subprocess.check_output('hostname').decode().split('\n')[0].strip()
print(computerName)
computerModel = subprocess.check_output('wmic computersystem get model').decode().split('\n')[1].strip()
print(computerModel)

#!/usr/bin/python
top = tkinter.Tk()
# Code to add widgets will go here...
L1 = tkinter.Label(top, text="User Name: ")
L1.grid(row=1, column=1, sticky="W")
L2 = tkinter.Label(top, text=userName)
L2.grid(row=1, column=2, sticky="W")
L3 = tkinter.Label(top, text="Serial Number: ")
L3.grid(row=2, column=1, sticky="W")
L4 = tkinter.Label(top, text=serialNumber)
L4.grid(row=2, column=2, sticky="W")

#E1.pack(side = tkinter.RIGHT)
top.mainloop()