"""
[summary]
"""
# Creates a foder structure with empty null groups

#Import Maya commands
import maya.cmds as cmds

def UI (*args):
    #Check to see if window exists
    if cmds.window("Toolbar", exists = True):
        cmds.deleteUI("Toolbar")

    #Creates UV Tools window
    tool = cmds.window("Toolbar", sizeable = False)
    buttonForm = cmds.formLayout( width=300, height=15, parent = tool)
    cmds.button( parent = buttonForm, label="folderStructure", command="GroupStruct.folderStructure('tempParentName')")

def folderStructure (*args):
    """
    docstring here
        :param *args: 
    """
    #Create temporary parent group
    nameInput = cmds.textField(query = True, text = True)
    parentName = nameInput
    cmds.group( em=True, name = nameInput )

    #Lists A specified set of names for the groups to be created

    groupName = ["GEO", "LIGHTS", "CAMERAS", "CURVES", "CONTROLS", "LOCS", "SKY", "REF", "UV", "DONE"]
    for index in range(len(groupName)):
        cmds.group( em=True, name = groupName[index] )
        cmds.parent (groupName[index], parentName)
    cmds.select (parentName, replace=True)

def FStrucUI (folderStructure):
    """
    docstring here
        :param folderStructure: 
    """
    if cmds.window("FolderStructure", exists = True):
        cmds.deleteUI("FolderStructure")

    folderStructureWindow = cmds.window("FolderStructure", title = "Folder Structure" + " " + "1.0", w = 150, h = 60, mnb = True, mxb = False,  sizeable = False)
    structLayout = cmds.rowColumnLayout( width=300, height=60, parent = folderStructureWindow, columnAlign=(1, "center"), numberOfColumns=1)
    cmds.separator( height=10, visible=False )
    cmds.button(width = 320, parent = structLayout, label="Create folder structure", command = folderStructure )
    cmds.separator( height=10, visible=False )
    cmds.showWindow()




























# Run this: folderStructure (name="PROD_A")
