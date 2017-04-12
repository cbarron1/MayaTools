from pymel.core import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as mui

def maya_main_window():
    main_window_ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QWidget)
    
class gMainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        
        super(gMainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.Tool)
        self.ui = Ui_ColorOverrider()
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
       
        palette = QPalette(self.ui.confirmButton.palette())
        palette.setColor(QPalette.Button,QColor(self.colorValues[0]*255,self.colorValues[1]*255,self.colorValues[2]*255))
        self.ui.confirmButton.setPalette(palette)
        

################################
###                          ###
###      Gui Definition      ###
###                          ###
################################

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ColorOverrider(object):
    def setupUi(self, ColorOverrider):
        ColorOverrider.setObjectName("ColorOverrider")
        ColorOverrider.resize(224, 284)
        self.centralWidget = QtWidgets.QWidget(ColorOverrider)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.blueButton = QtWidgets.QPushButton(self.centralWidget)
        self.blueButton.setMinimumSize(QtCore.QSize(100, 50))
        self.blueButton.setObjectName("blueButton")
        self.gridLayout_3.addWidget(self.blueButton, 0, 1, 1, 1)
        self.yellowButton = QtWidgets.QPushButton(self.centralWidget)
        self.yellowButton.setMinimumSize(QtCore.QSize(100, 50))
        self.yellowButton.setObjectName("yellowButton")
        self.gridLayout_3.addWidget(self.yellowButton, 1, 0, 1, 1)
        self.redButton = QtWidgets.QPushButton(self.centralWidget)
        self.redButton.setMinimumSize(QtCore.QSize(100, 50))
        self.redButton.setObjectName("redButton")
        self.gridLayout_3.addWidget(self.redButton, 0, 0, 1, 1)
        self.orangeButton = QtWidgets.QPushButton(self.centralWidget)
        self.orangeButton.setMinimumSize(QtCore.QSize(100, 50))
        self.orangeButton.setObjectName("orangeButton")
        self.gridLayout_3.addWidget(self.orangeButton, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ColorSlider = QtWidgets.QSlider(self.centralWidget)
        self.ColorSlider.setMaximum(31)
        self.ColorSlider.setSliderPosition(0)
        self.ColorSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ColorSlider.setObjectName("ColorSlider")
        self.verticalLayout.addWidget(self.ColorSlider)
        self.myText = QtWidgets.QLabel(self.centralWidget)
        self.myText.setAlignment(QtCore.Qt.AlignCenter)
        self.myText.setObjectName("myText")
        self.verticalLayout.addWidget(self.myText)
        self.confirmButton = QtWidgets.QPushButton(self.centralWidget)
        self.confirmButton.setMinimumSize(QtCore.QSize(0, 50))
        self.confirmButton.setObjectName("confirmButton")
        self.verticalLayout.addWidget(self.confirmButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 6, 0, 1, 1)
        ColorOverrider.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ColorOverrider)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 224, 21))
        self.menuBar.setObjectName("menuBar")
        ColorOverrider.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(ColorOverrider)
        self.mainToolBar.setObjectName("mainToolBar")
        ColorOverrider.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(ColorOverrider)
        self.statusBar.setObjectName("statusBar")
        ColorOverrider.setStatusBar(self.statusBar)

        self.retranslateUi(ColorOverrider)
        QtCore.QMetaObject.connectSlotsByName(ColorOverrider)

    def retranslateUi(self, ColorOverrider):
        ColorOverrider.setWindowTitle(QtWidgets.QApplication.translate("ColorOverrider", "Color Overrider", None, -1))
        self.blueButton.setText(QtWidgets.QApplication.translate("ColorOverrider", "Blue", None, -1))
        self.yellowButton.setText(QtWidgets.QApplication.translate("ColorOverrider", "Yellow", None, -1))
        self.redButton.setText(QtWidgets.QApplication.translate("ColorOverrider", "Red", None, -1))
        self.orangeButton.setText(QtWidgets.QApplication.translate("ColorOverrider", "Orange", None, -1))
        self.myText.setText(QtWidgets.QApplication.translate("ColorOverrider", "Push below to confirm color", None, -1))
        self.confirmButton.setText(QtWidgets.QApplication.translate("ColorOverrider", "Select Color", None, -1))

        

       
if __name__ == "__main__":
    
    try:
        coWin.close()
    except:
        pass
        
    coWin = gMainWindow(parent=maya_main_window())
    coWin.show()