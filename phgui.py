import phonenumbers 
from phonenumbers import geocoder,timezone,carrier
from geopy.geocoders import Nominatim
from tkinter import *
import time
import subprocess
#from datetime import *

#body settings
root = Tk()
#root.geometry('370×970')
root.resizable(False,False)
label=Label(root,text="Please Use With A VPN")
label.pack()
def track():
    number=entry.get()
    pars=phonenumbers.parse(number)
    #country
    geo=geocoder.description_for_number(pars,"en")
    country.config(text=geo)
    
#date
date="2022-06-01"

#Heading
head=Label(root,text="PhoneTrack\n--------------------------------",font=("arial",15,"bold"))
head.place(x=10,y=110)

#Entry
entry=StringVar()
ent_num=Entry(root,textvariable=entry,width=20,bd=0,font=("arial",15),justify="center")
ent_num.place(x=10,y=300)

#button
search=Button(text="[search]",bg="#57adff",borderwidth=0,cursor="hand2",bd=0,font=("arial",15),command=track)
search.place(x=5,y=390)

#bottom box

#bb=Label(root,text=f" This tool was made By the one and Only\n>> TeknikalDon <<\nOn {date}",font=("arial",10,"bold")).place(x=2,y=1010)

country=Label(text="country:",bg="#57adff",fg="black",font=( "arial",10,"bold")).place(x=50,y=500)

sim=Label(text="sim:",bg="#47adff",fg="black",font=( "arial",10,"bold")).place(x=50,y=580)

clock=Label(text="phone_time:",bg="#57adff",fg="black",font=( "arial",10,"bold")).place(x=50,y=670)

zone=Label(text="timezone:",bg="#57adff",fg="black",font=( "arial",10,"bold")).place(x=50,y=750)

longitude=Label(text="longitude:",bg="#57adff",fg="black",font=( "arial",10,"bold")).place(x=50,y=820)





root.mainloop()