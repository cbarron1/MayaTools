from pymel.core import *

def turnColor(inputColor):
    selectedShapes = listRelatives(s=True)
    for item in selectedShapes:
        setAttr (item + ".overrideEnabled",1)
        setAttr (item + ".overrideColor",inputColor)
            

def redButton(*args):
    print "Red"
    turnColor(13)
    
def blueButton(*args):
    print "Blue"
    turnColor(6)

def yellowButton(*args):
    print "Yellow"
    turnColor(17)

def orangeButton(*args):
    print "Orange"
    turnColor(24)
    
win = window(title="Color Overrider",width=200,height=400)
layout = columnLayout()
redBtn = button(label='Red', command=redButton, width=200,height=100)
blueBtn = button(label='Blue', command=blueButton, width=200,height=100)
yellowButton = button(label='Yellow', command=yellowButton, width=200,height=100)
orangeButton = button(label='Orange', command=orangeButton, width=200,height=100)
win.show()
