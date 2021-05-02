from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from translate import Translator
from tkinter.messagebox import *

w=Tk()
w.geometry('550x500')
w.title('Translator')
w.config(bg='black')
w.resizable(0,0)
n=StringVar()

languages=Combobox(w,width=27,textvariable=n)
languages['values']=('-------Select language--------','de')
languages.place(relx=1,x=-535,y=180)

languages.current(0)

Label(w,text='English to German Translator',bg='black',fg='yellow',font=('Roboto',18)).pack()
Label(w,text='Enter text to translate:',bg='black',fg='yellow',font=('Roboto',16)).place(relx=1,x=-535,y=70)

txt=Entry(w,font=('Roboto',13))
txt.place(relx=1,x=-535,y=115,width=300,height=40)

# txt1=Entry(w,font=('Roboto',12))
# txt1.place(relx=1,x=-535,y=350,width=300,height=90)

def retrieve():
    z=txt.get()
    translator=Translator(to_lang='de')
    translation=translator.translate(z)
    Label(w,text=translation,bg='black',fg='yellow',font=('Roboto',18)).place(relx=1,x=-535,y=350)

Label(w,text='Translated Text:',bg='black',fg='yellow',font=('Roboto',18)).place(relx=1,x=-535,y=300)

Button(w,text='Translate',command=retrieve,bg='red',fg='yellow',font=('Roboto',14)).place(relx=1,x=-335,y=240)

w.mainloop()
