from tkinter import *
from tkinter import messagebox as tmsg

def login():
    if username.get()=='Taniv' and password.get()=='Tanivgoyal1808':
        tmsg.showinfo('Welcome','Hey! Thanks to login')
        root.destroy()
        import code2
    else:
        tmsg.showerror('Error','User mismatch')


def exit():
    op=tmsg.askyesno('Exit','Are you sure to exit?')
    if op>0:
        root.destroy()

root=Tk()

root.geometry('500x500')

root.title('Hospital Management System')

l1=Label(root,text='Hospital Management',font='georgia 43 bold',bg='red').pack(fill=X)

f1=Frame(root,relief=GROOVE,bg='gold',bd=3)
f1.place(width=300,height=200,x=600,y=200)
lbl1=Label(f1,text='LOGIN',font='georgia 20 bold',fg='red',bg='gold').place(x=110,y=10)

username=StringVar()
password=StringVar()

user_label=Label(f1,text='USERNAME',font='georgia 10 bold',bg='gold').place(x=2,y=70)
pass_label=Label(f1,text='PASSWORD',font='georgia 10 bold',bg='gold').place(x=2,y=100)

user_entry=Entry(f1,textvariable=username).place(x=110,y=70)
pass_entry=Entry(f1,show='*',textvariable=password).place(x=110,y=100)

button=Button(f1,text='Login',command=login,bg='red').place(x=80,y=150)
button=Button(f1,text='Exit',command=exit,bg='red').place(x=170,y=150,width=40)

root.mainloop()