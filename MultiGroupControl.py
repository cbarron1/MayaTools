#   This script will take all selected objects
#   and place them within individual group
#   hierarchies. Used mainly for controls that
#   have external controls and expressions 
#   modifying them (e.g. fingers with master hand controls
#       as well as individual joint controls)

from pymel.core import *

selected = ls(sl=True)

if not selected:
    print "empty blah"
else:
    for cntrl in selected:       
        orig = cntrl
        new1 = orig + "_grp"
        new2 = orig + "_align_grp"
        group(em=True, name=new1)
        group(em=True, name=new2)
        parent(cntrl,new1)
        parent(new1,new2)
