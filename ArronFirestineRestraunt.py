# Arron Firestine            Date of Completion 7/21/2024
# Class SDEV 140             Module 08 Final Project GUI
# This code is a GUI that will be used for a touch screen cash register. It will allow the user to pick dishes and how many of said dishes and
# calculate the total, taxes, and subtotal. 

from tkinter import * # inporting all from tkinter and getting a messagebox 
from tkinter import messagebox

#I like to call it main more than root. 
main=Tk() 
main.geometry("1350x450") # geting the starting size
main.title("Arron Firestine Restaurant") # Name of title of the GUI

#  Creating the header frame
header = Frame (main, width = 1350 , height = 100, bd= 12, relief = "sunken" ) # I really like the look of sunken 
header.pack (side=TOP) # This puts the header at the top of the GUI
title= Label(header, font=("time", 40 ), text="Arron Firestine Restaurant of Fun and Imagination Menu") # This put the text in the header and my favorite font is time new roman
title.grid( row = 0, column = 0) # This puts the text in row 0 and column 0 

# Created a main frame to go below the header and take up all the space to put three frames those three frames are left, middle, and Right
Bottommainframe = Frame (main, width= 1350 , height = 450) 
Bottommainframe.pack(side=BOTTOM)
Leftframe = Frame (Bottommainframe, width = 350 , height = 450, relief = "groove", bd= 10, ) 
Leftframe.pack (side=LEFT)
Middleframe = Frame (Bottommainframe, width = 350 , height = 450, relief = "groove", bd= 10,) # I experimented with relief and I liked all of them having groove 
Middleframe.pack (side=LEFT)
Rightframe = Frame (Bottommainframe, width = 350 , height = 450, relief = "groove", bd= 10, )
Rightframe.pack (side=RIGHT)

# blank variable that will be used as the Checkbutton values and they are set to off. 
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

# Left frame variable values 
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

# Middle frame variable values 
variabletaxes = StringVar()
variabletaxes.set("0")
variableTotal = StringVar()
variableTotal.set("0")
variableSubtotal = StringVar()
variableSubtotal.set("0")

# Right frame variable values 
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

# defining function 
# This will exit the GUI
def exitthing():
    x = messagebox.askyesno("Goodbye", "Do you want to leave the program?") # Creating a message box just in case the user misclicks
    if x:
        main.quit()

# This sets all the values back to 0 which restart the ordering system
def Restartprogram():
    x = messagebox.askyesno("Restarting", "Do you want to restart the Bill?") #Creating a message box just in case the user misclicks
    if x:
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
        variableSubtotal.set("0")
        variableTotal.set("0")
        variabletaxes.set("0")
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
        textSubtotal.config(state = DISABLED)
        texttaxes.config(state=DISABLED)

# These are the sides check button functions when clicked will change state to normal and when clicked again it will change state to disabled
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

# These are the mainmeal check button functions when clicked will change state to normal and when clicked again it will change state to disabled
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

# totalcost function this will take all the values form sides and mainmeals and convert them to a float and add all of them up
def totalcost():
    x = messagebox.askyesno("Total", "Is the customers order finished?") # Creating a message box just in case the user misclicks
    if x:    
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
        total = (meal1 * 3.5 + meal2 * 3.5 + meal3 * 4 + meal4 * 5.25 + meal5 * 5 + meal6 * 9.99
                       + meal7 * 16.99 + meal8 * 8.99 + meal9 * 12.99 + meal10 * 8.99)
        
        # After they are all added up that is the subtotal
        variableSubtotal.set(total)

        # This calculates the tax 
        tax = total * 0.07 # You can change the sales tax per state by changing the 0.07. 0.07 is for Indinia sales taxs
        cleantax = ("%.2f" % tax) # This rounds the tax to two decimal places
        variabletaxes.set(cleantax)

        # The calcuates the total
        newtotal = total + tax # adding taxes to the subtotal gets you the total
        cleannewtotal = ("%.2f" % newtotal) # This rounds the newtotal to two decimal places
        variableTotal.set(cleannewtotal)

    

