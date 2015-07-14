from tkinter import *

def button_authorization_clicked():
    print(u"authorization started!")
    top_authorization = Toplevel(bg="#F0FFFF")
    top_authorization.title("authorization")

    label_login = Label(top_authorization, height=1, width=15, font='Arial 10', bg="#F0FFFF", text="Enter your login")
    label_login.pack()
    label_login.place(relx=0.15, rely=0.07)

    text_login=Text(top_authorization, height=1, width=15, font='Arial 10', wrap=WORD)
    text_login.pack()
    text_login.place(relx=0.20, rely=0.21)

    label_pass = Label(top_authorization, height=1, width=15, font='Arial 10', bg="#F0FFFF", text="Enter your password")
    label_pass.pack()
    label_pass.place(relx=0.15, rely=0.36)

    text_pass=Text(top_authorization, height=1, width=15, font='Arial 10', wrap=WORD)
    text_pass.pack()
    text_pass.place(relx=0.20, rely=0.51)

    button_authorization = Button(top_authorization, bg="#AFEEEE", bd=0, text=u"Authorization")
    button_authorization.pack()
    button_authorization.place(relx=0.26, rely=0.70)

    top_authorization.mainloop()