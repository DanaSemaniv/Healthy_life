from tkinter import *
import calculations
import recommendations
import authorization
import registration

def button_clicked():
     input_weight = text_weight.get(index1=1.0, index2=END)
     input_height = text_height.get(index1=1.0, index2=END)
     try:
         input_weight = float(input_weight)
         input_height = float(input_height)
     except ValueError:
         input_weight = 0
         input_height = 0
         text_height.delete(0.0,END)
         text_height.insert(0.0,0.0)
         text_weight.delete(0.0,END)
         text_weight.insert(0.0,0.0)
     if input_height > 0:
         perfect_weight = calculations.get_ideal_weight_lorentz(input_height)
         text_perfect_weight.delete(1.0, END)
         text_perfect_weight.insert(END, perfect_weight)
     else:
         print ("Please input your weight")
     if (input_height > 0) & (input_weight > 0):
         bmi = calculations.get_bmi(input_height, input_weight)
         text_BMI.delete(1.0,END)
         text_BMI.insert(END, bmi)
     else:
         print ("Please input your weight and height")

def button_recomendatin_ration_clicked():
    print (u"Recomendation_ration!")

def button_recomendatin_training_clicked():
    print (u"Recomendation_training!")

def exit_(event):
     root.destroy()

root=Tk()
root.title("Healthy_life")
root.geometry('380x300+300+200')

label_height = Label(root,height=1,width=15,font='Arial 10', text = "Enter your height" )
label_height.pack()
label_height.place(relx = 0.01, rely = 0.01)
text_height=Text(root,height=1,width=7,font='Arial 10',wrap=WORD)
text_height.pack()
text_height.place(relx = 0.1, rely = 0.07)

label_weight = Label(root,height=1,width=15,font='Arial 10', text = "Enter your weight" )
label_weight.pack()
label_weight.place(relx = 0.01, rely = 0.15)
text_weight=Text(root,height=1,width=7,font='Arial 10',wrap=WORD)
text_weight.pack()
text_weight.place(relx = 0.1, rely = 0.21)

button_calculate = Button(root, bg="red", text=u"Calculate!", command=button_clicked)
button_calculate.pack()
button_calculate.place(relx  = 0.4, rely = 0.27)
#button_calculate.bind("Button", button_clicked)

label_perfect_weight = Label(root,height=1,width=15,font='Arial 10', text = "Your perfect weight" )
label_perfect_weight.pack()
label_perfect_weight.place(relx = 0.01, rely = 0.37 )
text_perfect_weight=Text(root,height=1,width=7,font='Arial 10',wrap=WORD)
text_perfect_weight.pack()
text_perfect_weight.place(relx = 0.1, rely = 0.43)

# Вивід BMI - індекс маси тіла
label_BMI = Label(root,height=1,width=15,font='Arial 10', text = "Your BMI" )
label_BMI.pack()
label_BMI.place(relx = 0.01, rely = 0.51)
text_BMI=Text(root,height=1,width=7,font='Arial 10',wrap=WORD)
text_BMI.pack()
text_BMI.place(relx = 0.1, rely = 0.57)

label_sex = Label(root,height=1,width=25,font='Arial 10', text = "Your sex:" )
label_sex.pack()
label_sex.place(relx = 0.51, rely = 0.01)
var=IntVar()
rbutton_sex_man=Radiobutton(root,text='Man',variable=var,value="Man")
rbutton_sex_man.pack()
rbutton_sex_man.place(relx = 0.7, rely = 0.09)
rbutton_sex_woman=Radiobutton(root,text='Woman',variable=var,value="Woman")
rbutton_sex_woman.pack()
rbutton_sex_woman.place(relx = 0.7, rely = 0.17)

button_recomendatin_ration = Button(root, height = 1, width = 8, bg="#5CACEE", text=u"Ration", command=button_recomendatin_ration_clicked)
button_recomendatin_ration.pack()
button_recomendatin_ration.place(relx = 0.7, rely = 0.41)

button_recomendatin_training = Button(root,height = 1, width = 8, bg="#5CACEE", text=u"Training", command=button_recomendatin_training_clicked)
button_recomendatin_training.pack()
button_recomendatin_training.place(relx = 0.7, rely = 0.55)

button_registration = Button(root,height = 1, width = 12, bg="#00FA9A", text=u"Registration", command=registration.button_registration_clicked)
button_registration.pack()
button_registration.place(relx = 0.1, rely = 0.75)

button_authorization= Button(root,height = 1, width = 12, bg="#BDB76B", text=u"Authorization", command=authorization.button_authorization_clicked)
button_authorization.pack()
button_authorization.place(relx = 0.5, rely = 0.75)

root.bind('<Escape>', exit_)
root.mainloop()
