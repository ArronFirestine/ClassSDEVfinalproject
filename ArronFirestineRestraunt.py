from tkinter import *
from tkinter import messagebox



main=Tk()
main.geometry("1350x750+0+0")
main.title("Arron Firestine Restraunt")

header = Frame (main, width = 1350 , height = 100, bd= 12, relief = "sunken" )
header.pack (side=TOP)

title= Label(header, font=("time", 40 ), text="Arron Firestine Restraunt of Fun and Imagination Menu")
title.grid( row = 0, column = 0)

Bottommainframe = Frame (main, width= 1350 , height = 100, relief = "raise", bd= 10,)
Bottommainframe.pack(side=BOTTOM)

Leftframe = Frame (Bottommainframe, width = 350 , height = 650, relief = "groove", bd= 10, )
Leftframe.pack (side=LEFT)

Middleframe = Frame (Bottommainframe, width = 350 , height = 650, relief = "ridge", bd= 10,)
Middleframe.pack (side=LEFT)

Rightframe = Frame (Bottommainframe, width = 350 , height = 650, relief = "groove", bd= 10, )
Rightframe.pack (side=RIGHT)


variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()
variable17 = IntVar()
variable18 = IntVar()
variable19 = IntVar()
variable20 = IntVar()
variable21 = IntVar()
variable22 = IntVar()
variable23 = IntVar()

variable1.set(0)
variable2.set(0)
variable3.set(0)
variable4.set(0)
variable5.set(0)
variable6.set(0)
variable7.set(0)
variable8.set(0)
variable9.set(0)
variable10.set(0)

valuesides1 = StringVar()
valuesides1.set("0")
valuesides2 = StringVar()
valuesides2.set("0")
valuesides3 = StringVar()
valuesides3.set("0")
valuesides4 = StringVar()
valuesides4.set("0")
valuesides5 = StringVar()
valuesides5.set("0")

variableChange = StringVar()
variableChange.set("0")
variableTotal = StringVar()
variableTotal.set("0")
variablePayment = StringVar()
variablePayment.set("0")

valuemain1 = StringVar()
valuemain1.set("0")
valuemain2 = StringVar()
valuemain2.set("0")
valuemain3 = StringVar()
valuemain3.set("0")
valuemain4 = StringVar()
valuemain4.set("0")
valuemain5 = StringVar()
valuemain5.set("0")
# Stuff
def exitthing():
    x = messagebox.askyesno("Goodbye", "Do you want to leave the program?")
    if x:
        main.quit()

def Restartprogram():
    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8.set(0)
    variable9.set(0)
    variable10.set(0)
    valuesides1.set("0")
    valuesides2.set("0")
    valuesides3.set("0")
    valuesides4.set("0")
    valuesides5.set("0")
    variableChange.set("0")
    variableTotal.set("0")
    variablePayment.set("0")
    valuemain1.set("0")
    valuemain2.set("0")
    valuemain3.set("0")
    valuemain4.set("0")
    valuemain5.set("0")
    textsides1.config(state= DISABLED)
    textsides2.config(state= DISABLED)
    textsides3.config(state= DISABLED)
    textsides4.config(state= DISABLED)
    textsides5.config(state= DISABLED)
    textmainmeal1.config(state= DISABLED)
    textmainmeal1.config(state= DISABLED)
    textmainmeal2.config(state= DISABLED)
    textmainmeal3.config(state= DISABLED)
    textmainmeal4.config(state= DISABLED)
    textmainmeal5.config(state= DISABLED)
    texttotal.config(state= DISABLED)
    
# sides 
def Aside1():
    if (variable1.get() == 1):
        textsides1.config(state = NORMAL)
        valuesides1.set("0")
    elif(variable1.get() == 0):
        textsides1.config(state = DISABLED)
        valuesides1.set("0")
def Bside2():
    if (variable2.get() == 1):
        textsides2.config(state = NORMAL)
        valuesides2.set("0")
    elif(variable2.get() == 0):
        textsides2.config(state = DISABLED)
        valuesides2.set("0")
def Cside3():
    if (variable3.get() == 1):
        textsides3.config(state = NORMAL)
        valuesides3.set("0")
    elif(variable3.get() == 0):
        textsides3.config(state = DISABLED)
        valuesides3.set("0")
def Dside4():
    if (variable4.get() == 1):
        textsides4.config(state = NORMAL)
        valuesides4.set("0")
    elif(variable4.get() == 0):
        textsides4.config(state = DISABLED)
        valuesides4.set("0")
def Eside5():
    if (variable5.get() == 1):
        textsides5.config(state = NORMAL)
        valuesides5.set("0")
    elif(variable5.get() == 0):
        textsides5.config(state = DISABLED)
        valuesides5.set("0")
# mains
def Amainmeal1():
    if (variable6.get() == 1):
        textmainmeal1.config(state = NORMAL)
        valuemain1.set("0")
    elif(variable6.get() == 0):
        textmainmeal1.config(state = DISABLED)
        valuemain1.set("0")
def Bmainmeal2():
    if (variable7.get() == 1):
        textmainmeal2.config(state = NORMAL)
        valuemain2.set("0")
    elif(variable7.get() == 0):
        textmainmeal2.config(state = DISABLED)
        valuemain2.set("0")
def Cmainmeal3():
    if (variable8.get() == 1):
        textmainmeal3.config(state = NORMAL)
        valuemain3.set("0")
    elif(variable8.get() == 0):
        textmainmeal3.config(state = DISABLED)
        valuemain3.set("0")
