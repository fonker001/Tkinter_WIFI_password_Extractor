#Tkinter-based GUI application for extracting and displaying WiFi passwords on a Windows system.


#importing tkinter module
from tkinter import *

#importing pyperclip to copy the extracted password to the clipboard
import pyperclip

#creating tkinter window
root = Tk()

#providing geometry to tkinter window
root.geometry("450x350")

#setting the background colour of the tkinter window
root.configure(bg="lime")

#to make the tkinter window unresizable
root.resizable(False,False)

#Providing title to tkinter window
root.title("EXECUTER")

#creating an object of type StringVar(): it will accept String text only
pass_details = StringVar()


#creating an empty list
myList = []

# it is the function to define the see_wifi_pass
def see_wifi_pass():

    #importing subprocess module: helps to create new processes.
    import subprocess

    #defining myList as a global variable
    global myList

    #this will get the output like netsh,wlan,show,profiles and then decode it in 'utf- 
    #8' format,removes the backspaces and store the final output into 'data'
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf- 8').split('\n')
    
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
        'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            myList.append(i)
            myList.append("--")
            myList.append(results[0])
            myList.append("")
        except IndexError:
            myList.append(i)
            myList.append("--")
            myList.append("")


#Defining function "show_wifi_pass"
def show_wifi_pass():
    pass_details.set(myList)

#defining function "copytoclipboard
def copytoclipboard():
    #stores the obtained password using get() i.e pass_details into password.
    password = pass_details.get()
    pyperclip.copy(password)

#creating label and packing it using pack() method
Label(root, text="EXECUTER",bg="lime", font="Helvetica 35 bold").place(x=100,y=30)


#Creating button for "Initiate the process"
Button(root, text="EXTRACT",cursor="hand2",bg='red', font="Helvetica 12 bold" , command=see_wifi_pass).place(x=180,y=100)

#Creating button for "Show all WIFI details"
Button(root, text="Show WIFI details",bg='yellow', font="Helvetica 12 bold" , command=show_wifi_pass).place(x=150,y=140)

Entry(root, textvariable=pass_details, width=65, borderwidth=10 ).place(x=20,y=180,height=50)

#Creating button for ""COPY to CLIPBOARD"
button = Button(root, text="COPY to CLIPBOARD",bg='blue', font="Helvetica 12 bold",command=copytoclipboard).place(x=140,y=250)

Label(root, text="fonker001",bg="lime", font="Helvetica 10 bold").place(x=5,y=330)


#running the main application
root.mainloop()