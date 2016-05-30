import socket
from main import Gesture
from data import DataManager
import controller
import Xlib.display
import win32gui

app_id = 1
app = Gesture(app_id)
manager = DataManager()
app.train(manager.folders,manager.names,manager.labels)	
app.initClassifier()
last_msg="0.00"
value_to_controller=-1

s = socket.socket()
host = socket.gethostname() 
port = 8000
s.bind((host, port))
s.listen(5)

while True:
   c, addr = s.accept()
   print '\nGot connection from', addr
   
   msg= [] 
   msg = c.makefile().read(-1)
   w=win32gui
   window_in_focus_name=w.GetWindowText(w.GetForegroundWindow())
   print window_in_focus_name
   print(len(msg)) 
   msg = msg[2:]
   print msg
   file = open("test.txt","w")
   file.write(msg)
   file.close()   

   #checking for special button inputs
   if(len(msg)<30):
           if("up" in msg):
               #controller.fun(9)
               value_to_controller=9
           if("down" in msg): 
               #controller.fun(10)
               value_to_controller=10
           if("left" in msg): 
               #controller.fun(11)
               value_to_controller=11
           if("right" in msg): 
               #controller.fun(12)
               value_to_controller=12
   elif((len(msg)>=1024)and(last_msg!=msg)):
           test = app.getDataFromFile("test.txt")
           last_msg=msg
           result = app.predict(test)
           print manager.folders[result-1]
           app.plotImage("test.txt")
           #controller.fun(result)
           value_to_controller=result
   else:
       print "data not recieved properly"
       
   #checking if the picasa photo viewer is opened or not    
   if(("Picasa Photo" in window_in_focus_name)or("Flash" in window_in_focus_name)or("PowerPoint" in window_in_focus_name)):
           controller.fun(value_to_controller)
   #controller.fun(value_to_controller)
   c.close()    
