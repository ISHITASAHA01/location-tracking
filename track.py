from tkinter import *
from PIL import ImageTk,Image
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root=Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+100+100")
root.resizable(False,False)
def Track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)
    #country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)
    
    #operator like idea,airtel,jio
    operator=carrier.name_for_number(number,'en')
    sim.config(text=operator)
    
    #phone timezone
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)
    
    #lomgitude and latitude
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(locate)
    
    lng=location.longitude
    lat=location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)
    
    #time showing in phone
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longtidue,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    CURRENT_time=local_time.strftime("%I:%M %p")
    clock.config(text=CURRENT_time)
    

#icon image
icon=ImageTk.PhotoImage(file=r'F:\my project\python\python project\locationTrack\Ltproject\1.jpg')
root.iconphoto(False,icon)

#logo
logo=ImageTk.PhotoImage(file=r'F:\my project\python\python project\locationTrack\Ltproject\2.jpg')
Label(root,image=logo).place(x=240,y=70)

Eback=ImageTk.PhotoImage(file=r'F:\my project\python\python project\locationTrack\Ltproject\3.jpg')
Label(root,image=Eback).place(x=20,y=190)

Heading=Label(root,text="TRACK NUMBER",font=('arial',12,'bold'))
Heading.place(x=90,y=100)
#bottom box
Box=ImageTk.PhotoImage(file=r'F:\my project\python\python project\locationTrack\Ltproject\4.jpg')
Label(root,image=Box,width=100,height=10).place(x=-2,y=355)

#entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=("arial",20))
enter_number.place(x=50,y=220)
#search button
Search_image=ImageTk.PhotoImage(file=r'F:\my project\python\python project\locationTrack\Ltproject\5.jpg')
Search=Button(root,image=Search_image,borderwidth=0,cursor="hand2",bd=0,command=Track,width=100,height=50)
Search.place(x=35,y=300)

#label(information)
country=Label(root,text="country:",bg="#57adff",fg="black",font=("arial",10,'bold'))
country.place(x=50,y=400)

sim=Label(root,text="SIM:",bg="#57adff",fg="black",font=("arial",10,'bold'))
sim.place(x=250,y=400)

zone=Label(root,text="Time Zone:",bg="#57adff",fg='black',font=("arial",10,'bold'))
zone.place(x=50,y=500)

clock=Label(root,text="Phone Time:",bg="#57adff",fg='black',font=("arial",10,'bold'))
clock.place(x=50,y=440)

longitude=Label(root,text="Longitude:",bg="#57adff",fg='black',font=("arial",10,'bold'))
longitude.place(x=250,y=440)

latitude=Label(root,text="Latitude:",bg="#57adff",fg='black',font=("arial",10,'bold'))
latitude.place(x=250,y=500)

root.mainloop()
