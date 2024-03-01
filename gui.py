from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

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
class Trackno:    
    def __init__(self,root):
        self.root=root
        self.root.title("Phone Number Tracker")
        self.root.geometry("500x600+100+100")
        self.root.resizable(False,False)
        self.Heading=Label(self.root,text="TRACK NUMBER",font=('arial',12,'bold'))
        self.Heading.place(x=180,y=100)
         
        self.varphno=StringVar()
        self.varCtry=StringVar()
        
        
        toplbl=Label(self.root,text="Country code:").place(x=50,y=220)
        self.Ctrycom=ttk.Combobox(self.root,textvariable=self.varCtry,font=("",15,"bold"),state=READABLE)
        self.Ctrycom["values"]=('+91','+1','+44','+61','+86','+61')
        self.Ctrycom.place(x=50,y=190)  
        self.Ctrycom.current(0) 
        
        self.enter_number=Entry(self.root,textvariable=self.varphno,width=25,justify="center",font=("arial",20))
        self.enter_number.place(x=50,y=220)
        #search button
        
        self.Searc=Button(self.root,text="Search",font=("",15,"bold"),cursor='hand2',command=self.dataretrieve)
        self.Searc.place(x=200,y=280)
        
        self.country=Label(self.root,text="country:",bg="#57adff",fg="black",font=("arial",10,'bold'))
        self.country.place(x=50,y=400)

        self.sim=Label(self.root,text="SIM:",bg="#57adff",fg="black",font=("arial",10,'bold'))
        self.sim.place(x=250,y=400)

        self.zone=Label(self.root,text="Time Zone:",bg="#57adff",fg='black',font=("arial",10,'bold'))
        self.zone.place(x=50,y=500)

        self.clock=Label(self.root,text="Phone Time:",bg="#57adff",fg='black',font=("arial",10,'bold'))
        self.clock.place(x=50,y=440)

        self.longitude=Label(self.root,text="Longitude:",bg="#57adff",fg='black',font=("arial",10,'bold'))
        self.longitude.place(x=250,y=440)

        self.latitude=Label(self.root,text="Latitude:",bg="#57adff",fg='black',font=("arial",10,'bold'))
        self.latitude.place(x=250,y=500)
        
        
    def dataretrieve(self):
        conn=mysql.connector.connect(host="localhost",user='root',password='mysql',database='indradb')
        my_cursor=conn.cursor() 
        print(self.varphno.get())
        print(self.varCtry.get())
        con=my_cursor.execute("select * from register where phno=%s and code=%s",(self.varphno.get(),self.varCtry.get()))
        print(con)
        row=my_cursor.fetchone()
        print(row)
        if(row==None):
            messagebox.showerror("Invaid","phone no. not exist")
            enter_number=self.varCtry.get()+self.varphno.get()
            print(enter_number)
            number=phonenumbers.parse(enter_number)         
            locate=geocoder.description_for_number(number,'en')
            geolocator=Nominatim(user_agent="geoapiExercises")
            location=geolocator.geocode(locate)            
            lng=location.longitude
            lat=location.latitude   
            self.longitude.config(text=lng)
            self.latitude.config(text=lat)
            self.Track(self.varCtry.get()+self.varphno.get())
        else:
            #lomgitude and latitude              
            enter_number=self.varCtry.get()+self.varphno.get()
            # enter_number=self.varphno.get()
            number=phonenumbers.parse(enter_number)         
            locate=geocoder.description_for_number(number,'en')
            geolocator=Nominatim(user_agent="geoapiExercises")
            location=geolocator.geocode(locate)
            
            lng=location.longitude
            lat=location.latitude            
            self.longitude.config(text=row[2])
            self.latitude.config(text=row[3])
            self.Track(self.varCtry.get()+self.varphno.get())
        conn.close()
        messagebox.showinfo("info:","success")
    
    
    def Track(self,t):
        enter_number=t
        # enter_number=self.varphno.get()
        number=phonenumbers.parse(enter_number)
        #country
        locate=geocoder.description_for_number(number,'en')
        self.country.config(text=locate)
        
        #operator like idea,airtel,jio
        operator=carrier.name_for_number(number,'en')
        self.sim.config(text=operator)
        
        #phone timezone
        time=timezone.time_zones_for_number(number)
        self.zone.config(text=time)
        
        # #lomgitude and latitude
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(locate)
        
        # lng=location.longitude
        # lat=location.latitude
        # self.longitude.config(text=lng)
        # self.latitude.config(text=lat)
        
        #time showing in phone
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        CURRENT_time=local_time.strftime("%I:%M %p")
        self.clock.config(text=CURRENT_time)


      
        
        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry("1200x600+0+0")
        ###################
        self.varFname=StringVar()
        self.varLname=StringVar()
        self.varLag=StringVar()
        self.varLat=StringVar()
        self.varCtry=StringVar()
        self.varPh=StringVar()
        
        
        
        ################
        frame=Frame(self.root,bg="yellow")
        frame.place(x=600,y=150,width=400,height=400)  
        
        toplbl=Label(frame,text="Register here",bg="yellow",font=("",15,"bold"))
        toplbl.place(x=10,y=10)      
        toplbl=Label(frame,text="First Name:").place(x=50,y=50)
        self.fnameentry=ttk.Entry(frame,textvariable=self.varFname,font=("",15,"bold"))
        self.fnameentry.place(x=130,y=50)     
        toplbl=Label(frame,text="Last name:").place(x=50,y=100)
        self.lnameentry=ttk.Entry(frame,textvariable=self.varLname,font=("",15,"bold"))
        self.lnameentry.place(x=130,y=100)     
        toplbl=Label(frame,text="langitude:").place(x=50,y=150)
        self.lagentry=ttk.Entry(frame,textvariable=self.varLag,font=("",15,"bold"),width=12)
        self.lagentry.place(x=50,y=180)       
        toplbl=Label(frame,text="latitude:").place(x=230,y=150)
        self.latentry=ttk.Entry(frame,textvariable=self.varLat,font=("",15,"bold"),width=12)
        self.latentry.place(x=230,y=180) 
        toplbl=Label(frame,text="Country code:").place(x=50,y=220)
        self.Ctrycom=ttk.Combobox(frame,textvariable=self.varCtry,font=("",15,"bold"),state=READABLE)
        self.Ctrycom["values"]=('+91','+1','+44','+61','+86','+61')
        self.Ctrycom.place(x=130,y=220)  
        self.Ctrycom.current(0) 
        
        toplbl=Label(frame,text="phone no:").place(x=50,y=250)
        self.phentry=ttk.Entry(frame,textvariable=self.varPh,font=("",15,"bold"))
        self.phentry.place(x=130,y=250)
        
        self.btn=Button(frame,text="ADD To DB",font=("",15,"bold"),cursor='hand2',command=self.registerData)
        self.btn.place(x=150,y=300)
        
    def registerData(self):
        #self.varFname.get()
        conn=mysql.connector.connect(host="localhost",user='root',password='mysql',database='indradb')
        my_cursor=conn.cursor()
        query=("select * from register where phno=%s")
        value=(self.varPh.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if row!=None:
            messagebox.showerror("error:","aready exist")
        else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.varFname.get(),
                                                                                self.varLname.get(),
                                                                                self.varLag.get(),
                                                                                self.varLat.get(),
                                                                                self.varCtry.get(),
                                                                                self.varPh.get()
                                                                                ))
        conn.commit()
        conn.close()
        messagebox.showinfo("info:","success")
        
        


if(__name__=='__main__'):
    root=Tk()
    # app=Register(root)    
    app=Trackno(root)
    root.mainloop()
    
    