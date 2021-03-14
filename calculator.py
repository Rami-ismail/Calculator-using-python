from tkinter import*
from tkinter import ttk
expression=''
def press(num):
    global expression
    expression=expression+num
    equation.set(expression)
def clear():
    global expression
    expression=''
    equation.set("")
def calculate():
    global expression
    equation.set(eval(expression))
    expression=''
    
    

window=Tk()
window.title('Calculator')
Ecran=ttk.LabelFrame(window,text='Ecran')
Ecran['padding']=(50,50)
Ecran.grid(row=1,column=1)
frame=ttk.LabelFrame(Ecran,text='Bouttons')
frame.grid(row=1,column=0)
texte1=ttk.Label(frame)

texte1.grid(row=0,column=1)
equation=StringVar()
texte=ttk.Entry(Ecran,textvariable=equation)
texte.grid(row=0,column=0)
button1=Button(frame,text='1',fg='black',bg='white',command=lambda:press('1'),height=1,width=7)
button1.grid(row=2,column=0)

button2=Button(frame,text='2',fg='black',bg='white',command=lambda:press('2'),height=1,width=7)
button2.grid(row=2,column=1)

button3=Button(frame,text='3',fg='black',bg='white',command=lambda:press('3'),height=1,width=7)
button3.grid(row=2,column=2)

buttonplus=Button(frame,text='+',fg='black',bg='white',command=lambda:press('+'),height=1,width=7)
buttonplus.grid(row=2,column=3)
                  
button4=Button(frame,text='4',fg='black',bg='white',command=lambda:press('4'),height=1,width=7)
button4.grid(row=3,column=0)

button5=Button(frame,text='5',fg='black',bg='white',command=lambda:press('5'),height=1,width=7)
button5.grid(row=3,column=1)
button6=Button(frame,text='6',fg='black',bg='white',command=lambda:press('6'),height=1,width=7)
button6.grid(row=3,column=2)
buttonminus=Button(frame,text='-',fg='black',bg='white',command=lambda:press('-'),height=1,width=7)
buttonminus.grid(row=3,column=3)
button7=Button(frame,text='7',fg='black',bg='white',command=lambda:press('7'),height=1,width=7)
button7.grid(row=4,column=0)
button8=Button(frame,text='8',fg='black',bg='white',command=lambda:press('8'),height=1,width=7)
button8.grid(row=4,column=1)
button9=Button(frame,text='9',fg='black',bg='white',command=lambda:press('9'),height=1,width=7)
button9.grid(row=4,column=2)
buttonmultiply=Button(frame,text='*',fg='black',bg='white',command=lambda:press('*'),height=1,width=7)
buttonmultiply.grid(row=4,column=3)
button0=Button(frame,text='0',fg='black',bg='white',command=lambda:press('0'),height=1,width=7)
button0.grid(row=5,column=0)
buttonclear=Button(frame,text='clear',fg='black',bg='blue',command=clear,height=1,width=7)
buttonclear.grid(row=5,column=1)
buttonequal=Button(frame,text='=',fg='black',bg='white',command=calculate,height=1,width=7)
buttonequal.grid(row=5,column=2)
buttondivide=Button(frame,text='/',fg='black',bg='white',command=lambda:press('/'),height=1,width=7)
buttondivide.grid(row=5,column=3)

window.mainloop()
