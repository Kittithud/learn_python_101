from tkinter import *
from tkinter import ttk # Theme of tk
from tkinter import messagebox

GUI = Tk() # Main display
GUI.title('Note program') # Name of program
GUI.geometry('500x400')# Display size

# Header
L1 = Label(GUI, text = 'My workout routine', font =('Ansana new', 40), fg = 'red')
L1.place(x = 20, y = 20)

# Monday
def Button1():
    text = 'Chest day!!'
    messagebox.showinfo('Today is', text)

FB1 = Frame(GUI)
FB1.place(x = 20, y = 120)
B1 = ttk.Button(FB1, text ='Monday', command = Button1)
B1.pack(ipadx = 10, ipady = 10)

# Tuesday
def Button2():
    text = 'Back day!!'
    messagebox.showinfo('Today is', text)

FB2 = Frame(GUI)
FB2.place(x = 20, y = 170)
B2 = ttk.Button(FB2, text ='Tuesday', command = Button2)
B2.pack(ipadx = 10, ipady = 10)

# Wendesday
def Button3():
    text = 'Arms day!!'
    messagebox.showinfo('Today is', text)

FB3 = Frame(GUI)
FB3.place(x = 20, y = 220)
B3 = ttk.Button(FB3, text ='Wendesday', command = Button3)
B3.pack(ipadx = 10, ipady = 10)

# Thursday
def Button4():
    text = 'Rest day!!'
    messagebox.showinfo('Today is', text)

FB4 = Frame(GUI)
FB4.place(x = 20, y = 270)
B4 = ttk.Button(FB4, text ='Thursday', command = Button4)
B4.pack(ipadx = 10, ipady = 10)

# Friday
def Button5():
    text = 'Rest day!!'
    messagebox.showinfo('Today is', text)

FB5 = Frame(GUI)
FB5.place(x = 20, y = 320)
B5 = ttk.Button(FB5, text ='Friday', command = Button5)
B5.pack(ipadx = 10, ipady = 10)



GUI.mainloop()
