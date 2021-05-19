from tkinter import *
import parser

root = Tk()

root.title("Calculator")
entry = Entry(root)
entry.grid(row=0,columnspan=6,sticky=W+E)

i=0
def fun(num): # inserting number in text box
    global i
    entry.insert(i,num)
    i += 1

def clear_all(): # clear all
    entry.delete(0,END)

def undo(): # undo numbers
    str=entry.get()
    if len(str):
        new_str = str[:-1]
        clear_all()
        entry.insert(0,new_str)
    else:
        clear_all()
        entry.insert(0,"error")

def get_operator(opr):
    global i
    length = len(opr)
    entry.insert(i,opr)
    i += length

def calculation():
    str = entry.get()
    try:
        a = parser.expr(str).compile()
        result = eval(a)
        clear_all()
        entry.insert(0,result)
    except Exception:
        clear_all()
        entry.insert(0,"error")
    

# creating buttons
Button(root,text="AC",command=lambda:clear_all()).grid(row=2,column=0)
Button(root,text=" ( ",command=lambda:get_operator('(')).grid(row=2,column=2)
Button(root,text=" ) ",command=lambda:get_operator(')')).grid(row=2,column=3)
Button(root,text=" 1 ",command=lambda:fun(1)).grid(row=3,column=0)
Button(root,text=" 2 ",command=lambda:fun(2)).grid(row=3,column=1)
Button(root,text=" 3 ",command=lambda:fun(3)).grid(row=3,column=2)
Button(root,text=" 4 ",command=lambda:fun(4)).grid(row=4,column=0)
Button(root,text=" 5 ",command=lambda:fun(5)).grid(row=4,column=1)
Button(root,text=" 6 ",command=lambda:fun(6)).grid(row=4,column=2)
Button(root,text=" 7 ",command=lambda:fun(7)).grid(row=5,column=0)
Button(root,text=" 8 ",command=lambda:fun(8)).grid(row=5,column=1)
Button(root,text=" 9 ",command=lambda:fun(9)).grid(row=5,column=2)
Button(root,text=" 0 ",command=lambda:fun(0)).grid(row=6,column=0)
Button(root,text="PI",command=lambda:get_operator('*3.14')).grid(row=6,column=1)
Button(root,text=" = ",command=lambda:calculation()).grid(row=6,column=2)
Button(root,text="EXP",command=lambda:get_operator('EXP')).grid(row=3,column=3)
Button(root,text="undo",command=lambda:undo()).grid(row=3,column=4)
Button(root,text=" % ",command=lambda:get_operator('%')).grid(row=4,column=3)
Button(root,text="  *  ",command=lambda:get_operator('*')).grid(row=4,column=4)
Button(root,text="  +  ",command=lambda:get_operator('+')).grid(row=5,column=3)
Button(root,text="  /  ",command=lambda:get_operator('/')).grid(row=5,column=4)
Button(root,text="   -   ",command=lambda:get_operator('-')).grid(row=6,column=3)
Button(root,text="^2",command=lambda:get_operator('**2')).grid(row=6,column=4)








root.mainloop()