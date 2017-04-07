from pymel.core import *

class renamer:
    
    def __init__(self):
        
        self.selected = []
        self.baseName = ""
        self.prefix=""
        self.suffix=""
        self.zeroPadding = 1
        
    def renameObjects(self,base=None,pref=None,suff=None,padd=None):
        
        self.selected = ls(sl=True)
        print self.selected
        
        if (len(self.selected) == 0):
            print "No objects selected"
        else:
            if base is None:
                print "Must enter base name"
            else:
                print "Rename"
                
if __name__ == "__main__":
    rT = renamer()
    rT.renameObjects()