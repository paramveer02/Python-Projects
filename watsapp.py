
import pywhatkit as watsapp
from tkinter import *
from tkinter import ttk
import tkinter as tk


w=Tk()
w.geometry('450x350')
w.title('Params Automated Watsapp')
w.config(bg='yellow')
w.resizable(0,0)

nb=ttk.Notebook(w)
nb.pack(expand=1,fill=BOTH)

fr1=tk.Frame(nb,bg='yellow')
nb.add(fr1,text='Messaging')

fr=tk.Frame(nb,bg='red')
nb.add(fr,text='Youtube')

Label(fr1,text='Automated Watsapp',bg='yellow',fg='black',font=('Roboto',18)).pack()
Label(fr,text='Automated Youtube',bg='Red',fg='black',font=('Roboto',18)).pack()

Label(fr1,text='Enter Number:',bg='yellow',fg='black',font=('Roboto',16)).place(relx=1,x=-380,y=120)
Label(fr1,text='Enter Message:',bg='yellow',fg='black',font=('Roboto',16)).place(relx=1,x=-380,y=150)
Label(fr1,text='Enter Time in hours:',bg='yellow',fg='black',font=('Roboto',14)).place(relx=1,x=-425,y=195)
Label(fr1,text='Enter Time in minutes:',bg='yellow',fg='black',font=('Roboto',14)).place(relx=1,x=-425,y=225)
Label(fr,text='Enter Youtube URL: ',bg='red',fg='black',font=('Roboto',16)).place(relx=1,x=-410,y=115)

num=Entry(fr1,width=20)
num.place(relx=1,x=-225,y=125)

msg=Entry(fr1,width=24,font=('Roboto',13))
msg.place(relx=1,x=-225,y=155,height=27)

hr=Entry(fr1,width=20)
hr.place(relx=1,x=-225,y=200)

mi=Entry(fr1,width=20)
mi.place(relx=1,x=-225,y=230)

u=Entry(fr,width=27)
u.place(relx=1,x=-215,y=120)

def send():
    n=num.get()
    m=msg.get()
    hrs=int(hr.get())
    mins=int(mi.get())

    watsapp.sendwhatmsg(n,m,hrs,mins)
    watsapp.playonyt(url)

n=StringVar()
m=StringVar()

def yt():
    url=u.get()
    watsapp.playonyt(url)

Button(fr,text='Play',command=yt,bg='red',fg='black',font=('Roboto',14)).place(relx=1,x=-270,y=170)

Button(fr1,text='Send',command=send,bg='yellow',fg='black',font=('Roboto',14)).place(relx=1,x=-270,y=270)

w.mainloop()
