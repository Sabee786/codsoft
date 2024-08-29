import tkinter
from  tkinter import *
c=Tk()
c.title("calculator")
c.geometry("570x600+100+200")
c.resizable(False,False)
c.configure(bg="#17161b")
equation=" "

def show(value):
    global equation
    equation+=value
    res.config(text=equation)
def clear():
    global equation
    equation=""
    res.config(text=equation)
def calculate():
    global equation
    r=""
    if equation !="":
        try:
            r=eval(equation)
        except:
            r="error"
            euqtion=""
    res.config(text=r)

res=Label(c,width=25,height=2, text="" ,font=("arial",30,))
res.pack()
Button(c,text="c",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(c,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('/')).place(x=150,y=100)
Button(c,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('%')).place(x=290,y=100)
Button(c,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('*')).place(x=430,y=100)
Button(c,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('9')).place(x=10,y=200)
Button(c,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('8')).place(x=150,y=200)
Button(c,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('7')).place(x=290,y=200)
Button(c,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('-')).place(x=430,y=200)
Button(c,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('6')).place(x=10,y=300)
Button(c,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('5')).place(x=150,y=300)
Button(c,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('4')).place(x=290,y=300)
Button(c,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('+')).place(x=430,y=300)
Button(c,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('3')).place(x=10,y=400)
Button(c,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('2')).place(x=150,y=400)
Button(c,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('1')).place(x=290,y=400)
Button(c,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('0')).place(x=10,y=500)
Button(c,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show('.')).place(x=290,y=500)
Button(c,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#f74087",command=lambda:calculate( )).place(x=430,y=400)
c.mainloop()
