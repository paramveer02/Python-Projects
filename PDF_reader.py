
import pyttsx3
import PyPDF2
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

bg='#ffdab1'
w=Tk()
w.geometry('450x400')
w.title('Audiobook')
w.configure(bg=bg)
# w.iconbitmap('C:/Users/Paramveer/PycharmProjects/Audiobook/icon.png') [to add icon to the window]

my_image=ImageTk.PhotoImage(Image.open('audiobookimage.png'))
Label(image=my_image,bg=bg).place(relx=1,x=-375,y=50)

Label(w,text='Please enter the page number:',bg=bg,font=('none 20',16)).pack()

page_num=Entry(w,bg=bg)
page_num.place(relx=1,x=-280,y=30)

def click():
    global path
    path=filedialog.askopenfilename()
    print(path)

Button(w,text='OPEN',command=click,bg=bg,width=5,font=('none 20',15)).place(relx=1,x=-270,y=60)

def talk():
    page_n=page_num.get()
    engine=pyttsx3.init()
    book=open(path,'rb')
    pdfreader=PyPDF2.PdfFileReader(book)

    page=pdfreader.getPage(int(page_n))
    text=page.extractText()

    engine.say(text)
    engine.runAndWait()

Button(w,text='TALK',command=talk,bg=bg,width=5,font=('none 20',15)).place(relx=1,x=-300,y=310)
Button(w,text='Exit',command=w.quit,bg=bg,width=5,font=('none 20',15)).place(relx=1,x=-200,y=310)


w.mainloop()






