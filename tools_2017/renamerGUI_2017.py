from pymel.core import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as mui

def maya_main_window():
    main_window_ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QWidget)
    
class renamerGUI(QDialog):
    
    def __init__(self, parent=None):
        
        super(renamerGUI, self).__init__(parent)
        self.setWindowFlags(Qt.Tool)
        self.ui = Ui_Renamer()
        self.ui.setupUi(self)

        self.ui.baseInput.setPlaceholderText("New Base Name")
        self.ui.prefixInput.setPlaceholderText("New Prefix")
        self.ui.suffixInput.setPlaceholderText("New Suffix")
        
        self.ui.baseCheck.setChecked(True)

        self.ui.prefixInput.setEnabled(False)
        self.ui.suffixInput.setEnabled(False)

        self.ui.zeroPadBox.setEnabled(False)
        self.ui.startNumBox.setEnabled(False)
        
        self.make_connections()
        
    def make_connections(self):
        
        #self.ui.numObjCheck.stateChanged.connect(self.check_box_changed)
        self.ui.baseCheck.stateChanged.connect(self.base_box_changed)
        self.ui.prefixCheck.stateChanged.connect(self.pref_box_changed)
        self.ui.suffixCheck.stateChanged.connect(self.suff_box_changed)
        self.ui.numObjCheck.stateChanged.connect(self.num_box_changed)
            
        self.ui.renameBtn.clicked.connect(self.rename_objects)

    ############################
    ###  Callback Functions  ###
    ############################
    def base_box_changed(self, int):

        if self.ui.baseCheck.isChecked():
            self.ui.baseInput.setEnabled(True)
        else:
            self.ui.baseInput.setEnabled(False)

    def pref_box_changed(self, int):

        if self.ui.prefixCheck.isChecked():
            self.ui.prefixInput.setEnabled(True)
        else:
            self.ui.prefixInput.setEnabled(False)

    def suff_box_changed(self, int):

        if self.ui.suffixCheck.isChecked():
            self.ui.suffixInput.setEnabled(True)
        else:
            self.ui.suffixInput.setEnabled(False)

    def num_box_changed(self, int):

        if self.ui.numObjCheck.isChecked():
            self.ui.zeroPadBox.setEnabled(True)
            self.ui.startNumBox.setEnabled(True)
        else:
            self.ui.zeroPadBox.setEnabled(False)
            self.ui.startNumBox.setEnabled(False)

    def rename_objects(self):

        sel = ls(sl=True)

        newBase = ""
        newPref = ""
        newSuff = ""

        addBase = True
        addPref = False
        addSuff = False
        addNum = False

        numberExt = "_"

        if self.ui.baseCheck.isChecked():
            newBase = self.ui.baseInput.text()
            addBase = True
        else:
            addBase = False


        if self.ui.prefixCheck.isChecked():
            newPref = self.ui.prefixInput.text()
            addPref = True
        else:
            addPref = False

        if self.ui.suffixCheck.isChecked():
            newSuff = self.ui.suffixInput.text()
            addSuff = True
        else:
            addSuff = False

        if self.ui.numObjCheck.isChecked():
            addNum = True
            zeroIter = 0
            while(zeroIter < self.ui.zeroPadBox.value()):
                numberExt += "0"
                zeroIter += 1
        else:
            addNum = False

        numIter = self.ui.startNumBox.value()
        for obj in sel:
            newName = obj
            if ((numIter == 10 or numIter == 100) and (self.ui.zeroPadBox.value() > 0)):
                numberExt = numberExt[:-1]
            if addBase:
                newName = newBase
            if addPref:
                newName = newPref + "_" + newName
            if addSuff:
                newName = newName + "_" + newSuff
            if addNum:
                newName = newName + numberExt + str(numIter)
                numIter += 1
            
            rename(obj,newName)

################################
###                          ###
###      Gui Definition      ###
###                          ###
################################

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Renamer(object):
    def setupUi(self, Renamer):
        Renamer.setObjectName("Renamer")
        Renamer.resize(211, 343)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Renamer.sizePolicy().hasHeightForWidth())
        Renamer.setSizePolicy(sizePolicy)
        Renamer.setMinimumSize(QtCore.QSize(211, 343))
        Renamer.setMaximumSize(QtCore.QSize(211, 343))
        self.layoutWidget = QtWidgets.QWidget(Renamer)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 323))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.baseCheck = QtWidgets.QCheckBox(self.layoutWidget)
        self.baseCheck.setObjectName("baseCheck")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.baseCheck)
        self.baseInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.baseInput.setObjectName("baseInput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.baseInput)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.suffixCheck = QtWidgets.QCheckBox(self.layoutWidget)
        self.suffixCheck.setObjectName("suffixCheck")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.suffixCheck)
        self.prefixCheck = QtWidgets.QCheckBox(self.layoutWidget)
        self.prefixCheck.setObjectName("prefixCheck")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.prefixCheck)
        self.prefixInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.prefixInput.setObjectName("prefixInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prefixInput)
        self.suffixInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.suffixInput.setObjectName("suffixInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.suffixInput)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.numObjCheck = QtWidgets.QCheckBox(self.layoutWidget)
        self.numObjCheck.setObjectName("numObjCheck")
        self.verticalLayout.addWidget(self.numObjCheck)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(5, 5, 5, 5)
        self.formLayout_3.setHorizontalSpacing(20)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.zeroPadBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.zeroPadBox.setMinimumSize(QtCore.QSize(0, 25))
        self.zeroPadBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.zeroPadBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.zeroPadBox.setMaximum(5)
        self.zeroPadBox.setObjectName("zeroPadBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zeroPadBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.startNumBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.startNumBox.setMinimumSize(QtCore.QSize(0, 25))
        self.startNumBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.startNumBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startNumBox.setObjectName("startNumBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startNumBox)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.renameBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.renameBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.renameBtn.setObjectName("renameBtn")
        self.verticalLayout.addWidget(self.renameBtn)

        self.retranslateUi(Renamer)
        QtCore.QMetaObject.connectSlotsByName(Renamer)

    def retranslateUi(self, Renamer):
        Renamer.setWindowTitle(QtWidgets.QApplication.translate("Renamer", "Renamer", None, -1))
        self.baseCheck.setText(QtWidgets.QApplication.translate("Renamer", "Base  ", None, -1))
        self.suffixCheck.setText(QtWidgets.QApplication.translate("Renamer", "Suffix", None, -1))
        self.prefixCheck.setText(QtWidgets.QApplication.translate("Renamer", "Prefix", None, -1))
        self.numObjCheck.setText(QtWidgets.QApplication.translate("Renamer", "Number Objects", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Renamer", "Zero Padding", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Renamer", "Start Number", None, -1))
        self.renameBtn.setText(QtWidgets.QApplication.translate("Renamer", "Rename Objects", None, -1))


        

       
if __name__ == "__main__":
    
    try:
        renWin.close()
    except:
        pass
        
    renWin = renamerGUI(parent=maya_main_window())
    renWin.show()
