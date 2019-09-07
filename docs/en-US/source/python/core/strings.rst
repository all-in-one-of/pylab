Strings
=======


Working with Strings
--------------------
``You can use backticks for showing highlighted code.``


Formatting Strings
------------------
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

String Methods
--------------
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


Escape Sequences
----------------
.. note::
    See the docs


Special String Operators
------------------------
.. warning::
    This is a warning


String Format Operators
------------------------
.. warning::
    This is a warning


String Methods
--------------

To create a virtual environment for the project, run the following commands to
build the virtual environment, install the packages, and read back the virtual
environment's path:


Unicode
-------

To create a virtual environment for the project, run the following commands to
build the virtual environment, install the packages, and read back the virtual
environment's path: