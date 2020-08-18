from tkinter import *
def btnClicK(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnCleardisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsnum():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def dmode():
    cal.configure(bg="BLACK")

cal=Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()
cal.configure(bg="White")


text_Dislpay= Entry(cal,font=('arial',20,'bold'), textvariable=text_input,bd=30,insertwidth=4,bg="white",justify='right').grid(columnspan=4)

btn7=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda :btnClicK(7)).grid(row=1,column=0)
btn8=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda :btnClicK(8)).grid(row=1,column=1)
btn9=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda :btnClicK(9)).grid(row=1,column=2)
Addition=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda :btnClicK("+")).grid(row=1,column=3)
btn4=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda :btnClicK(4)).grid(row=2,column=0)
btn5=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda :btnClicK(5)).grid(row=2,column=1)
btn6=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda :btnClicK(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda :btnClicK("-")).grid(row=2,column=3)
btn1=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda :btnClicK(1)).grid(row=3,column=0)
btn2=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda :btnClicK(2)).grid(row=3,column=1)
btn3=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda :btnClicK(3)).grid(row=3,column=2)
Multiply=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda :btnClicK("*")).grid(row=3,column=3)
btn0=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda :btnClicK(0)).grid(row=4,column=0)
btnClear=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=btnCleardisplay).grid(row=4,column=1)
btnEquals=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=btnEqualsnum).grid(row=4,column=2)
Divide=Button(cal,padx=12,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda :btnClicK("/")).grid(row=4,column=3)

rbd=Radiobutton(cal,padx=12,pady=10,text="Dark Mode",value=1,command=dmode)
rbd.place(x=300,y=320)


cal.mainloop()