from tkinter import *

def button_registration_clicked():
    print(u"Registration started!")
    top_registration = Toplevel()
    top_registration.title("Registration")
    top_registration.geometry('280x250+50+100')

    label_login = Label(top_registration, height=1, width=20, font='Arial 10', text="Enter your login")
    label_login.pack()
    label_login.place(relx=0.15, rely=0.01)
    text_login = Text(top_registration, height=1, width=15, font='Arial 10', wrap=WORD)
    text_login.pack()
    text_login.place(relx=0.25, rely=0.11)

    label_password = Label(top_registration, height=1, width=20, font='Arial 10', text="Enter your password")
    label_password.pack()
    label_password.place(relx=0.15, rely=0.21)
    text_password = Text(top_registration, height=1, width=15, font='Arial 10', wrap=WORD)
    text_password.pack()
    text_password.place(relx=0.25, rely=0.31)

    label_password_confirm = Label(top_registration, height=1, width=20, font='Arial 10', text="Confirm password")
    label_password_confirm.pack()
    label_password_confirm.place(relx=0.15, rely=0.41)
    text_password_confirm = Text(top_registration, height=1, width=15, font='Arial 10', wrap=WORD)
    text_password_confirm.pack()
    text_password_confirm.place(relx=0.25, rely=0.51)

    label_email = Label(top_registration, height=1, width=20, font='Arial 10', text="Enter your email")
    label_email.pack()
    label_email.place(relx=0.15, rely=0.61)
    text_email = Text(top_registration, height=1, width=25, font='Arial 10', wrap=WORD)
    text_email.pack()
    text_email.place(relx=0.12, rely=0.71)

    button_registration = Button(top_registration, height=1, width = 12, bg="#32CD32", text=u"Registration")#, command=button_registration_clicked)
    button_registration.pack()
    button_registration.place(relx=0.28, rely=0.87)

    top_registration.mainloop()


