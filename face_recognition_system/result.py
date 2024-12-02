from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
import sqlite3

class ResultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #====title====
        title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=50)

        #=====Widgets====
        #=====Variables====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_standard=StringVar()
        self.var_marks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_list=[]
        self.fetch_roll()


        lbl_select=Label(self.root,text="Select student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_obtained=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy ols style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=180)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=120,height=30)


        txt_name=Entry(self.root,textvariable=self.var_name,font=("gougy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=160,width=330)
        txt_standard=Entry(self.root,textvariable=self.var_standard,font=("gougy old style",20,"bold"),bg="lightyellow",state='readonly').place(x=280,y=220,width=330)
        txt_marks_obtained=Entry(self.root,textvariable=self.var_marks,font=("gougy old style",20,"bold"),bg="lightyellow").place(x=280,y=280,width=330)
        txt_full_marks=Entry(self.root,textvariable=self.var_fullmarks,font=("gougy old style",20,"bold"),bg="lightyellow").place(x=280,y=340,width=330)

        #====Button=====
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=400,width=120,height=35)
        btn=clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="white",cursor="hand2",command=self.clear).place(x=430,y=400,width=120,height=35)

        #=====image=====
        self.bg_img=Image.open("images/result.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)


    def fetch_roll(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append([row[0]])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            cur.execute("select name,standard from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_standard.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already exist",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_fullmarks.get())
                    cur.execute("insert into result(roll,name,marks_ob,full_marks,per) values(?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_marks.get(),
                        self.var_fullmarks.get(),   
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_standard.set("")
        self.var_marks.set("")
        self.var_fullmarks.set("")


if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()