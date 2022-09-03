import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time


def signUpPage():

    global sup
    sup = Tk()
    sup.title('TCDS App')
    
    fname = StringVar()
    datee = StringVar()
    time = StringVar()
    street = StringVar()
    colony = StringVar()
    city = StringVar()
    nearestp = StringVar()
    mobile = StringVar()
    email = StringVar()
    desc = StringVar()
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="#BADA55")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="TCDS Details",fg="#FFA500",bg="#BADA55")
    heading.config(font=('calibri 30'))
    heading.place(relx=0.3,rely=0.01)

    #name
    flabel = Label(sup_frame,text="Name",fg='white',bg='black')
    flabel.place(relx=0.01,rely=0.2)
    fname = Entry(sup_frame,bg='white',fg='black',textvariable = fname)
    fname.config(width=35)
    fname.place(relx=0.11,rely=0.2)

    #Date
    dlabel = Label(sup_frame,text="Date",fg='white',bg='black')
    dlabel.place(relx=0.01,rely=0.4)
    dat = Entry(sup_frame,bg='white',fg='black',textvariable = datee)
    dat.config(width=35)
    dat.place(relx=0.11,rely=0.4)
    
    
    #Time
    tlabel = Label(sup_frame,text="Time",fg='white',bg='black')
    tlabel.place(relx=0.51,rely=0.4)
    time = Entry(sup_frame,bg='white',fg='black',textvariable = time)
    time.config(width=35)
    time.place(relx=0.61,rely=0.4)
    
    
    
    #Street
    slabel = Label(sup_frame,text="Street",fg='white',bg='black')
    slabel.place(relx=0.517,rely=0.2)
    s = Entry(sup_frame,bg='white',fg='black',textvariable = street)
    s.config(width=35)
    s.place(relx=0.61,rely=0.2)

    #Colony
    clabel = Label(sup_frame,text="Colony",fg='white',bg='black')
    clabel.place(relx=0.01,rely=0.3)
    c = Entry(sup_frame,bg='white',fg='black',textvariable = colony)
    c.config(width=35)
    c.place(relx=0.11,rely=0.3)



    #City
    ctlabel = Label(sup_frame,text="City",fg='white',bg='black')
    ctlabel.place(relx=0.52,rely=0.3)
    ct = Entry(sup_frame,bg='white',fg='black',textvariable = city)
    ct.config(width=35)
    ct.place(relx=0.61,rely=0.3)





    #Nearest Police station
    nlabel = Label(sup_frame,text="Nearest Police Station",fg='white',bg='black')
    nlabel.place(relx=0.05,rely=0.5)
    n = Entry(sup_frame,bg='white',fg='black',textvariable = nearestp)
    n.config(width=60)
    n.place(relx=0.30,rely=0.5)






    #Mobile Number
    mlabel = Label(sup_frame,text="Mobile Number",fg='white',bg='black')
    mlabel.place(relx=0.01,rely=0.6)
    m = Entry(sup_frame,bg='white',fg='black',textvariable = mobile)
    m.config(width=30)
    m.place(relx=0.18,rely=0.6)



    #Email
    elabel = Label(sup_frame,text="E-Mail Id",fg='white',bg='black')
    elabel.place(relx=0.52,rely=0.6)
    e = Entry(sup_frame,bg='white',fg='black',textvariable = email)
    e.config(width=35)
    e.place(relx=0.62,rely=0.6)



    #Description
    dlabel = Label(sup_frame,text="Describe the Incident",fg='white',bg='black')
    dlabel.place(relx=0.01,rely=0.7)
    d = Entry(sup_frame,bg='white',fg='black',textvariable = desc)
    d.config(width=70)
    d.place(relx=0.25,rely=0.7)

    
    def addUserToDataBase():
        
        Name = fname.get()
        Date = dat.get()
        Time = time.get()
        Street = s.get()
        Colony = c.get()
        City = ct.get()
        Nearest_Police_Station = n.get()
        Mobile_number = m.get()
        Email = e.get()
        Description_of_incident = d.get()
        
        
        if len(fname.get())==0 and len(dat.get())==0 and len(time.get())==0 and len(s.get())==0 and len(c.get())==0 and len(ct.get())==0 and len(n.get())==0 and len(m.get())==0 and len(e.get())==0 and len(d.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(dat.get())==0 or len(time.get())==0 or len(s.get())==0 or len(c.get())==0 or len(ct.get())==0 or len(n.get())==0 or len(m.get())==0 or len(e.get())==0 or len(d.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get()) == 0 and len(d.get()) == 0:
            error = Label(text="Name and Description can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(fname.get()) == 0 and len(d.get()) != 0 :
            error = Label(text="Name can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(fname.get()) != 0 and len(d.get()) == 0:
            error = Label(text="Description can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('Detailss.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(NAME text, DATE text, TIME text, STREET text, COLONY text, CITY text, NEAREST_POLICE_STATION text, MOBILE_NUMBER text, EMAIL text, DESCRIPTION_OF_INCIDENT text)')
            
            create.execute("insert into userSignUp values(?,?,?,?,?,?,?,?,?,?)", (str(fname),str (dat),str (time), str(street), str(colony), str(city), str(Nearest_Police_Station), str(Mobile_number), str(email), str(Description_of_incident)))
            conn.commit()

            
            conn.close()
            
        
    
    #signup BUTTON
    sp = Button(sup_frame,text='Report',padx=5,pady=5,width=5,command = exit(), bg="black",fg="white")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)


def start():
    exit()
   

    sup.mainloop()



    
if __name__=='__main__':
    signUpPage()
