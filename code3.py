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
    p_name.set('')
    p_id.set('')
    gender.set('')
    age.set('')
    disease.set('')
    doctor.set('')
    phone.set('')
    address.set('')
    blood.set('')
    checkin.set('')
    checkout.set('')
    room_no.set('')
    room_type.set('')
    price.set('')

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
    messagebox.showinfo('Saved','Patient Saved')

def open1():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = NONE
    else:
        root.title(os.path.basename(file) + "HMS")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def add():
    text.delete('1.0',END)
    text.insert(END,"\t        Details")
    text.insert(END, f"\n Patient Name:{p_name.get()}")
    text.insert(END, f"\n Patient Id:{p_id.get()}")
    text.insert(END, f"\n Gender:{gender.get()}")
    text.insert(END, f"\n Age:{age.get()}")
    text.insert(END, f"\n Disease:{disease.get()}")
    text.insert(END, f"\n Phone:{phone.get()}")
    text.insert(END, f"\n Address:{address.get()}")
    text.insert(END, f"\n Check-In:{checkin.get()}")
    text.insert(END, f"\n Check-Out:{checkout.get()}")
    text.insert(END, f"\n Room No.:{room_no.get()}")
    text.insert(END, f"\n Room Type:{room_type.get()}")
    text.insert(END, f"\n Price:{price.get()}")
    text.insert(END, f"\n Blood:{blood.get()}")
    text.insert(END, f"\n Doctor:{doctor.get()}")
    text.insert(END, f"\n --------------------------------------------")
    text.insert(END, f"\n \t Thanks to Visit Us")



root=Tk()

root.geometry('500x500')

lbl=Label(root,text='Patient Admit',bg='red',font='arial 23 bold').pack(fill=X)

f1=Frame(root,bd=3,relief=GROOVE,bg='cyan')
f1.place(x=3,y=60,width=500,height=580)

p_name_lbl=Label(f1,text='Patient Name',font='georgia 10 bold',bg='cyan').place(x=2,y=10)
p_id_lbl=Label(f1,text='Patient ID',font='georgia 10 bold',bg='cyan').place(x=2,y=50)
gender_lbl=Label(f1,text='Gender',font='georgia 10 bold',bg='cyan').place(x=2,y=90)
age_lbl=Label(f1,text='Age',font='georgia 10 bold',bg='cyan').place(x=2,y=130)
phone_lbl=Label(f1,text='Phone',font='georgia 10 bold',bg='cyan').place(x=2,y=170)
address_lbl=Label(f1,text='Address',font='georgia 10 bold',bg='cyan').place(x=2,y=210)
disease_lbl=Label(f1,text='Disease',font='georgia 10 bold',bg='cyan').place(x=2,y=250)
checkin_lbl=Label(f1,text='Check In',font='georgia 10 bold',bg='cyan').place(x=2,y=290)
blood_lbl=Label(f1,text='Blood Group',font='georgia 10 bold',bg='cyan').place(x=2,y=330)
docname_lbl=Label(f1,text='Doctor Name',font='georgia 10 bold',bg='cyan').place(x=2,y=370)
checkout_lbl=Label(f1,text='Check Out',font='georgia 10 bold',bg='cyan').place(x=2,y=410)
room_lbl=Label(f1,text='Room No',font='georgia 10 bold',bg='cyan').place(x=2,y=450)
rtype_lbl=Label(f1,text='Room Type',font='georgia 10 bold',bg='cyan').place(x=2,y=490)
price_lbl=Label(f1,text='Price',font='georgia 10 bold',bg='cyan').place(x=2,y=530)

p_name=StringVar()
p_id=StringVar()
gender=StringVar()
age=IntVar()
phone=IntVar()
address=StringVar()
disease=StringVar()
checkin=IntVar()
checkout=IntVar()
blood=StringVar()
doctor=StringVar()
room_no=IntVar()
room_type=StringVar()
price=IntVar()

p_name_entry=Entry(f1,textvariable=p_name).place(x=190,y=10)
p_id_entry=Entry(f1,textvariable=p_id).place(x=190,y=50)
gender = ttk.Combobox(f1, width=17, textvariable=gender, state='readonly')
gender['values'] = ('Male', 'Female', 'Others')
gender.current(0)
gender.place(x=190,y=90)
age_entry=Entry(f1,textvariable=age).place(x=190,y=130)
phone_entry=Entry(f1,textvariable=phone).place(x=190,y=170)
address_entry=Entry(f1,textvariable=address).place(x=190,y=210)
disease_entry=Entry(f1,textvariable=disease).place(x=190,y=250)
checkin_entry=Entry(f1,textvariable=checkin).place(x=190,y=290)
blood_entry=Entry(f1,textvariable=blood).place(x=190,y=330)
docname_entry=Entry(f1,textvariable=doctor).place(x=190,y=370)
checkout_entry=Entry(f1,textvariable=checkout).place(x=190,y=410)
room_entry=Entry(f1,textvariable=room_no).place(x=190,y=450)
room_type = ttk.Combobox(f1, width=17, textvariable=room_type, state='readonly')
room_type['values'] = ('General Ward','Private')
room_type.current(0)
room_type.place(x=190,y=490)
price_entry=Entry(f1,textvariable=price).place(x=190,y=530)

b1=Button(root,text='Exit',relief=GROOVE,bg='red',command=exit1).place(x=600,y=200,width=100)
b2=Button(root,text='Clear',relief=GROOVE,bg='red',command=clear).place(x=600,y=300,width=100)
b3=Button(root,text='Add',relief=GROOVE,bg='red',command=add).place(x=600,y=400,width=100)

f2=Frame(root,relief=GROOVE,bd=3)
f2.place(x=800,y=50,width=400,height=440)

lbl=Label(f2,text='Receipt',font='georgia 20 bold',bg='red').pack(fill=X)

scroll_y=Scrollbar(f2,orient=VERTICAL)
text=Text(f2,yscrollcommand=scroll_y.set)
file=NONE
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=text.yview)
text.pack(pady=3)

b1=Button(f2,text='Save',relief=GROOVE,bg='cyan',command=savefile).place(x=2,y=0)
b2=Button(f2,text='Open',relief=GROOVE,bg='cyan',command=open1).place(x=60,y=0)

root.mainloop()