from tkinter import *
from klase import *
from idlelib.tooltip import Hovertip
main=Tk()

main.title="Password generator"

main.geometry('500x175')
l1=Label(main,text='Number of characters').place(x=10,y=20)
l2=Label(main,text='Upper letters').place(x=10,y=50)
l3=Label(main,text='Numbers').place(x=10,y=80)
l4=Label(main,text='Special charcaters').place(x=10,y=110)

l44=Label(main,text='*', fg='red',font=('Times New Roman',25,'bold'))
l44.place(x=127,y=107)
myTip = Hovertip(l44,'Special characters:\n'+str(punctuation))

e1=Entry(main,width=3)
e1.place(x=152,y=20)
var_upper = BooleanVar()
var_number = BooleanVar()
var_spec = BooleanVar()

c1 = Checkbutton(main, variable = var_upper, onvalue = True, offvalue = False, height=1, width = 2)
c1.place(x=160,y=50)

c2 = Checkbutton(main, variable = var_number, onvalue = True, offvalue = False, height=1, width = 2)
c2.place(x=160,y=80)

c3 = Checkbutton(main, variable = var_spec, onvalue = True, offvalue = False, height=1, width = 2)
c3.place(x=160,y=110)

l5=Label(main,text='Generated password:').place(x=300,y=5)

l6=Label(main,text='', fg='red')
l6.place(x=20,y=150)

pass_str = StringVar()
pass_str.set('')

e2=Entry(main,width=16,textvariable=pass_str,state="readonly")
e2.place(x=300,y=25)

def generate():
    pass_str.set('')
    p.generate([int(e1.get()),var_upper.get(),var_number.get(),var_spec.get()])
    pass_str.set(p)
    e2.config(textvariable=pass_str)

def num_check():
    if e1.get().isdigit():
        if int(e1.get())<3:
            l6.config(text='Password must be atleast 3 characters long.')
        else:
            l6.config(text="")
            generate()
    
    else:
        l6.config(text='First text box requires integer.')

    
b=Button(main,text='Generate password',height=5,command=lambda:num_check())
b.place(x=300,y=65)



mainloop()