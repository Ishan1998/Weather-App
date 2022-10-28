from calendar import c
import json
from tkinter import *
import tkinter as tk
from turtle import bgcolor, color
from unicodedata import name
from unittest import result
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather Forecast App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#Function

def getWeather():
    try:
        city=textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #Weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=04898df0636345f0198e3ad2835729f3"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] -273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|", "FEELS", "LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather Forecast App","Wrong Input, please check and retry!😊")
        


# Search Box
Search_image= PhotoImage(file="Images/search_box.png")
myimage= Label(image=Search_image)
myimage.place(x=270,y=20)

textfield= tk.Entry(root,justify="center", width=18, font=("Times New Roman",25,"bold"),bg="black",border=0,fg="white")
textfield.place(x=290,y=25)
textfield.focus()

#Search Icon
Search_icon = PhotoImage(file="Images/search.png")
myimage_icon = Button(image=Search_icon,borderwidth=0, bg="black" ,cursor="hand2", command=getWeather)
myimage_icon.place(x=590,y=30)

#logo
Logo_image=PhotoImage(file="Images/logo.png")
logo=Label(image=Logo_image)
logo.place(x=200,y=100)

#Bottom Box
Frame_image = PhotoImage(file="Images/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Time
name = Label(root, font=("Algerian",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Algerian",20))
clock.place(x=30,y=130)

#Label
label1 = Label(root, text="WIND", font=("Showcard Gothic",15,'bold'),fg="White", bg="#00A2E8")
label1.place(x=120,y=400)

label2 = Label(root, text="HUMIDITY", font=("Showcard Gothic",15,'bold'),fg="White", bg="#00A2E8")
label2.place(x=250,y=400)

label3 = Label(root, text="DESCRIPTION", font=("Showcard Gothic",15,'bold'),fg="White", bg="#00A2E8")
label3.place(x=440,y=400)

label4 = Label(root, text="PRESSURE", font=("Showcard Gothic",15,'bold'),fg="White", bg="#00A2E8")
label4.place(x=650,y=400)

t= Label(font=("Algerian",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("Algerian",15,"bold"))
c.place(x=400,y=250)

w = Label(text="...",font=("Showcard Gothic",20,"bold"),bg="#00A2E8")
w.place(x=120,y=440)
h = Label(text="...",font=("Showcard Gothic",20,"bold"),bg="#00A2E8")
h.place(x=280,y=440)
d = Label(text="...",font=("Showcard Gothic",20,"bold"),bg="#00A2E8")
d.place(x=450,y=440)
p = Label(text="...",font=("Showcard Gothic",20,"bold"),bg="#00A2E8")
p.place(x=670,y=440)

root.mainloop()