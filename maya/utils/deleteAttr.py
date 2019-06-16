'''
Removes a specifically defined attribute
'''
import sys
import pymel.core as pm

sel = pm.selected()
attrName = 'overrideName'
for i in sel:
    pm.deleteAttr(i, at=attrName)
sys.__stdout__.write( str(attrName)+ ' attribute removed!' + '\n')
print '\n' + str(attrName)+ ' == Attribute removed!' + '\n'