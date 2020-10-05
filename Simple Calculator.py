import math
from tkinter import *
d=Tk()
d.title('Simple Calculator')
d.wm_geometry("440x436")
d.configure(bg='black')
e=Entry(d,width=68,borderwidth=5)
e.config(bg='black',fg='white')
e.grid(column=0,columnspan=5,padx=10,pady=10)
#----------------------------------------------------------------------------------------------------------------------------------------
def e_get(num):
    global y,x
    E=e.get()
    e.delete(0,END)
    e.insert(0,str(E)+str(num))
#----------------------------------------------------------------------------------------------------------------------------------------
def _equal():
    if map=='addition':
      try:
         d=float(a)+float(e.get());e.delete(0,END)
         e.insert(0,str(d))
      except:
            e.insert(0,'0')
    elif map=='subtraction':
        try:
           d=float(c)-float(e.get());e.delete(0,END)
           e.insert(0,str(d))
        except:
            e.insert(0,'0')
    elif map=='multiplication':
        try:
            d=float(b)*float(e.get());e.delete(0,END)
            
            e.insert(0,str(d))
        except:
            e.insert(0,'0')
        
    elif map=='division':
        try:
          x=float(z)/float(e.get());e.delete(0,END)
          e.insert(0,str(x))
        except:
            e.delete(0,END)
            e.insert(0,'0')
    
    elif map=='percent':
        try:
          x=float(alpha)/float(e.get())
          e.insert(0,str(x))
        except:
            e.delete(0,END)
            e.insert(0,str(float(alpha)/100))
        
#------------------------------------------------------------------------------------------------------------------------------------------
def addition():
    global a,map
    map='addition'
    a=e.get()
    e.delete(0,END)
def multiplication():
    global b,map
    map='multiplication'
    b=e.get()
    e.delete(0,END)
def subtraction():
    global c,map
    map='subtraction'
    c=e.get()
    e.delete(0,END)
    
def division():
    global z,map
    map='division'
    z=e.get()
    e.delete(0,END)

    
def e_config():
    try:
       x=int(e.get())*-1
       e.delete(0,END)
       e.insert(0,str(x))
    except:
        x=int(0)*-1
        e.delete(0,END)
        e.insert(0,str(x))

def e_div():
    try:
      s=1/float(e.get())
      e.delete(0,END)
      e.insert(0,str(s))
    except:
        e.delete(0,END)
        e.insert(0,'ERROR')

def e_sqr():
    try:
      d=float(e.get())**2
      e.delete(0,END)
      e.insert(0,str(d))
    except:
        d=float(0)**2
        e.delete(0,END)
        e.insert(0,str(d))

def e_sqrt():
    try:
      q=math.sqrt(float(e.get()))
      e.delete(0,END)
      e.insert(0,str(q))
    except:
        q=math.sqrt(0)
        e.delete(0,END)
        e.insert(0,str(q))

def percent():
    global alpha,map
    map='percent'
    alpha=e.get()
    e.delete(0,END)

#-------------------------------------------------------------------------------------------------------------------------------------
b1=Button(d,text='1',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command = lambda:e_get('1'))
b2=Button(d,text='2',padx=46,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('2'))
b3=Button(d,text='3',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('3'))
b4=Button(d,text='4',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('4'))
b5=Button(d,text='5',padx=46,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('5'))
b6=Button(d,text='6',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('6'))
b7=Button(d,text='7',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('7'))
b8=Button(d,text='8',padx=46,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('8'))
b9=Button(d,text='9',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('9'))
b0=Button(d,text='0',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('0'))
b_add=Button(d,text='+',padx=46,pady=20,bg='black',fg='white',relief=GROOVE,command =addition)
b_sub=Button(d,text='-',padx=48,pady=20,bg='black',fg='white',relief=GROOVE,command =subtraction)
b_mul=Button(d,text='X',padx=47,pady=20,bg='black',fg='white',relief=GROOVE,command =multiplication)
b_div=Button(d,text='÷',padx=47,pady=20,bg='black',fg='white',relief=GROOVE,command =division)
b_point=Button(d,text='.',padx=46,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e_get('.'))
b_percent=Button(d,text='%',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =percent)
b_equal=Button(d,text='=',padx=44,pady=20,bg='skyblue',fg='white',relief=GROOVE,command =_equal)
b_CE=Button(d,text='CE',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e.delete(0,END))
b_C=Button(d,text='C',padx=44,pady=20,bg='black',fg='white',relief=GROOVE,command =lambda:e.delete(0,END))
b_sqrt=Button(d,text='^x',padx=42,pady=20,bg='black',fg='white',relief=GROOVE,command =e_sqrt)
b_pow=Button(d,text='x**2',padx=39,pady=20,bg='black',fg='white',relief=GROOVE,command =e_sqr)
b_1=Button(d,text='1/x',padx=39,pady=20,bg='black',fg='white',relief=GROOVE,command =e_div)
b_2=Button(d,text='+/-',padx=39,pady=20,bg='black',fg='white',relief=GROOVE,command =e_config)
b_exit=Button(d,text='EXIT<<',padx=30,pady=20,fg='white',bg='skyblue',relief=GROOVE,command =lambda:d.quit())
#---------------------------------------------------------------------------------------------------------------------------------------------
b_percent.grid(column=0,row=1)
b_CE.grid(column=1,row=1) 
b_C.grid(column=2,row=1)
b_exit.grid(column=3,row=1)
b_1.grid(column=0,row=2)
b_pow.grid(column=1,row=2)
b_sqrt.grid(column=2,row=2)
b_div.grid(column=3,row=2)
b1.grid(column=0,row=5)
b2.grid(column=1,row=5)
b3.grid(column=2,row=5)
b4.grid(column=0,row=4)
b5.grid(column=1,row=4)
b6.grid(column=2,row=4)
b7.grid(column=0,row=3)
b8.grid(column=1,row=3)
b9.grid(column=2,row=3)
b_mul.grid(column=3,row=3)
b_add.grid(column=3,row=5)
b_sub.grid(column=3,row=4)
b_2.grid(column=0,row=6)
b0.grid(column=1,row=6)
b_point.grid(column=2,row=6)
b_equal.grid(column=3,row=6)


d.mainloop()
