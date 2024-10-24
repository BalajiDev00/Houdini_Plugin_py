import hou
import os

def py():
    import hou
    node = hou.pwd()
    if not node.parm("myStringInput"):
        result = hou.ui.readInput("Enter your custom text:", buttons=("OK", "Cancel"))
        hou.session.result = result[1]


def createObjects():
    obj_level = hou.node('/obj')

    geo = obj_level.createNode('geo','TextTo3D')

    font = geo.createNode('font',"Text")

    text =hou.session.result

    font.parm("text").set(text)


    polyex =  geo.createNode('polyextrude::2.0','Extrude')
    polyex.setInput(0,font)

    polyex.parm('dist').set(0.3)

    polyex.parm('outputback').set(1)

    div = geo.createNode('divide','Divide')
    div.setInput(0,polyex)


    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "exported_geometry.obj")

    rop_geo = geo.createNode("rop_geometry", "ExportGeometry")
    rop_geo.setInput(0,div)

    rop_geo.parm("sopoutput").set(output_file)
    rop_geo.parm("execute").pressButton()

def main():
    py()
    createObjects()
