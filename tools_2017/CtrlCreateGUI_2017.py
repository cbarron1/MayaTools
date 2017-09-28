from pymel.core import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as mui

def maya_main_window():
    main_window_ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QWidget)
      
class ctrlMainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        
        super(ctrlMainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.Tool)
        self.ui = Ui_ControlCreator()
        self.ui.setupUi(self)
        
        self.make_connections()
        
    def make_connections(self):
        
        self.ui.cageCtrlBtn.clicked.connect(lambda: self.createControl(1))
        self.ui.squareCtrlBtn.clicked.connect(lambda: self.createControl(2))
        self.ui.sphereCtrlBtn.clicked.connect(lambda: self.createControl(3))
        self.ui.visCtrlBtn.clicked.connect(lambda: self.createControl(4))
        self.ui.transCtrlBtn.clicked.connect(lambda: self.createControl(5))
        
    def createControl(self,ctrlType):
        
        if self.ui.ctrlNameTxt.toPlainText() != '':
            if ctrlType == 1:
                self.cubeCtrl(self.ui.ctrlNameTxt.toPlainText())
            elif ctrlType == 2:
                self.squareCtrl(self.ui.ctrlNameTxt.toPlainText())
            elif ctrlType == 3:
                self.sphereCtrl(self.ui.ctrlNameTxt.toPlainText())
            elif ctrlType == 4:
                self.visCtrl(self.ui.ctrlNameTxt.toPlainText())
            elif ctrlType == 5:
                self.translateCtrl(self.ui.ctrlNameTxt.toPlainText())
        else:
            confirmDialog(title="Create Control Error",message="New control must be given a name", button="OK")
        
    def visCtrl(self,ctrlName):
        upperVisCurve = curve(n="upperVisCurve",p=[(-2,0,0), (-1.333333,0,-0.5), (0,0,-1.5), (1.333333,0,-0.5), (2,0,0)],k=[0,0,0,1,2,2,2])
        lowerVisCurve = curve(n="lowerVisCurve",p=[(-2,0,0), (-1.333333,0,0.5), (0,0,1.5), (1.333333,0,0.5), (2,0,0)],k=[0,0,0,1,2,2,2])
        pupilVis = circle(n="pupilVis", r=0.8, nr=[0,1,0])
        emptyGrp = group(n=ctrlName, em=True)
    
        select(cl=True)
        select(listRelatives('upperVisCurve', c=True,s=True)[0],add=True)
        select(listRelatives('lowerVisCurve', c=True,s=True)[0],add=True)
        select(listRelatives('pupilVis', c=True,s=True)[0],add=True)
        select(emptyGrp, add=True)
        parent(r=True, s=True)
        
        delete(upperVisCurve)
        delete(lowerVisCurve)
        delete(pupilVis)
        select(emptyGrp)
        
    def translateCtrl(self,ctrlName):
        transCurve = curve(n='trans',d=1,p=[(-1,0,-1),(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1),(1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-1,0,-1)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

    def squareCtrl(self,ctrlName):
        squareCtrl = curve(n=ctrlName,d=1,p=[(-2,0,-2),(2,0,-2),(2,0,2),(-2,0,2),(-2,0,-2)],k=[0,1,2,3,4])
        
    def cubeCtrl(self,ctrlName):
        self.squareCtrl('cageSquare_01') 
        rotate(90,x=True) 
        move(0,0,-2) 
        makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=True)
        
        self.squareCtrl('cageSquare_02')
        rotate(90,x=True)
        move(0,0,2)
        makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=True)
        
        self.squareCtrl('cageSquare_03')
        move(0,2,0)
        makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=True)
        
        self.squareCtrl('cageSquare_04')
        move(0,-2,0)
        makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=True)  
        
        emptyGrp = group(em=True,n=ctrlName)
        
        select(cl=True)
        select(listRelatives('cageSquare_01', c=True,s=True)[0],add=True)
        select(listRelatives('cageSquare_02', c=True,s=True)[0],add=True)
        select(listRelatives('cageSquare_03', c=True,s=True)[0],add=True)
        select(listRelatives('cageSquare_04', c=True,s=True)[0],add=True)
        select(ctrlName,add=True)
        parent(r=True,s=True)
        
        delete('cageSquare_01')
        delete('cageSquare_02')
        delete('cageSquare_03')
        delete('cageSquare_04')
        
        select(emptyGrp)
        
    def sphereCtrl(self,ctrlName):
        circle(n='sphereCtrl_01',nr=[0,1,0])
        
        circle(n='sphereCtrl_02',nr=[0,1,0])
        rotate(90,x=True)
        makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=True)
        
        circle(n='sphereCtrl_03',nr=[0,1,0])
        rotate(90,z=True)
        makeIdentity(apply=True,t=True,r=True,s=True,n=0,pn=True)
        
        emptyGrp = group(em=True,n=ctrlName)
        
        select(cl=True)
        select(listRelatives('sphereCtrl_01', c=True,s=True)[0],add=True)
        select(listRelatives('sphereCtrl_02', c=True,s=True)[0],add=True)
        select(listRelatives('sphereCtrl_03', c=True,s=True)[0],add=True)
        
        select(ctrlName,add=True)
        parent(r=True,s=True)
        
        delete('sphereCtrl_01')
        delete('sphereCtrl_02')
        delete('sphereCtrl_03')
        
        select(emptyGrp)



