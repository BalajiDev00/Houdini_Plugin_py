import hou 
import imp

filename=hou.session.pathPyG
pyfile = hou.session.pyfileG

inputs = hou.ui.readInput("Run Function :")
split = inputs[1].split(" ")

for i,values in enumerate(split,start=0):
    function_to_run = getattr(pyfile,values)
    print(values)
    function_to_run()

hou.ui.displayMessage(f" Successfull! ")
