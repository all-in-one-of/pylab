'''
Add a defined custom string attribute
'''

import pymel.core as pm
import sys

def addAttr(attrName, niceName):
    sel = pm.ls(sl=True)
    for i in sel:
        pm.addAttr(i,ln=attrName, nn=niceName, dt='bool')
        pm.setAttr(i,lock=True)
    sys.__stdout__.write( str(attrName) + ' 完成しました!' + '\n')
    print ('\n' + str(attrName) + ' == 含みました!' + '\n')


addAttr('TestAttr', 'Test Attr')
