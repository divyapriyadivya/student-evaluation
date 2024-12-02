from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from student import StudentClass
from result import ResultClass
from report import ReportClass
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1530x700+0+0")
        self.root.config(bg="white")

        #====Title====
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)


        #====Content====

        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=210,y=100,width=920,height=350)

        #====Menus====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=500,width=1320,height=80)
        
        btn_students=Button(M_Frame,text="Student Details",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=150,y=5,width=200,height=40)
        btn_marks=Button(M_Frame,text="Student Marks",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=400,y=5,width=200,height=40)
        btn_results=Button(M_Frame,text="Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.view_report).place(x=650,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)

        #====Footer===
        footer=Label(self.root,text="Result Management System",padx=10,compound=LEFT,font=("goudy old style",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)

    def view_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()