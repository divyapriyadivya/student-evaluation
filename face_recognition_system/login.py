from tkinter import*
from tkinter import ttk,messagebox
import os

class LoginClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1530x700+0+0")
        self.root.config(bg="#021e2f")
        
        #======Frame======
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="Login Here",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=300,y=50)

        email=Label(login_frame,text="USERNAME",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=140)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        password=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=240)
        self.txt_password=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=250,y=280,width=350,height=35)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",18,"bold"),bg="#B00857",fg="white").place(x=350,y=360,width=150,height=40)



    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "username and password required",parent=self.root)
        else:
            username="admin"
            password="admin@123"
            if self.txt_email.get()!="admin" or self.txt_password.get()!="admin@123":
                messagebox.showerror("Error","Invalid username and password",parent=self.root)
                os.system("pyhon login.py")
                
            elif self.txt_email.get()==username and self.txt_password.get()==password:
                self.root.destroy()
                os.system("python main.py")


if __name__=="__main__":
    root=Tk()
    obj=LoginClass(root)
    root.mainloop()


    



    
        




 






        