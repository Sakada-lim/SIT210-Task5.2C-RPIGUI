from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
red = LED(14)
green = LED(15)
blue = LED(4)

## GUI DEFINITIONS ##

win = Tk()
win.title("RGB led toggler")
myFont = tkinter.font.Font(family = 'Hekvetica', size = 12 , weight = "bold")

### EVENT FUNCTION###

def redtoggle():
    if red.is_lit:
        red.off()
        redButton["text"] = "turn red LED on"
    else:
        red.on()
        redButton["text"] = "turn red LED off"
def greentoggle():
    if green.is_lit:
        green.off()
        greenButton["text"] = "turn green LED on"
    else:
        green.on()
        greenButton["text"] = " turn green LED off"
def bluetoggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "turn blue LED on"
    else:
        blue.on()
        blueButton["text"] = "turn blue LED off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
    
### WIDGETS ###
    
redButton = Button(win, text = "turn red LED On", font = myFont, command = redtoggle, bg = "pink", height = 1, width = 24)
redButton.grid(row = 0, column = 1)
blueButton = Button(win, text = "turn blue LED On", font = myFont, command = bluetoggle, bg = "lightblue", height = 1, width = 24)
blueButton.grid(row = 1, column = 1)
greenButton = Button(win, text = "turn green LED On", font = myFont, command = greentoggle, bg = "lightgreen", height = 1, width = 24)
greenButton.grid(row = 2, column = 1)


win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        