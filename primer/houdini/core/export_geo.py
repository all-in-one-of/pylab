import hou

def export_geo():
    path = "D:/git-dev/pylab/primer/houdini/test_data/export/"
    obj = hou.node("/obj")
    children = obj.children()

    # print (children)

    for node in children:
        node_name = node.name()
        file_path = path + node_name + ".fbx"
        node.parm("sopoutput").set(file_path)
        node.parm("execute").pressButton()
        print (file_path)