from pymel.core import *
from PySide.QtCore import *
from PySide.QtGui import *
from shiboken import wrapInstance
from maya import OpenMayaUI as mui
import coloroverrider as cOVR

def maya_main_window():
    main_window_ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QWidget)
    
class gMainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        
        super(gMainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.Tool)
        self.ui = cOVR.Ui_ColorOverrider()
        self.ui.setupUi(self)
        
        self.buttonBG = QPalette()
        self.colorValues = self.ui.ColorSlider.value()
        
        self.make_connections()
        
    def make_connections(self):
        
        self.ui.redButton.clicked.connect(self.red_button_press)
        self.ui.blueButton.clicked.connect(self.blue_button_press)
        self.ui.yellowButton.clicked.connect(self.yellow_button_press)
        self.ui.orangeButton.clicked.connect(self.orange_button_press)
        self.ui.confirmButton.clicked.connect(self.confirm_button_press)
        self.ui.ColorSlider.valueChanged.connect(self.slider_value_change)
        
    def turnColor(self,inputColor):
        selectedShapes = listRelatives(s=True)
        for item in selectedShapes:
            setAttr (item + ".overrideEnabled",1)
            setAttr (item + ".overrideColor",inputColor)
        
    ############################
    ###  Callback Functions  ###
    ############################
    
    def red_button_press(self):
        self.ui.ColorSlider.setValue(13)
        
    def blue_button_press(self):
        self.ui.ColorSlider.setValue(6)
        
    def yellow_button_press(self):
        self.ui.ColorSlider.setValue(17)
        
    def orange_button_press(self):
        self.ui.ColorSlider.setValue(24)
        
    def confirm_button_press(self):
        self.turnColor(self.ui.ColorSlider.value())
        
    def slider_value_change(self):
        
        myColorIndex = self.ui.ColorSlider.value()
        if (myColorIndex > 0):
            self.colorValues = colorIndex(myColorIndex, q=True)
        print self.colorValues
       
        '''
        palette = self.ui.confirmButton.palette()
        palette.setColor(QPalette.Button, QColor(self.colorValues[0], self.colorValues[1], self.colorValues[2]))
        self.ui.confirmButton.setPalette(palette)
        '''

    
        
coWin = gMainWindow(parent=maya_main_window())
coWin.show()

'''        
if __name__ == "__main__":
    try:
        ui.close()
    except:
        pass
    
    ui = PrimitiveUi()
    ui.show()
'''