from pymel.core import *

class attrAdder:
    
    def __init__(self, titleName):
        self.win = window(title=titleName, width=400, height=200)
        self.mainLayout = columnLayout(adj=True, rs=5, co=('both', 5))
        self.confirmBtn = button(label="Confirm", command=self.AddAllAttributes)
        self.addMoreBtn = button(label="Add More Attributes", command=self.addRow)
        self.rowList = []
        self.layoutList = []
        self.addMoreBtn = None
        self.addRow()
        print self.rowList
        
        
        

    def addRow(self, *args):
        #addNewBtn = False
        #if self.addMoreBtn is not None:
        #    deleteUI(self.addMoreBtn)
        #    addNewBtn = True
        columnList = []
        form = formLayout(nd=100)
        t1=textField(pht="Long Name")
        t2=textField(pht="Nice Name")
        r1=radioButtonGrp(nrb=3, labelArray3=['Keyable','Displayable','Hidden'], vr=True)
        r2=radioButtonGrp(nrb=3, labelArray3=['Float','Integer','Enum'], vr=True)
        t3=textField(pht="Enum Values (':' delimited)")
        
        formLayout( form, edit=True, attachForm=[(t1, 'top', 5), (t1, 'left', 5), (t1, 'bottom', 5), 
                                                 (t2, 'bottom', 5), (t2, 'top', 5), 
                                                 (r1, 'top', 5), (r1, 'bottom', 5), 
                                                 (r2, 'top', 5), (r2, 'bottom', 5), 
                                                 (t3, 'right', 5), (t3,'top',5), (t3, 'bottom',5) ], 
                                     attachControl=[(t2, 'left',0,t1), 
                                                 (r1, 'right', 5, r2), (r1,'left',5,t2),
                                                 (r2, 'right', 5, t3)], 
                                     attachPosition=[(t1,'right', 5, 25), 
                                                 (t2,'right', 5, 50),
                                                 (t3, 'left', 5, 75)] )

        
        setParent('..')
        columnList.append(t1)
        columnList.append(t2)
        columnList.append(r1)
        columnList.append(r2)
        columnList.append(t3)
        self.rowList.append(columnList)
        self.layoutList.append(form)
        #if addNewBtn:
        #    self.addMoreBtn = button(label="Add More Attributes", command=self.addRow)
        
    def AddAllAttributes(self, *args):
        sel = ls(sl=True)
        for obj in sel:
            for row in self.rowList:
                lName = row[0].getText()
                nName = row[1].getText()
                display = row[2].getSelect()
                dSelect = row[3].getSelect()
                dType = None
                if dSelect == 1:
                    dType = 'float'
                elif dSelect == 2:
                    dType = 'short'
                elif dSelect == 3:
                    dType = 'enum'
                else:
                    dType = 'float'
                
                eName = row[4].getText()
                
                
                #print obj + "." + lName
                
                if display == 1 and dSelect != 3:
                    addAttr(ln = lName, nn = nName, at = dType, k=True)
                elif display == 2 and dSelect != 3:
                    addAttr(ln = lName, nn = nName, at = dType, k=False)
                    setAttr(obj + "." + lName, cb=True)
                elif display == 3 and dSelect != 3:
                    addAttr(ln = lName, nn = nName, at = dType, h=True)
                elif display == 1 and dSelect == 3:
                    addAttr(ln = lName, nn = nName, at = dType, k=True, en=eName)
                elif display == 2 and dSelect == 3:
                    addAttr(ln = lName, nn = nName, at = dType, k=False, en=eName)
                    setAttr(obj + "." + lName, cb=True)
                elif display == 3 and dSelect == 3:
                    addAttr(ln = lName, nn = nName, at = dType, h=True, en=eName)
                    
                #print row[0].getText() + " + " + row[1].getText() + " + " + str(row[2].getSelect()) + " + " + str(row[3].getSelect()) + " + " + row[4].getText() 
        
        for LO in self.layoutList:
            deleteUI(LO)
        #if self.addMoreBtn is not None:
        #    deleteUI(self.addMoreBtn)
        self.addRow()
        #self.addMoreBtn = button(label="Add More Attributes", command=self.addRow)
        
    def openWindow(self):
        self.win.show()
        
if __name__ == "__main__":
    if window(aAdd.win, exists=True):
        deleteUI(aAdd.win)
        
    aAdd = attrAdder("AddAttributes")
    aAdd.openWindow()
    