from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
import cv2
from detect import getprofile
import time
from sms import email_alert

class ReportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #====title====
        title=Label(self.root,text="View Student Result",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

        #====Search=====
        self.var_search=StringVar()


        lbl_select=Label(self.root,text="Roll No",font=("goudy old style",20,"bold"),bg="white").place(x=200,y=100)
        txt_select=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20),bg="lightyellow").place(x=320,y=100,width=150)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=480,y=100,width=100,height=35)
        
        #====detect image========
        lbl_detect=Label(self.root,text="Detect Face",font=("goudy old style",20,"bold"),bg="white").place(x=600,y=100)
        self.btn_image=Button(self.root,text='Capture',font=("goudy old style",15,"bold"),bg="lightyellow",fg="black",cursor="hand2",command=self.detectcam)
        self.btn_image.place(x=750,y=100,width=150,height=35)

        #======result_labels======
        lbl_roll=Label(self.root,text="Roll No",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=180,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=330,y=230,width=150,height=50)
        lbl_standard=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=480,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Scored",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=630,y=230,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Total Marks",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=780,y=230,width=150,height=50)
        lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=930,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=180,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=330,y=280,width=150,height=50)
        self.standard=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.standard.place(x=480,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=630,y=280,width=150,height=50)
        self.full_marks=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full_marks.place(x=780,y=280,width=150,height=50)
        self.percentage=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.percentage.place(x=930,y=280,width=150,height=50)

        #====Button Delete======
        # btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=450,y=350,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=550,y=350,width=100,height=35)


    def search(self):
        con=sqlite3.connect(database="srms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                cur.execute("select * from student where roll=?",(self.var_search.get(),))
                row1=cur.fetchone()
                if row!=None and row1!=None:
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.standard.config(text=row1[7])
                    self.marks.config(text=row[3])
                    self.full_marks.config(text=row[4])
                    self.percentage.config(text=row[5])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def detectcam(self):
        facedetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cam=cv2.VideoCapture(0)
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("recognizer/trainingdata.yml")
        flag=1
        while(flag==1):
            ret,img=cam.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=facedetect.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,conf=recognizer.predict(gray[y:y+h,x:x+w])
                profile=getprofile(id)
                # print(profile,conf)
                if(profile!=None):
                    if(conf >=70):
                        messagebox.showerror("Error","No record found",parent=self.root)
                        time.sleep(10)
                        flag=0
                        break;
                    else:
                        con=sqlite3.connect(database="srms.db")
                        cur=con.cursor()
                        cur.execute("select * from result where roll=?",(id,))
                        row=cur.fetchone()
                        cur.execute("select * from student where roll=?",(id,))
                        row1=cur.fetchone()
                        if row!=None:
                            self.roll.config(text=row[1])
                            self.name.config(text=row1[1])
                            self.standard.config(text=row1[7])
                            self.marks.config(text=row[3])
                            self.full_marks.config(text=row[4])
                            self.percentage.config(text=row[5])
                            flag=0
                            subject=str(row1[7])
                            marks=str(row[3])
                            details = "Marks you scored in " + subject +" is "+ marks + " / " + row[4]
                            mailid = row1[2]
                            email_alert("Marks Scored",details,mailid)
                            break;

                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    flag=0
                    break;

            cv2.imshow("FACE",img);
            if(cv2.waitKey(10)==ord('q')):
                break;
        
        cam.release()
        cv2.destroyAllWindows()

    def clear(self):
        self.roll.config(text="")
        self.name.config(text="")
        self.standard.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")

if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()