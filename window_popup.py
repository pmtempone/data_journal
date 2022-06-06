#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

def guardar_dato():
    valor = str(entry.get())
    with open('prueba_tinker.txt', 'w') as f:
        for line in valor:
            f.write(line)
            #f.write('\n')
    
valor=''
#Create a Button to validate Entry Widget
#ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)
ttk.Button(win, text= "Okay",width= 20, command= guardar_dato).pack(pady=20)
