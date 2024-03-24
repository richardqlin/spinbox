from tkinter import *

root= Tk()

b1=Button(root,text = ' Value')
b1.grid(row=1,column=0)

b2=Button(root,text = ' Value')
b2.grid(row=1,column=2)

lb1=Label(text='value here', fg='red')
lb1.grid(row=1,column=2)

def show():
    lst= ''
   
    for i in sb:
        lst=lst+i.get() +','
        print(i.get())
    print(lst)
    

sb=[]

def main():
    for i in range(7):
        sbx=Spinbox(root, from_=0,to_=10,width=2)
        sbx.grid(row=i, column=1)
        sb.append(sbx)
    
b1=Button(root,text='Print value', command=show)
b1.grid(row=1, column=0)

main()
