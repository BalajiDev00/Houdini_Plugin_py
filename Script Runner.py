import hou 
import imp

filename=hou.session.pathPyG
pyfile = hou.session.pyfileG

inputs = hou.ui.readInput("Script Refresh")
module = __import__(inputs[1])
imp.reload(module)

hou.ui.displayMessage(f" Reload module {inputs[1]} Successfully! ")
