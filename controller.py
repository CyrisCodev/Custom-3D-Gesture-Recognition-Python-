"""
from main import Gesture
from data import DataManager

app_id = 1
app = Gesture(app_id)

manager = DataManager()

app.train(manager.folders,manager.names,manager.labels)	
#print len(app.features[0])
app.initClassifier()


test = app.getDataFromFile("./dataset/circle/one.txt")
print manager.folders[app.predict(test)-1]
print app.predict(test)
app.plotImage("./dataset/circle/one.txt")"""

from pymouse import PyMouse
from pykeyboard import PyKeyboard
from win32api import GetSystemMetrics

m = PyMouse()
k = PyKeyboard()
system_height=GetSystemMetrics(1)
system_width=GetSystemMetrics(0)
move_factor=150

print(system_height)
print(system_width)

def fun(inp):
    if(inp==1):
        k.tap_key(k.right_key)
        
        #m.drag(100,100)
    elif(inp==2):
        #will perform zoom-in 
        k.tap_key(k.left_key)
    elif(inp==3):
        #will perform zoom-in 
        k.tap_key(k.up_key)
    elif(inp==4):
        #will perform zoom-in 
        k.tap_key(k.down_key)
    elif(inp == 9):
        #up button pressed
        #will perform downward motion
        move_image(0,move_factor)
    elif(inp == 10):
        #down button pressed
        #will perform upward motion
        move_image(0,-move_factor)
    elif(inp == 11):
        #left button pressed
        #will perform rightward motion
        move_image(move_factor,0)
    elif(inp == 12):
        #right button pressed
        #will perform leftward motion
        move_image(-move_factor,0)
    elif(inp==14):
        k.press_key(k.alt_key)
        k.tap_key(k.right_key,n=8)
        k.release_key(k.alt_key)
    elif(inp==15):
        k.press_keys([k.windows_l_key,'d'])
    else:
        k.press_key(k.alt_key)
        k.tap_key(k.left_key,n=8)
        k.release_key(k.alt_key)
        
def move_image(a,b):
        x,y=m.position()
        print("x ",x,"y ", y)
        print("System width-50 :",system_width-50)
        print("System height-250 :",system_height-250)
        print("x+a :", x+a," y+b :", y+b)
        
        if((x+a)>50 and (x+a)<(system_width-50)):
            if((y+b)>50 and (y+b)<(system_height-(system_height/6))):
                print("x ",x,"y ",y )
                m.press(*m.position())
                m.move(x+a,y+b)
                m.release(*m.position())       
        
