from tkinter import *

def button_registration_clicked():
    print(u"Registration started!")
    top_registration = Toplevel()
    top_registration.title("Registration")
    top_registration.mainloop()

    label_height = Label(top_registration,height=1,width=15,font='Arial 10', text = "Enter your height" )
    label_height.pack()
