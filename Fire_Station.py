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
from haversine import haversine
lat_curr = 37.670806
lon_curr = 126.778892
# class MyFrame(Frame):
#     def __init__(self, master=Frame):
#         self.lb_dronestate = Label(master, text = "drone state : ")
#         self.lb_curdronestate = Label(master, text = "nomal")
#         self.lb_latitude= Label(master, text = "")
#         self.lb_longitude = Label(master, text = "")
#         self.lb_lat = Label(master, text = "Latitude : ")
#         self.lb_long = Label(master, text = "Longitude : ")
#         self.btn_map = Button(master, text = "지도 보기")
#         self.lb_dronestate.place(x=20, y=50)
#         self.lb_curdronestate.place(x=90, y=50)
#         self.lb_lat.place(x=20, y=100)
#         self.lb_latitude.place(x=90, y=100)
#         self.lb_longitude.place(x=90, y=150)
#         self.lb_long.place(x=20, y=150)
        
        
#     def sett(self, text1):
#         self.lb_curdronestate.config(text=text1)
        
#     def createLatitude(self, pos):
#         self.lb_latitude.config(text = pos)
        
#     def createLongitude(self, pos):
#         self.lb_longitude.config(text=pos)
    
        
# class Frame_1(Frame):
#     def __init__(self, master=Frame):
#         self.lb_lat = Label(master, text="Latitude")
#         self.lb_lon = Label(master, text="Longitude")
#         self.lb_lat_curr = Label(master, text="")
#         self.lb_lon_curr = Label(master, text="")
#         self.lb_state_curr = Label(master, text="Not Yet")
#         self.lb_state = Label(master, text="Drone")
        
#         self.lb_lat.grid(row=0,column=0)
#         self.lb_lat_curr.grid(row=0,column=1)
        
#         self.lb_lon.grid(row=1,column=0)
#         self.lb_lon_curr.grid(row=1,column=1)
        
#         self.lb_state.grid(row=2,column=0)
#         self.lb_state_curr.grid(row=2,column=1)

#     def setText(self, lb, msg):
#         lb.config(text=msg)
        
# class Frame_2(Frame):
#     def __init__(self, master=Frame):
#         self.btn_map = Button(master, text="지도보기")
#         self.btn_start = Button(master, text="드론 출발")
        
#         self.btn_map.grid(row= 0 , column = 0)
#         self.btn_start.grid(row= 1 , column = 0)
     

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
    

#     if(command == "report"):
#         msg = messagebox.askquestion("report", "there is report\ndo you start mission?")
#         if(msg == "yes"):
#             s_st.publish("data/drone", (latitude + "," + longitude))
#             frame.sett("on progress")
#             frame.createLatitude(latitude)
#             frame.createLongitude(longitude)
#     elif(string == "done"):
#         messagebox.showinfo("info", "mission clear!")
#         frame.sett("no progress")

 
    
# if __name__ == '__main__':
#     broker = "210.106.192.242"
#     s_st = mqtt.Client("mqtt_ST")
#     s_st.on_message = call_back
 
    
#     s_st.connect(broker, 1883)
#     s_st.subscribe("data/ST")
    
#     root = Tk()
#     root.title('GUI')
#     f1 = Frame(root, width=500, height=500)
#     f2 = Frame(root, width=500, height=500)
#     frame1 = Frame_1(f1)
#     frame2 = Frame_2(f2)
#     frame1.pack(side="left")
#   #  frame2.pack(side="right")
    
    
#     # t2 = threading.Thread(target=mqtt_s)
#     # t2.start()
    
    # root.mainloop()
#     # t2.join()
    # fireStation = (lat_curr, lon_curr)  #Latitude, Longitude

    # # 거리 계산
    # haversine(Seoul, Toronto, unit = 'km')
    
broker = "210.106.192.242"
s_st = mqtt.Client("mqtt_ST")
s_st.on_message = call_back
 
    
s_st.connect(broker, 1883)
s_st.subscribe("data/ST")
            
               
root = Tk()
root.title('GUI')
frame1 = Frame(root, width=500, height=500,borderwidth=10)
frame2 = Frame(root, width=500, height=500,borderwidth=10)

# frame1
lb_lat = Label(frame1, text="Latitude", width=10, height=3, bg='white', fg='black', relief='ridge', borderwidth=4)
lb_lon = Label(frame1, text="Longitude", width=10, height=3, bg='white', fg='black', relief='ridge', borderwidth=4)
lb_lat_curr = Label(frame1, text="-", width=20, height=3, bg='white', fg='black', relief='ridge', borderwidth=4)
lb_lon_curr = Label(frame1, text="-", width=20, height=3, bg='white', fg='black', relief='ridge', borderwidth=4)
lb_state_curr = Label(frame1, text="Not Yet", width=20, height=3, bg='white', fg='black', relief='ridge', borderwidth=4)
lb_state = Label(frame1, text="Drone", width=10, height=3, bg='white', fg='black', relief='ridge', borderwidth=4)

lb_lat.grid(row=0,column=0)
lb_lat_curr.grid(row=0,column=1)
        
lb_lon.grid(row=1,column=0)
lb_lon_curr.grid(row=1,column=1)
        
lb_state.grid(row=2,column=0)
lb_state_curr.grid(row=2,column=1)



#frame2
btn_map = Button(frame2, text="지도보기",  pady = 5, padx = 5)
btn_start = Button(frame2, text="드론 출발",  pady = 5, padx = 5)
btn_cancel = Button(frame2, text='취소', pady = 5, padx = 5)
        
btn_map.grid(row= 0 , column = 0,  pady = 5, padx = 5)
btn_start.grid(row= 2 , column = 0,  pady = 5, padx = 5)
btn_cancel.grid(row=2, column=1,  pady = 5, padx = 5)

btn_start["state"] = DISABLED
btn_cancel["state"] = DISABLED

frame1.pack(side='left')
frame2.pack(side='left')
t2 = threading.Thread(target=mqtt_s)
t2.start()
    
root.mainloop()
t2.join()