def Dmainmeal4():
    if (variable9.get() == 1):
        textmainmeal4.config(state = NORMAL)
        valuemain4.set("0")
    elif(variable9.get() == 0):
        textmainmeal4.config(state = DISABLED)
        valuemain4.set("0")
def Emainmeal5():
    if (variable10.get() == 1):
        textmainmeal5.config(state = NORMAL)
        valuemain5.set("0")
    elif(variable10.get() == 0):
        textmainmeal5.config(state = DISABLED)
        valuemain5.set("0")
# total
def totalcost():
    meal1 = float(valuesides1.get())
    meal2 = float(valuesides2.get())
    meal3 = float(valuesides3.get())
    meal4 = float(valuesides4.get())
    meal5 = float(valuesides5.get())
    meal6 = float(valuemain1.get())
    meal7 = float(valuemain2.get())
    meal8 = float(valuemain3.get())
    meal9 = float(valuemain4.get())
    meal10 = float(valuemain5.get())
    variableTotal.set (meal1 * 3 + meal2 * 3 + meal3 * 4 + meal4 * 5 + meal5 * 5 + meal6 * 10
                       + meal7 * 16 + meal8 * 8 + meal9 * 12 + meal10 * 8)
    

    

# This is all of the left frame
sidestitle= Label(Leftframe, font=("time", 20, "bold" ), text="                Sides                 ")
sidestitle.grid( row = 0, column = 0)

sides1 = Checkbutton(Leftframe, text = "frenchfries  3$", variable=variable1, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Aside1).grid(row = 1, column = 0, sticky=W)
textsides1 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides1,
                    width = 4, justify = "center", state= DISABLED)
textsides1.grid(row = 1 , column= 1)

sides2 = Checkbutton(Leftframe, text = "tatertots  3$", variable=variable2, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Bside2).grid(row = 2, column =0, sticky=W)
textsides2 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides2,
                    width = 4, justify = "center", state= DISABLED)
textsides2.grid(row = 2 , column= 1)

sides3 = Checkbutton(Leftframe, text = "apple sauce  4$", variable=variable3, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Cside3).grid(row = 3, column =0, sticky=W)
textsides3 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides3,
                    width = 4, justify = "center", state= DISABLED)
textsides3.grid(row = 3 , column= 1)

sides4 = Checkbutton(Leftframe, text = "salad  5$", variable=variable4, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Dside4).grid(row = 4, column =0, sticky=W)
textsides4 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides4,
                    width = 4, justify = "center", state= DISABLED)
textsides4.grid(row = 4 , column= 1)

sides5 = Checkbutton(Leftframe, text = "cheese dip  5$", variable=variable5, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Eside5).grid(row = 5, column =0, sticky=W)
textsides5 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides5,
                    width = 4, justify = "center", state= DISABLED)
textsides5.grid(row = 5 , column= 1)

blankspace = Label(Leftframe, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
blankspace.grid(row = 6 , column = 0)

# middle Frame
middletitle= Label(Middleframe, font=("time", 20, "bold" ), text = "                  Bill                  ")
middletitle.grid( row = 0, column = 0)

Total = Label(Middleframe , font=("time", 14,), text = "Total")
Total.grid(row = 3, column = 0, sticky=N)
texttotal = Entry(Middleframe , font=("time", 14,), width = 4 , state= DISABLED, 
                   textvariable = variableTotal, justify = "center")
texttotal.grid(row = 3, column = 1)

# Buttons 
Paybutton = Button(Middleframe, padx= 10 , pady= 1, font=("time", 14),
                    width=5, text="Pay", command=totalcost)
Paybutton.grid(row = 4, column= 0, sticky=N)

Restartbutton = Button(Middleframe, padx= 10 , pady= 1, font=("time", 14),
                    width=5, text="Restart", command = Restartprogram)
Restartbutton.grid(row = 5, column= 0, sticky=N)

Exitbutton = Button(Middleframe, padx= 10 , pady= 1, font=("time", 14),
                    width=5, text="Exit", command = exitthing)
Exitbutton.grid(row = 6, column= 0, sticky=N)

blankspace = Label(Middleframe, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
blankspace.grid(row = 8 , column = 0)


# Right Frame
sidestitle= Label(Rightframe, font=("time", 20, "bold" ), text="                   Mains                 ")
sidestitle.grid( row = 0, column = 0)

mainmeal1 = Checkbutton(Rightframe, text = "Burger  10$", variable=variable6, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Amainmeal1).grid(row = 1, column = 0, sticky=W)
textmainmeal1 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain1,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal1.grid(row = 1 , column= 1)

mainmeal2 = Checkbutton(Rightframe, text = "Steak  16$", variable=variable7, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Bmainmeal2).grid(row = 2, column = 0, sticky=W)
textmainmeal2 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain2,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal2.grid(row = 2 , column= 1)

mainmeal3 = Checkbutton(Rightframe, text = "Sub  8$", variable=variable8, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Cmainmeal3).grid(row = 3, column = 0, sticky=W)
textmainmeal3 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain3,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal3.grid(row = 3 , column= 1)

mainmeal4 = Checkbutton(Rightframe, text = "Pork Chop  12$", variable=variable9, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Dmainmeal4).grid(row = 4, column = 0, sticky=W)
textmainmeal4 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain4,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal4.grid(row = 4 , column= 1)

mainmeal5 = Checkbutton(Rightframe, text = "Chicken  8$", variable=variable10, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Emainmeal5).grid(row = 5, column = 0, sticky=W)
textmainmeal5 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain5,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal5.grid(row = 5 , column= 1)

blankspace = Label(Rightframe, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
blankspace.grid(row = 6 , column = 0)
#






main.mainloop()