#left frame
sidestitle= Label(Leftframe, font=("time", 20, "bold" ), text="                Sides                 ") # Main lable of the left frame that will be at the top
sidestitle.grid( row = 0, column = 0)

# For each side there is going to be a checkbutton and entry. 
sides1 = Checkbutton(Leftframe, text = "french fries  3.50$", variable=variable1, onvalue=1, # This has the price and the name of the side and seting up the onvalue and the off value
                     offvalue = 0, font=("time", 14, ), command = Aside1).grid(row = 1, column = 0, sticky=W)# All the sides are sticky to the west and they all go up by 1 for each row and if click the command runs. 
textsides1 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides1,# the textvariable will be the same as valuesides so what ever is typed into the text box will set the value of the sides
                    width = 4, justify = "center", state= DISABLED) # It starts off as disabled but clicking the button will set it to normal. Justify center set things in the entry box to the center of it.
textsides1.grid(row = 1 , column= 1) # all the text entry boxes will be in column 1 and go up by 1 for each row
#nothing chnages except the rows, text, textvariable, and the variable
sides2 = Checkbutton(Leftframe, text = "tater tots  3.50$", variable=variable2, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Bside2).grid(row = 2, column =0, sticky=W)
textsides2 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides2,
                    width = 4, justify = "center", state= DISABLED)
textsides2.grid(row = 2 , column= 1)

sides3 = Checkbutton(Leftframe, text = "apple sauce  4.00$", variable=variable3, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Cside3).grid(row = 3, column =0, sticky=W)
textsides3 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides3,
                    width = 4, justify = "center", state= DISABLED)
textsides3.grid(row = 3 , column= 1)

sides4 = Checkbutton(Leftframe, text = "salad  5.25$", variable=variable4, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Dside4).grid(row = 4, column =0, sticky=W)
textsides4 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides4,
                    width = 4, justify = "center", state= DISABLED)
textsides4.grid(row = 4 , column= 1)

sides5 = Checkbutton(Leftframe, text = "cheese dip  5.00$", variable=variable5, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Eside5).grid(row = 5, column =0, sticky=W)
textsides5 = Entry(Leftframe, font=("time", 14, ), textvariable = valuesides5,
                    width = 4, justify = "center", state= DISABLED)
textsides5.grid(row = 5 , column= 1)

