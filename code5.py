from tkinter import *
from tkinter import ttk
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import messagebox


def exit1():
    op=messagebox.askyesno('Exit','Are you sure to exit?')
    if op>0:
        root.destroy()
        import code2

def clear():
    name.set('')
    app.set('')
    gender.set('')
    age.set('')
    time.set('')
    phone.set('')
    address.set('')


def savefile():
    global file
    if file == NONE:
        file=asksaveasfilename(initialfile='Untitled',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=NONE
        else:
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"HMS")
            print("File saved")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def open1():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = NONE
    else:
        root.title(os.path.basename(file) + "Record System")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def add():
    text.delete('1.0',END)
    text.insert(END,"\t        Details")
    text.insert(END, f"\n Name:{name.get()}")
    text.insert(END, f"\n Appointment No.:{app.get()}")
    text.insert(END, f"\n Gender:{gender.get()}")
    text.insert(END, f"\n Age:{age.get()}")
    text.insert(END, f"\n Time:{time.get()}")
    text.insert(END, f"\n Phone:{phone.get()}")
    text.insert(END, f"\n Address:{address.get()}")
    text.insert(END, f"\n --------------------------------------------")

root=Tk()

root.geometry('500x500')

lbl=Label(root,text='Appointment List',bg='red',font='arial 23 bold').pack(fill=X)

f1=Frame(root,bd=3,relief=GROOVE,bg='cyan')
f1.place(x=3,y=60,width=500,height=580)

name_lbl=Label(f1,text='Name',font='georgia 10 bold',bg='cyan').place(x=2,y=10)
app_lbl=Label(f1,text='Appointment No.',font='georgia 10 bold',bg='cyan').place(x=2,y=50)
gender_lbl=Label(f1,text='Gender',font='georgia 10 bold',bg='cyan').place(x=2,y=90)
age_lbl=Label(f1,text='Age',font='georgia 10 bold',bg='cyan').place(x=2,y=130)
phone_lbl=Label(f1,text='Phone',font='georgia 10 bold',bg='cyan').place(x=2,y=170)
address_lbl=Label(f1,text='Address',font='georgia 10 bold',bg='cyan').place(x=2,y=210)
time_lbl=Label(f1,text='Time',font='georgia 10 bold',bg='cyan').place(x=2,y=250)

name=StringVar()
app=StringVar()
gender=StringVar()
age=IntVar()
phone=IntVar()
address=StringVar()
time=IntVar()

name_entry=Entry(f1,textvariable=name).place(x=190,y=10)
app_entry=Entry(f1,textvariable=app).place(x=190,y=50)
gender = ttk.Combobox(f1, width=17, textvariable=gender, state='readonly')
gender['values'] = ('Male', 'Female', 'Others')
gender.current(0)
gender.place(x=190,y=90)
age_entry=Entry(f1,textvariable=age).place(x=190,y=130)
phone_entry=Entry(f1,textvariable=phone).place(x=190,y=170)
address_entry=Entry(f1,textvariable=address).place(x=190,y=210)
t_entry=Entry(f1,textvariable=time).place(x=190,y=250)

b1=Button(root,text='Exit',relief=GROOVE,bg='red',command=exit1).place(x=600,y=200,width=100)
b2=Button(root,text='Clear',relief=GROOVE,bg='red',command=clear).place(x=600,y=300,width=100)
b3=Button(root,text='Add',relief=GROOVE,bg='red',command=add).place(x=600,y=400,width=100)

f2=Frame(root,relief=GROOVE,bd=3)
f2.place(x=800,y=50,width=400,height=300)

lbl=Label(f2,text='Appointments',font='georgia 20 bold',bg='red').pack(fill=X)

scroll_y=Scrollbar(f2,orient=VERTICAL)
text=Text(f2,yscrollcommand=scroll_y.set)
file=NONE
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=text.yview)
text.pack(pady=3)

b1=Button(f2,text='Save',relief=GROOVE,bg='cyan',command=savefile).place(x=2,y=0)
b2=Button(f2,text='Open',relief=GROOVE,bg='cyan',command=open1).place(x=55,y=0)

root.mainloop()