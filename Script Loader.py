import sys,os,importlib,hou  

def fetch_path():
    path = hou.ui.selectFile(title="Select File",file_type=hou.fileType.Any,pattern = "*.py")
    dict = os.path.dirname(path)
    base = os.path.basename(path)
    return dict,base
        
selected_path = fetch_path()
hou.session.pathPyG = selected_path

if selected_path not in sys.path:
    sys.path.append(selected_path[0])
    
pyfile = importlib.import_module(selected_path[1].split(".")[0])

hou.session.pyfileG = pyfile

hou.ui.displayMessage(f" Successfull Loaded module {pyfile}")