################################
###                          ###
###      Gui Definition      ###
###                          ###
################################

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ControlCreator(object):
    def setupUi(self, ControlCreator):
        ControlCreator.setObjectName("ControlCreator")
        ControlCreator.resize(306, 521)
        self.centralwidget = QtWidgets.QWidget(ControlCreator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 64))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.ctrlNameTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.ctrlNameTxt.setMaximumSize(QtCore.QSize(16777215, 64))
        self.ctrlNameTxt.setObjectName("ctrlNameTxt")
        self.verticalLayout_2.addWidget(self.ctrlNameTxt)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.visCtrlBtn = QtWidgets.QPushButton(self.centralwidget)
        self.visCtrlBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("testIcon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.visCtrlBtn.setIcon(icon)
        self.visCtrlBtn.setIconSize(QtCore.QSize(128, 128))
        self.visCtrlBtn.setObjectName("visCtrlBtn")
        self.gridLayout.addWidget(self.visCtrlBtn, 0, 0, 1, 1)
        self.sphereCtrlbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sphereCtrlbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("testIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sphereCtrlbtn.setIcon(icon1)
        self.sphereCtrlbtn.setIconSize(QtCore.QSize(128, 128))
        self.sphereCtrlbtn.setObjectName("sphereCtrlbtn")
        self.gridLayout.addWidget(self.sphereCtrlbtn, 0, 1, 1, 1)
        self.squareCtrlBtn = QtWidgets.QPushButton(self.centralwidget)
        self.squareCtrlBtn.setMinimumSize(QtCore.QSize(128, 128))
        self.squareCtrlBtn.setObjectName("squareCtrlBtn")
        self.gridLayout.addWidget(self.squareCtrlBtn, 1, 0, 1, 1)
        self.transCtrlBtn = QtWidgets.QPushButton(self.centralwidget)
        self.transCtrlBtn.setMinimumSize(QtCore.QSize(128, 128))
        self.transCtrlBtn.setObjectName("transCtrlBtn")
        self.gridLayout.addWidget(self.transCtrlBtn, 1, 1, 1, 1)
        self.cageCtrlBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cageCtrlBtn.setMinimumSize(QtCore.QSize(128, 128))
        self.cageCtrlBtn.setObjectName("cageCtrlBtn")
        self.gridLayout.addWidget(self.cageCtrlBtn, 2, 0, 1, 1)
        self.sphereCtrlBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sphereCtrlBtn.setMinimumSize(QtCore.QSize(128, 128))
        self.sphereCtrlBtn.setObjectName("sphereCtrlBtn")
        self.gridLayout.addWidget(self.sphereCtrlBtn, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        ControlCreator.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlCreator)
        QtCore.QMetaObject.connectSlotsByName(ControlCreator)

    def retranslateUi(self, ControlCreator):
        ControlCreator.setWindowTitle(QtWidgets.QApplication.translate("ControlCreator", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ControlCreator", "New Control Name", None, -1))
        self.squareCtrlBtn.setText(QtWidgets.QApplication.translate("ControlCreator", "Square", None, -1))
        self.transCtrlBtn.setText(QtWidgets.QApplication.translate("ControlCreator", "Translate", None, -1))
        self.cageCtrlBtn.setText(QtWidgets.QApplication.translate("ControlCreator", "Cage", None, -1))
        self.sphereCtrlBtn.setText(QtWidgets.QApplication.translate("ControlCreator", "Sphere", None, -1))


if __name__ == "__main__":
    try:
        ctrlWin.close()
    except:
        pass
        
    ctrlWin = ctrlMainWindow(parent=maya_main_window())
    ctrlWin.show()