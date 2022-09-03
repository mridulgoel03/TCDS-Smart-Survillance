import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time


def signUpPage():

    global sup
    sup = Tk()
    sup.title('TCDS App')
    
    time = StringVar()
    datee = StringVar()
    bod = StringVar()
    col = StringVar()
    gen = StringVar()
    agee = StringVar()
    dress = StringVar()
    ob = StringVar()
    placee = StringVar()
    des = StringVar()
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#585858")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#88001B")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="TCDS Details",fg="#FFA500",bg="#88001B")
    heading.config(font=('calibri 30'))
    heading.place(relx=0.3,rely=0.01)



    #time
    tlabel = Label(sup_frame,text="Time",fg='white',bg='black')
    tlabel.place(relx=0.01,rely=0.2)
    tim = Entry(sup_frame,bg='white',fg='black',textvariable = time)
    tim.config(width=35)
    tim.place(relx=0.11,rely=0.2)

    #Date
    dlabel = Label(sup_frame,text="Date",fg='white',bg='black')
    dlabel.place(relx=0.01,rely=0.4)
    dat = Entry(sup_frame,bg='white',fg='black',textvariable = datee)
    dat.config(width=35)
    dat.place(relx=0.11,rely=0.4)
    
    
    #Body Posture
    blabel = Label(sup_frame,text="Body Posture",fg='white',bg='black')
    blabel.place(relx=0.51,rely=0.4)
    bod = Entry(sup_frame,bg='white',fg='black',textvariable = bod)
    bod.config(width=28)
    bod.place(relx=0.65,rely=0.4)


    
    
    
    #Colour
    clabel = Label(sup_frame,text="Colour",fg='white',bg='black')
    clabel.place(relx=0.517,rely=0.2)
    col = Entry(sup_frame,bg='white',fg='black',textvariable = col)
    col.config(width=35)
    col.place(relx=0.61,rely=0.2)

    #Gender
    glabel = Label(sup_frame,text="Gender",fg='white',bg='black')
    glabel.place(relx=0.01,rely=0.3)
    gen = Entry(sup_frame,bg='white',fg='black',textvariable = gen)
    gen.config(width=35)
    gen.place(relx=0.11,rely=0.3)




    #Age
    alabel = Label(sup_frame,text="Age",fg='white',bg='black')
    alabel.place(relx=0.52,rely=0.3)
    age = Entry(sup_frame,bg='white',fg='black',textvariable = agee)
    age.config(width=35)
    age.place(relx=0.61,rely=0.3)


    #Dressing
    drlabel = Label(sup_frame,text="Dressing",fg='white',bg='black')
    drlabel.place(relx=0.01,rely=0.5)
    dress = Entry(sup_frame,bg='white',fg='black',textvariable = dress)
    dress.config(width=60)
    dress.place(relx=0.18,rely=0.5)



    #Objects
    olabel = Label(sup_frame,text="Objects",fg='white',bg='black')
    olabel.place(relx=0.01,rely=0.6)
    ob = Entry(sup_frame,bg='white',fg='black',textvariable = ob)
    ob.config(width=30)
    ob.place(relx=0.18,rely=0.6)



    #Place
    plabel = Label(sup_frame,text="Place",fg='white',bg='black')
    plabel.place(relx=0.52,rely=0.6)
    place = Entry(sup_frame,bg='white',fg='black',textvariable = placee)
    place.config(width=35)
    place.place(relx=0.62,rely=0.6)



    #Description of incident
    delabel = Label(sup_frame,text="Describe the Incident",fg='white',bg='black')
    delabel.place(relx=0.01,rely=0.7)
    des = Entry(sup_frame,bg='white',fg='black',textvariable = des)
    des.config(width=70)
    des.place(relx=0.25,rely=0.7)

    
    def addUserToDataBase():
        #time,dat,body_posture,colorr,gender,age,dressing,objects,place,Description_of_incident 
        time = tim.get()
        datee = dat.get()
        body_posture = bod.get()
        colorr = col.get()
        gender = gen.get()
        agee = age.get()
        dressing = dress.get()
        objects = ob.get()
        placee = place.get()
        Description_of_incident = des.get()
        
        
        if len(tim.get())==0 and len(dat.get())==0 and len(bod.get())==0 and len(col.get())==0 and len(gen.get())==0 and len(age.get())==0 and len(dress.get())==0 and len(ob.get())==0 and len(place.get())==0 and len(des.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(tim.get())==0 or len(dat.get())==0 or len(bod.get())==0 or len(col.get())==0 or len(gen.get())==0 or len(age.get())==0 or len(dress.get())==0 or len(ob.get())==0 or len(place.get())==0 or len(des.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(dat.get()) == 0 and len(des.get()) == 0:
            error = Label(text="Name and Description can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(dat.get()) == 0 and len(des.get()) != 0 :
            error = Label(text="Name can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(dat.get()) != 0 and len(des.get()) == 0:
            error = Label(text="Description can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('Attendence.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(TIME text ,DAT text ,BODY_POSTURE text ,COLORR text ,GENDER text ,AGE text ,DRESSING text ,OBJECTS text ,PLACE text ,DESCRIPTION_OF_INCIDENT text )')
            
            create.execute("insert into userSignUp values(?,?,?,?,?,?,?,?,?,?)", (str(time),str (dat),str (bod), str(col), str(gen), str(age), str(dress), str(ob), str(place), str(des)))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        exec(open("part2.py").read())
    #signup BUTTON
    sp = Button(sup_frame,text='Report',padx=5,pady=5,width=5,command = lbw, bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)


def lbw():
    exit()


    sup.mainloop()



    
if __name__=='__main__':
    signUpPage()
