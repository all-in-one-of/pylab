"""
project documentation
"""
import sys
import pymel.core as pm


def deleteAttr(name = 'enterName'):
    """
    deleteAttr [summary]
    
    :param name: [description], defaults to 'enterName'
    :type name: str, optional
    """
    sel = pm.selected()
    attrName = name
    for i in sel:
        pm.deleteAttr(i, at=attrName)
    sys.__stdout__.write( str(attrName)+ '完成しました!' + '\n')
    print ('\n' + str(attrName)+ ' == 削りました!' + '\n')