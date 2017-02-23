from pymel.core import *
from PySide.QtCore import *
from PySide.QtGui import *
from shiboken import wrapInstance
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

from PySide import QtCore, QtGui

class Ui_BatchRename(object):
    def setupUi(self, BatchRename):
        BatchRename.setObjectName("BatchRename")
        BatchRename.resize(384, 232)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(BatchRename.sizePolicy().hasHeightForWidth())
        BatchRename.setSizePolicy(sizePolicy)
        BatchRename.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(BatchRename)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(10, 10, 10, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.filepathBox = QtGui.QLineEdit(BatchRename)
        self.filepathBox.setMinimumSize(QtCore.QSize(240, 30))
        self.filepathBox.setObjectName("filepathBox")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.filepathBox)
        self.browseButton = QtGui.QPushButton(BatchRename)
        self.browseButton.setMinimumSize(QtCore.QSize(100, 30))
        self.browseButton.setObjectName("browseButton")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.browseButton)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(10, 10, 10, -1)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.extensionBox0 = QtGui.QLineEdit(BatchRename)
        self.extensionBox0.setMinimumSize(QtCore.QSize(160, 30))
        self.extensionBox0.setObjectName("extensionBox0")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.extensionBox0)
        self.curExLabel = QtGui.QLabel(BatchRename)
        self.curExLabel.setWordWrap(True)
        self.curExLabel.setObjectName("curExLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.curExLabel)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.renameButton = QtGui.QPushButton(BatchRename)
        self.renameButton.setMinimumSize(QtCore.QSize(180, 50))
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(BatchRename)
        QtCore.QMetaObject.connectSlotsByName(BatchRename)

    def retranslateUi(self, BatchRename):
        BatchRename.setWindowTitle(QtGui.QApplication.translate("BatchRename", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.filepathBox.setPlaceholderText(QtGui.QApplication.translate("BatchRename", "File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("BatchRename", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.extensionBox0.setPlaceholderText(QtGui.QApplication.translate("BatchRename", "Current Extension (misplaced)", None, QtGui.QApplication.UnicodeUTF8))
        self.curExLabel.setText(QtGui.QApplication.translate("BatchRename", "i.e. the \"ext\" in  \"filename.ext.0001\"", None, QtGui.QApplication.UnicodeUTF8))
        self.renameButton.setText(QtGui.QApplication.translate("BatchRename", "Batch Rename", None, QtGui.QApplication.UnicodeUTF8))


        
if __name__=="__main__":
    
    try:
        renameWin.close()
    except:
        pass
        
    renameWin = renameWidget(parent=maya_main_window())
    renameWin.show() 