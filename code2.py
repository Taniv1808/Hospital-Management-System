from tkinter import *

def admit():
    import code3

def staffinfo():
    import code4

def app():
    import code5

root=Tk()

root.geometry('500x500')

lbl1=Label(root,text='Cygnus',bg='gold',font='georgia 30 bold').pack(fill=X)

button=Button(root,text='Patient Admit',command=admit,bg='red').place(x=580,y=110,width=150)
button=Button(root,text='Staff Information',command=staffinfo,bg='red').place(x=580,y=160,width=150)
button=Button(root,text='Appointment',command=app,bg='red').place(x=580,y=210,width=150)

lbl2=Label(root,text='STAY SAFE!',font='georgia 30 bold').place(x=580,y=400)
lbl3=Label(root,text='STAY HOME!',font='georgia 30 bold').place(x=630,y=500)

root.mainloop()