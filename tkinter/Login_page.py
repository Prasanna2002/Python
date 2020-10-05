import tkinter as tk
import string
class Login_page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login Page')
        self.config(bg='purple')
        self.geometry('450x300')
        
        self.head_line=tk.Label(self,text='LOGIN HERE',fg='white',bg='purple',compound=tk.CENTER,pady=40)
        self.entername=tk.Label(self,text='Enter Your Name ',fg='white',bg='purple',padx=27,pady=7)
        self.password=tk.Label(self,text='Password ',fg='white',bg='purple')

        self.name_entry=tk.Entry(self,width=40,fg='white',bg='purple')
        self.password_entry=tk.Entry(self,width=40,fg='white',bg='purple',show='*')

        self.login_btn=tk.Button(self,relief=tk.GROOVE,text='Login',fg='white',bg='purple',padx=5,pady=5,command=self.login_success)
        self.clear_btn=tk.Button(self,relief=tk.GROOVE,text='Clear',fg='white',bg='purple',padx=5,pady=5,command=self.clear_scrn)

        self.thanku=tk.Label(self,text='LOGIN SUCCESSFULL !',fg='Blue',bg='purple')
        
        self.head_line.grid(row=0,column=0,columnspan=2,rowspan=2)

        self.entername.grid(row=2,column=0)
        self.password.grid(row=3,column=0)
        
        self.name_entry.grid(row=2,column=1)
        self.password_entry.grid(row=3,column=1)

        self.login_btn.grid(row=6,column=1,columnspan=1,pady=20)
        self.clear_btn.grid(row=7,column=1,columnspan=1)
        

    def login_success(self):
        if len(self.name_entry.get())>2 and len(self.password_entry.get())>8:
            if self.name_entry.get()[0] in string.punctuation or self.name_entry.get()[0]==' ':
                self.error=tk.Label(self,text="Name Must Start with a Character",fg='Red',bg='purple')
                self.error.grid(row=8,column=1,columnspan=2)
            else:
                print(self.name_entry.get());print(self.password_entry.get())
                self.name_entry.delete(0,tk.END);self.password_entry.delete(0,tk.END)
                self.thanku.grid(row=8,column=1,columnspan=2)
        else:
            self.error=tk.Label(self,text="Invalid Name or Password\nPassword must be Greater than Eight",fg='Red',bg='purple')
            self.error.grid(row=8,column=1,columnspan=2)

    def clear_scrn(self):
        self.name_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
       
               
s=Login_page()
s.mainloop()
