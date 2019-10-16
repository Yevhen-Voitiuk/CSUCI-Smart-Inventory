import subprocess
import tkinter

def on_press(self):
    print(self.ciTag.get())

#Decode the serial number from the result of command line
serialNumber = subprocess.check_output('wmic bios get serialnumber').decode().split('\n')[1].strip()

#Decode the username...as all campus username start with domain, isolate the actual username
userName = subprocess.check_output('whoami').decode().split('\\')[1].strip()

#Decode computer name and computer model in the same fashion
computerName = subprocess.check_output('hostname').decode().split('\n')[0].strip()
computerModel = subprocess.check_output('wmic computersystem get model').decode().split('\n')[1].strip()

#Construct a window
mainWindow = tkinter.Tk()
mainWindow.title("CSUCI Inventory Questionnaire")
mainWindow.geometry("500x500")
mainWindow.resizable(0, 0)

#Display computer name
computerNameLabel = tkinter.Label(mainWindow, text="Computer Name: ")
computerNameLabel.grid(row=0, column=0, sticky="W")
computerNameLabelDisplay = tkinter.Label(mainWindow, text=computerName)
computerNameLabelDisplay.grid(row=0, column=1, sticky="W")

#Display computer model
computerModelLabel = tkinter.Label(mainWindow, text="Computer Model: ")
computerModelLabel.grid(row=1, column=0, sticky="W")
computerModelLabelDisplay = tkinter.Label(mainWindow, text=computerModel)
computerModelLabelDisplay.grid(row=1, column=1, sticky="W")

#Display serial number
serialNumberLabel = tkinter.Label(mainWindow, text="Serial Number: ")
serialNumberLabel.grid(row=2, column=0, sticky="W")
serialNumberLabelDisplay = tkinter.Label(mainWindow, text=serialNumber)
serialNumberLabelDisplay.grid(row=2, column=1, sticky="W")

#Display username
userNameLabel = tkinter.Label(mainWindow, text="Username: ")
userNameLabel.grid(row=3, column=0, sticky="W")
userNameLabelDisplay = tkinter.Label(mainWindow, text=userName)
userNameLabelDisplay.grid(row=3, column=1, sticky="W")

#Display CI Tag and Room Number fields with entry boxes
tkinter.Label(mainWindow, text="CI Tag: ").grid(row=4, column=0, sticky="W")
tkinter.Label(mainWindow, text="Room Number: ").grid(row=5, column=0, sticky="W")
ciTag = tkinter.Entry(mainWindow)
roomNumber = tkinter.Entry(mainWindow)
ciTag.grid(row=4, column=1, sticky="W")
roomNumber.grid(row=5, column=1, sticky="W")

listOfDivisions = tkinter.Listbox(mainWindow, width=20, height=10, font=("Helvetica", 12))
listOfDivisions.insert(0, "O_OTHER")
listOfDivisions.insert(1, "AA - Academic Affairs")
listOfDivisions.insert(2, "BFA - Business and Financial Affairs")
listOfDivisions.insert(3, "OOP - Office of the President")
listOfDivisions.insert(4, "SA - Student Affairs")
listOfDivisions.insert(5, "TI - Technology and Innovation")
listOfDivisions.insert(6, "UA - University Advancement")

listOfDivisions.grid(row=6, column=1)

scrollbar = tkinter.Scrollbar(mainWindow, orient="vertical")
scrollbar.config(command=listOfDivisions.yview)
scrollbar.grid(sticky="E")

listOfDivisions.config(yscrollcommand=scrollbar.set)

isShared = None
tkinter.Checkbutton(mainWindow, text="Shared Computer?", variable=isShared).grid(row=7, column=1, sticky="W")
if isShared:
    assignedUser = userName

ConfirmButton = tkinter.Button(mainWindow, text="Confirm", command=mainWindow.destroy)
ConfirmButton.grid(row=8, column=0)

mainWindow.mainloop()