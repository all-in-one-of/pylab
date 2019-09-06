Module Index
============

Highlighted Code
-----------------
``You can use backticks for showing highlighted code.``

Code Blocks wiht Line Numbers
-----------------------------
.. code-block:: python
    :linenos:
    

    def addAttr(attrName, niceName):
        """
        Adds a bool attr to the currewntly selected node.
        """
        sel = pm.ls(sl=True)
        for i in sel:
            pm.addAttr(i,ln=attrName, nn=niceName, dt='bool')
            pm.setAttr(i,lock=True)
        sys.__stdout__.write( str(attrName) + ' 完成しました!' + '\n')
        print ('\n' + str(attrName) + ' == 含みました!' + '\n')

Single Literal Block of Code
----------------------------

Code example::

    for i in sel:
        pm.addAttr(i,ln=attrName, nn=niceName, dt='bool')
        pm.setAttr(i,lock=True)


Code Blocks
-----------
.. code-block:: python

    def addAttr(attrName, niceName):
        """
        Adds a bool attr to the currewntly selected node.
        """
        sel = pm.ls(sl=True)
        for i in sel:
            pm.addAttr(i,ln=attrName, nn=niceName, dt='bool')
            pm.setAttr(i,lock=True)
        sys.__stdout__.write( str(attrName) + ' 完成しました!' + '\n')
        print ('\n' + str(attrName) + ' == 含みました!' + '\n')


Notes
-----
.. note::
    See the docs


Warnings
--------
.. warning::
    This is a warning
