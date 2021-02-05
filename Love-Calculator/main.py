from tkinter import ttk  
import tkinter
from tkinter import *
from tkinter import messagebox
root=tkinter.Tk()
root.geometry("330x400+350+300")
root.resizable(0,0)
root.title('MatchCalc')
root.iconbitmap(r'icon1.ico')

#heading---
lb=Label(root,text='Match Finder',height=1,width=20,
         font=('sans-serif',25,'bold'),bg="grey",fg="orange")
lb.pack(pady=5)
ae = Label(root,text='@CopyRight',height=1,width=30,
         font=('sans-serif',15,),bg="grey",fg="orange")
ae.pack(side=BOTTOM,pady=1)

#--------------------------------------------
def calc():
	a = lb2.get()  #a=lb2.get()
	b = lb4.get()  #b=lb4.get()

	li=[]
	c = set(a)
	print("c:",c)

	le=[]
	q = set(b)
	print("q :",q)

	f = c.intersection(q)
	print(f)

	if len(f)==0:
		tkinter.messagebox.showinfo(title="MatchCalc", message="Invalid")
		

	elif len(f)==1:
                
		tkinter.messagebox.showinfo(title="MatchCalc", message="your match percentage is 20%")

	elif len(f)==2:
		tkinter.messagebox.showinfo(title="MatchCalc", message="your match percentage is 40%")

	elif len(f)==3:
		tkinter.messagebox.showinfo(title="MatchCalc", message="your match percentage is 60%")

	elif len(f)==4:
	    tkinter.messagebox.showinfo(title="MatchCalc", message="your match percentage is 80%")

	elif len(f)==5:
	    tkinter.messagebox.showinfo(title="MatchCalc", message="your match percentage is 100%")

	else:
	    tkinter.messagebox.showinfo(title="MatchCalc", message="Invalid Input")


def reset_btn():
	lb2.delete(first=0,last=100)
	lb4.delete(first=0,last=100)
	

#-----------------------------------
lbe=Label(root,text="Enter First Name "+u"\u2193",bg="grey",fg="orange",font=("bold"),width=50)
lbe.pack(pady=5)
btnrow1=Frame(root)
btnrow1.pack(expand=False,fill = 'both',)

lb1 = Label(btnrow1,text='Enter Name',font=('sans-serif',15),
         relief=GROOVE,border=0)

lb1.pack(side=LEFT,expand=False,fill='both',)

lbe=Label(root,text="Enter Second Name "+u"\u2193",bg="grey",fg="orange",font=("bold"),width=50)
lbe.pack(pady=5)
#--------
d=StringVar()
lb2=Entry(btnrow1,text='',font=('sans-serif',15),bg='black',fg='white',
         textvariable=d)
lb2.pack(expand=False,fill = 'both',padx=5,pady=15)

#---------------------------------------------------
btnrow2=Frame(root)
btnrow2.pack(expand=False,fill = 'both',)

lb3 = Label(btnrow2,text='Enter name',font=('sans-serif',15),
         relief=GROOVE,border=0)
lb3.pack(side=LEFT,expand=False,fill='both',)
#--------
d=StringVar()
lb4=Entry(btnrow2,text='',font=('sans-serif',15),bg='black',fg='white',
         textvariable=d)
lb4.pack(side=LEFT,expand=False,fill = 'both',padx=8,pady=15)

#--------------------------------------------------


ef = Label(root,text="wait for results .!",bg="grey",fg = "orange",font=("bold"),width=50)
ef.pack(pady=5)
btn = Button(root,text='Submit',bg="orange",command=calc)
btn.pack(pady=10,padx=70,side=LEFT)

#------------------------------------------------------------

btn = Button(root,text='Reset',bg="orange",command=reset_btn)
btn.pack(pady=10,padx=20,side=LEFT)


root.mainloop()

#btn1=Button(btnrow1,text='1',font=('sans-serif',25),
#            relief=GROOVE,border=0,command=btn1_isclicked,)
#btn1.pack(side=LEFT,expand=False,fill='both',)
