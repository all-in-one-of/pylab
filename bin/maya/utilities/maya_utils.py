"""
Various little snippets of actions on maya nodes
"""

import pymel.core as pm


# List Shape Relatives
def get_shapes():
    """
    This gets the shape node of a selected transform
    :return: Shapes
    """
    sel = pm.ls(sl=True)
    shapes_list = []
    for s in sel:
        shapes = pm.listRelatives(s, shapes=True)
        add_shapes = shapes_list.append(shapes)
        print(add_shapes)
    print(shapes_list)


# Group each
def group_each(new_name='sm_1'):
    """
    This function takes the selected object and groups each them
    :param name: Name of the group
    :return: name arg
    """
    sel = pm.ls(sl=True)
    for g in sel:
        pm.group(g, name=new_name)


# Rename selection
def replace_name(name='geo', new_name='new_name'):
    """
        This function takes the selected object and groups each them
    :param name:
    :param new_name:
    :return:
    """
    sel = pm.ls(sl=True)
    for g in sel:
        new_name = g.replace(name, new_name)
        pm.rename(g, new_name)
