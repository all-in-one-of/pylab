'''
Removes a specifically defined attribute
'''
import sys
import pymel.core as pm

sel = pm.selected()
attrName = 'newName'
for i in sel:
    pm.deleteAttr(i, at=attrName)
sys.__stdout__.write( str(attrName)+ '完成しました!' + '\n')
print ('\n' + str(attrName)+ ' == 削りました!' + '\n')