# I do this to even out the frames so they look the same size
blankspace = Label(Leftframe, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
blankspace.grid(row = 6 , column = 0)


# middle Frame
middletitle= Label(Middleframe, font=("time", 20, "bold" ), text = "                  Bill                  ")# Main lable of the middle frame that will be at the top
middletitle.grid( row = 0, column = 0)

# Thiss label will show the text and be in row 1 column 0 and be sticky to the north. I made it sticky to the north to because I think it looks better in the middle.
Total = Label(Middleframe , font=("time", 14,), text = "Total").grid(row = 1, column = 0, sticky=N) 
texttotal = Entry(Middleframe , font=("time", 14,), width = 8 , state = DISABLED, # I made the width twice the size of the other entry because it deals with bigger number.
                   textvariable = variableTotal, justify = "center")# I set all of the entry boxes to disable so people can't ever mess with them directly. 
texttotal.grid(row = 1, column = 1) # It will also display the variableTotal once the Total button is clicked. The entry is dispayed right next to the label. 
# Subtotal and taxes are similarly structured but the row goes up by 1. The differences are the text, rows, and textvariable. 
Subtotal = Label(Middleframe , font=("time", 14,), text = "SubTotal").grid(row = 2, column = 0, sticky=N)
textSubtotal = Entry(Middleframe , font=("time", 14,), width = 8 , state= DISABLED, 
                   textvariable = variableSubtotal, justify = "center")
textSubtotal.grid(row = 2, column = 1)

taxes = Label(Middleframe , font=("time", 14,), text = "Taxes").grid(row = 3, column = 0, sticky=N)
texttaxes = Entry(Middleframe , font=("time", 14,), width = 8 , state= DISABLED, 
                   textvariable = variabletaxes, justify = "center")
texttaxes.grid(row = 3, column = 1)

# Buttons 
# The buttons are located under the labels and entrys of the middle frame. 
Paybutton = Button(Middleframe, padx= 10 , pady= 1, font=("time", 14), # The padx and pady make sure all the buttons are the same size.
                    width=5, text="Total", command = totalcost)  # Once the button is clicked it will run the function totalcost.   
Paybutton.grid(row = 4, column= 0, sticky=N) # Buttons location

Restartbutton = Button(Middleframe, padx= 10 , pady= 1, font=("time", 14), # The padx and pady make sure all the buttons are the same size.
                    width=5, text="Restart", command = Restartprogram) # Once the button is clicked it will run the function Restartprogram. 
Restartbutton.grid(row = 5, column= 0, sticky=N)# Buttons location

Exitbutton = Button(Middleframe, padx= 10 , pady= 1, font=("time", 14), # The padx and pady make sure all the buttons are the same size.
                    width=5, text="Exit", command = exitthing) # Once the button is clicked it will run the function exitthing. 
Exitbutton.grid(row = 6, column= 0, sticky=N)# Buttons location
# I do this to even out the frames so they look the same size
blankspace = Label(Middleframe, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
blankspace.grid(row = 7 , column = 0)

# Right Frame
sidestitle= Label(Rightframe, font=("time", 20, "bold" ), text="                   Mains                 ") # Main lable of the middle frame that will be at the top
sidestitle.grid( row = 0, column = 0)

# For each mainmeals there is going to be a checkbutton and entry. 
mainmeal1 = Checkbutton(Rightframe, text = "Burger  9.99$", variable=variable6, onvalue=1, # This has the price and the name of the mainmeal and seting up the onvalue and the off value
                     offvalue = 0, font=("time", 14, ), command = Amainmeal1).grid(row = 1, column = 0, sticky=W)# All the mainmeals are sticky to the west and they all go up by 1 for each row and if click the command runs to activate or deactivate the Checkbutton.  
textmainmeal1 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain1,# the textvariable will be the same as valuemain so what ever is typed into the text box will set the value of the sides which will be used for calculations. 
                    width = 4, justify = "center", state= DISABLED) # It starts off as disabled but clicking the button will set it to normal.
textmainmeal1.grid(row = 1 , column= 1)# The entry will be to the right of the checkbutton. 
#nothing chnages except the rows, text, textvariable, and the variable
mainmeal2 = Checkbutton(Rightframe, text = "Steak  16.99$", variable=variable7, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Bmainmeal2).grid(row = 2, column = 0, sticky=W)
textmainmeal2 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain2,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal2.grid(row = 2 , column= 1)

mainmeal3 = Checkbutton(Rightframe, text = "Sub  8.99$", variable=variable8, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Cmainmeal3).grid(row = 3, column = 0, sticky=W)
textmainmeal3 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain3,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal3.grid(row = 3 , column= 1)

mainmeal4 = Checkbutton(Rightframe, text = "Pork Chop  12.99$", variable=variable9, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Dmainmeal4).grid(row = 4, column = 0, sticky=W)
textmainmeal4 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain4,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal4.grid(row = 4 , column= 1)

mainmeal5 = Checkbutton(Rightframe, text = "Chicken  8.99$", variable=variable10, onvalue=1,
                     offvalue = 0, font=("time", 14, ), command = Emainmeal5).grid(row = 5, column = 0, sticky=W)
textmainmeal5 = Entry(Rightframe, font=("time", 14, ), textvariable = valuemain5,
                    width = 4, justify = "center", state= DISABLED)
textmainmeal5.grid(row = 5 , column= 1)
# I do this to even out the frames so they look the same size
blankspace = Label(Rightframe, text = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
blankspace.grid(row = 6 , column = 0)


mainloop() # This run the program
