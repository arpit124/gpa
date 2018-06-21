from tkinter import *
from tkinter import messagebox

window = Tk()
#ent0=range(20)
n=0
i=0
sum1=0
crsum=0
sum2=0.0

def sgpasum1():
    grade=(sum2/crsum)
    x="Your CGPA is "+str(grade)
    messagebox.showinfo('Your CGPA', x)

def ext1():
    lbl5=Label(window, text="Enter Semester You Have Passed Last : ")
    lbl5.grid(row=0, column=1)
    ent1=Entry(window)
    ent1.grid(row=0, column=2)
    def cal1():
        global n
        if(i==0):
            n=int(ent1.get())
        ent2=Entry(window)
        ent2.grid(row=(i+2), column=2)    
        lbl3=Label(window, text="Enter "+str(i+1)+" Semester SGPA : ")
        lbl3.grid(row=(i+2),column=1)
        ent3=Entry(window)
        ent3.grid(row=(i+2),column=4)
        lbl4=Label(window, text="Enter Credit Of The Semester : ")
        lbl4.grid(row=(i+2),column=3)
        def cont1():
            global sum2, crsum,i
            mark1=float(ent2.get())
            cr=int(ent3.get())
#            print(type(sum1),type(pt),type(cr))
            sum2+=(mark1*cr)
            crsum+=cr
            print(str(sum2)+"\t"+str(crsum)+"\t"+str(mark1))
            i=i+1
            if(i<n):
                btn3 = Button(window, text="Proceed", command=cal1)
                btn3.grid(column=6, row=i+1)
            else:
                btn3 = Button(window, text="Submit", command=sgpasum1)
                btn3.grid(column=6, row=i+1)

        btn3 = Button(window, text="Save", command=cont1)
        btn3.grid(column=5, row=i+2)
##        if(i==n-1):
##            btn4 = Button(window, text="Submit", command=sgpasum)
##            btn4.grid(column=5,row=i+2)

##    def sgpa():
##        
##        lbl2=Label(window, text="Enter Subject Marks : ")
##        lbl2.grid(row=1,column=2)

        
##        btn4 = Button(window, text="Submit", command=sgpasum)
##        btn4.grid(column=3, row=n+2)


    btn3 = Button(window, text="Next", command=cal1)
    btn3.grid(column=3, row=0)

def sgpasum():
    tot=crsum*10
    grade=(sum1/tot)*10
    x="Your SGPA ,Credit Points and total Credit is "+str(grade)+str(sum1)+str(crsum)
    messagebox.showinfo('Your SGPA', x)
def ext():
    lbl1=Label(window,text="Enter Number Of Subjects")
    lbl1.grid(row=0, column=1)
    ent1=Entry(window)
    ent1.grid(row=0, column=2)
    def cal():
        global n
        if(i==0):
            n=int(ent1.get())
        ent2=Entry(window)
        ent2.grid(row=(i+2), column=2)    
        lbl3=Label(window, text="Enter "+str(i+1)+" Subject Marks : ")
        lbl3.grid(row=(i+2),column=1)
        ent3=Entry(window)
        ent3.grid(row=(i+2),column=4)
        lbl4=Label(window, text="Enter Credit Of The Subject : ")
        lbl4.grid(row=(i+2),column=3)
        def cont():
            global sum1, crsum,i
            mark=int(ent2.get())
            if(mark>=90 and mark<=100):
                pt=10
            elif(mark>=80 and mark<=90):
                pt=9
            elif(mark>=70 and mark<=80):
                pt=8
            elif(mark>=60 and mark<=70):
                pt=7
            elif(mark>=50 and mark<=60):
                pt=6
            elif(mark>=45 and mark<=50):
                pt=5
            elif(mark>=40 and mark<=45):
                pt=4
            else:
                pt=0
            cr=int(ent3.get())
#            print(type(sum1),type(pt),type(cr))
            sum1+=(pt*cr)
            crsum+=cr
            print(str(sum1)+"\t"+str(crsum)+"\t"+str(mark))
            i=i+1
            if(i<n):
                btn3 = Button(window, text="Proceed", command=cal)
                btn3.grid(column=6, row=i+1)
            else:
                btn3 = Button(window, text="Submit", command=sgpasum)
                btn3.grid(column=6, row=i+1)

        btn3 = Button(window, text="Save", command=cont)
        btn3.grid(column=5, row=i+2)
##        if(i==n-1):
##            btn4 = Button(window, text="Submit", command=sgpasum)
##            btn4.grid(column=5,row=i+2)

##    def sgpa():
##        
##        lbl2=Label(window, text="Enter Subject Marks : ")
##        lbl2.grid(row=1,column=2)

        
##        btn4 = Button(window, text="Submit", command=sgpasum)
##        btn4.grid(column=3, row=n+2)


    btn3 = Button(window, text="Next", command=cal)
    btn3.grid(column=3, row=0)

window.title("GPA Calculator")
#window.geometry('400x400')
btn1 = Button(window, text="SGPA",command=ext)
btn1.grid(column=0, row=0)
btn2 = Button(window, text="CGPA",command=ext1)
btn2.grid(column=0, row=1)

window.mainloop()
