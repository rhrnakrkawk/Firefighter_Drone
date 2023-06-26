# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 01:51:51 2023

@author: taewoo
"""


import paho.mqtt.client as mqtt
import threading
import time
from tkinter import *
from tkinter import messagebox
import folium
import webbrowser

 
class MyFrame(Frame):
    def __init__(self, master=Frame):
        self.lb_dronestate = Label(master, text = "drone state : ")
        self.lb_curdronestate = Label(master, text = "nomal")
        self.lb_latitude= Label(master, text = "")
        self.lb_longitude = Label(master, text = "")
        self.lb_lat = Label(master, text = "Latitude : ")
        self.lb_long = Label(master, text = "Longitude : ")
        
        self.lb_dronestate.place(x=20, y=50)
        self.lb_curdronestate.place(x=90, y=50)
        self.lb_lat.place(x=20, y=100)
        self.lb_latitude.place(x=90, y=100)
        self.lb_longitude.place(x=90, y=150)
        self.lb_long.place(x=20, y=150)
        
        
    def sett(self, text1):
        self.lb_curdronestate.config(text=text1)
        
    def createLatitude(self, pos):
        self.lb_latitude.config(text = pos)
        
    def createLongitude(self, pos):
        self.lb_longitude.config(text=pos)
        

def mqtt_s():
    s_st.loop_forever()
    
def call_back(client, userdata, message):
    string = str(message.payload.decode("utf-8"))
    command, latitude, longitude = string.split(",")
    lat = float(latitude)
    lon = float(longitude)
    lat_curr = 37.670806
    lon_curr = 126.778892
    m = folium.Map(location=[(lat+lat_curr)/2, (lon+lon_curr)/2], zoom_start=15)
    folium.Marker([lat_curr, lon_curr], popup='<b>Fire Station</b>').add_to(m)
    folium.Marker([lat, lon], popup='<b>Destination</b>').add_to(m)
    m.save("map.html")
    webbrowser.open("map.html")
    

    if(command == "report"):
        msg = messagebox.askquestion("report", "there is report\ndo you start mission?")
        if(msg == "yes"):
            s_st.publish("data/drone", (latitude + "," + longitude))
            frame.sett("on progress")
            frame.createLatitude(latitude)
            frame.createLongitude(longitude)
    elif(string == "done"):
        messagebox.showinfo("info", "mission clear!")
        frame.sett("no progress")

 
    
if __name__ == '__main__':
    broker = "210.106.192.242"
    s_st = mqtt.Client("mqtt_ST")
    s_st.on_message = call_back
 
    
    s_st.connect(broker, 1883)
    s_st.subscribe("data/ST")
   
    root = Tk()
    root.title('GUI')
    root.geometry('200x200')
    frame = MyFrame(root)
    
    t2 = threading.Thread(target=mqtt_s)
    t2.start()
    
    root.mainloop()
    t2.join()