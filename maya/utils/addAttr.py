'''
Add a defined custom string attribute
'''

import pymel.core as pm
import sys


sel = pm.ls(sl=True)
attrName = 'overrideName'
niceName = 'Override Name'
for i in sel:
    i.addAttr(attrName,nn=niceName, dt='string')
sys.__stdout__.write( str(attrName) + ' attribute added!' + '\n')
print '\n' + str(attrName) + ' == Attribute added!' + '\n'
