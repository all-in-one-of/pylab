import hou


def createGeo():
    obj = hou.node('/obj')
    geoNode = obj.createNode('geo', 'myGeo')
    box = geoNode.createNode('box', 'myCube')
    sphere = geoNode.createNode('sphere', 'mySphere')

    box.setInput(0,sphere,0)

    box.setDisplayFlag(1)
    box.setRenderFlag(1)