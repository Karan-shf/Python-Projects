from tkinter import *

panjere = Tk()

neveshte = StringVar()

# matn = 'welcome to the site'

def add():
    a = int(form.get())
    b = int(form2.get())
    c = a + b
    neveshte.set(f'Result: {c}')

def subtract():
    a = int(form.get())
    b = int(form2.get())
    c = a - b
    neveshte.set(f'Result: {c}')

def multiply():
    a = int(form.get())
    b = int(form2.get())
    c = a * b
    neveshte.set(f'Result: {c}')

def devide():
    a = int(form.get())
    b = int(form2.get())
    c = a / b
    neveshte.set(f'Result: {c}')


panjere.title('calculator')

panjere.geometry('300x300')

panjere.resizable(width=False,height=False)

lab = Label(panjere,textvariable=neveshte)
lab.place(x=20,y=110)

form = Entry(panjere)
form.place(x=20,y=20)

form2 = Entry(panjere)
form2.place(x=20,y=50)

dokme = Button(panjere,text='+',command=lambda:add())
dokme.place(x=20,y=80)

dokme2 = Button(panjere,text='-',command=lambda:subtract())
dokme2.place(x=70,y=80)

dokme3 = Button(panjere,text='x',command=lambda:multiply())
dokme3.place(x=120,y=80)

dokme4 = Button(panjere,text='/',command=lambda:devide())
dokme4.place(x=170,y=80)

panjere.mainloop()