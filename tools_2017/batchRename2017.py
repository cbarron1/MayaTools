from pymel.core import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
from maya import OpenMayaUI as mui

def maya_main_window():
    main_window_ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QWidget)
    
class renameWidget(QDialog):
    
    def __init__(self, parent=None):
        
        super(renameWidget, self).__init__(parent)
        self.setWindowFlags(Qt.Tool)
        self.ui = Ui_BatchRename()
        self.ui.setupUi(self)
        
        self.filePathName = None
        self.filename = None
        self.path = None
        
        self.makeConnections()
        
    def makeConnections(self):
        
        self.ui.browseButton.clicked.connect(self.readFilePath)
        self.ui.renameButton.clicked.connect(self.renameFiles)
        
        
    ##########################
    ### Callback Functions ###
    ##########################
    
    def readFilePath(self):
        import os
        
        tempFilePathName = fileDialog2(fm=1)
        if tempFilePathName is not None:
            self.filePathName = tempFilePathName[0]
            self.ui.filepathBox.setText(self.filePathName)
        
            self.filename = os.path.basename(self.filePathName)
            self.path = os.path.dirname(self.filePathName)
           
    def renameFiles(self):
        #print self.ui.extensionBox0.text()
        
        import glob, os
        
        if self.filePathName is not None and self.ui.extensionBox0.text() != "":
            splitName = self.filename.split('.')
            currentExt = self.ui.extensionBox0.text()
            newExt = currentExt
            #print splitName
       
            pattern = splitName[0] + '*.' + currentExt + '.*'
            
            for pathAndFileName in glob.iglob(os.path.join(self.path,pattern)):
                correctPath = pathAndFileName 
                base = os.path.basename(correctPath)
                splitPAF = base.split(currentExt + '.', 1)
                title = ''.join(splitPAF)
                os.rename(correctPath, os.path.join(self.path, title + '.' + newExt))
        elif self.filePathName is None:
            print "No file path given"
        elif self.ui.extensionBox0.text()=="":
            print "No extension given"
  
########################
###                  ###
###  GUI Definition  ###
###                  ###
########################

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BatchRename(object):
    def setupUi(self, BatchRename):
        BatchRename.setObjectName("BatchRename")
        BatchRename.resize(384, 232)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(BatchRename.sizePolicy().hasHeightForWidth())
        BatchRename.setSizePolicy(sizePolicy)
        BatchRename.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(BatchRename)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(10, 10, 10, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.filepathBox = QtWidgets.QLineEdit(BatchRename)
        self.filepathBox.setMinimumSize(QtCore.QSize(240, 30))
        self.filepathBox.setObjectName("filepathBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.filepathBox)
        self.browseButton = QtWidgets.QPushButton(BatchRename)
        self.browseButton.setMinimumSize(QtCore.QSize(100, 30))
        self.browseButton.setObjectName("browseButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.browseButton)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(10, 10, 10, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.extensionBox0 = QtWidgets.QLineEdit(BatchRename)
        self.extensionBox0.setMinimumSize(QtCore.QSize(160, 30))
        self.extensionBox0.setObjectName("extensionBox0")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.extensionBox0)
        self.curExLabel = QtWidgets.QLabel(BatchRename)
        self.curExLabel.setWordWrap(True)
        self.curExLabel.setObjectName("curExLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.curExLabel)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.renameButton = QtWidgets.QPushButton(BatchRename)
        self.renameButton.setMinimumSize(QtCore.QSize(180, 50))
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(BatchRename)
        QtCore.QMetaObject.connectSlotsByName(BatchRename)

    def retranslateUi(self, BatchRename):
        BatchRename.setWindowTitle(QtWidgets.QApplication.translate("BatchRename", "Dialog", None, -1))
        self.filepathBox.setPlaceholderText(QtWidgets.QApplication.translate("BatchRename", "File Path", None, -1))
        self.browseButton.setText(QtWidgets.QApplication.translate("BatchRename", "Browse", None, -1))
        self.extensionBox0.setPlaceholderText(QtWidgets.QApplication.translate("BatchRename", "Current Extension (misplaced)", None, -1))
        self.curExLabel.setText(QtWidgets.QApplication.translate("BatchRename", "i.e. the \"ext\" in  \"filename.ext.0001\"", None, -1))
        self.renameButton.setText(QtWidgets.QApplication.translate("BatchRename", "Batch Rename", None, -1))


        
if __name__=="__main__":
    
    try:
        renameWin.close()
    except:
        pass
        
    renameWin = renameWidget(parent=maya_main_window())
    renameWin.show() 