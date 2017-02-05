from pymel.core import *

class fileReader:
    
    def __init__(self,titleName):
        self.filePathName = None
        self.win = window(title=titleName, width=300, height=100)
        self.layout1 = columnLayout()
        self.fileButton = button(label="choose file",command=self.readFilePath)

    def readFilePath(self,*args):
        self.filePathName = fileDialog2(fm=1)
        self.filePathName = self.filePathName[0]

    def openWindow(self):
        self.win.show()        

class uiConverter(fileReader):
    
    def __init__(self):
        fileReader.__init__(self,"UI Converter")
        self.textInput = textField("inputText")
        self.convertButton = button(label="Convert Chosen File", command=self.convertFile)
        
    def convertFile(self,*args):
        if self.filePathName is not None and self.textInput.getText()!='':
            import sys, pprint
            from pysideuic import compileUi
            
            
            drive, path = os.path.splitdrive(self.filePathName)
            path, filename = os.path.split(path)
            outFilePath = drive + path + "/" + self.textInput.getText()
            #print ("%s , %s , %s" % (drive,path,filename))

            
            pyfile = open(outFilePath,'w')
            compileUi(self.filePathName,pyfile, False, 4, False)
            pyfile.close()
        elif self.textInput.getText()=='':
            print "No output Filename" 
        else:
            print "No File Selected"

uiCon = uiConverter()
uiCon.openWindow()

