import bpy
import os,pickle
from bpy.props import *
from ... base_types import AnimationNode

ReaderItems=[
    ("Text","Text","Read Stand Text","",0),
    ("Pickle","Pickle","Read Python Pickle","",1),
]

class FileReader(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_FileReader"
    bl_label = "File Reader"
    
    mode = EnumProperty(name = "Mode", default = "Text",items = ReaderItems, update = AnimationNode.refresh)

    errorMessage = StringProperty()
    
    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Text", "Path","path")
        self.newInput("Text", "File","file",value="data.txt")
        if self.mode=="Text":
            self.newInput("Text", "Encoding","encoding",value="utf-8")
        self.newOutput("Generic",'Message','msg')

    def draw(self, layout):
        layout.prop(self,"mode")
    
    def getExecutionFunctionName(self):
        if self.mode == "Text":
            return "execute_Text"
        
        elif self.mode == "Pickle":
            return "execute_Pickle"
    

    def execute_Text(self,on,path,file,encoding):
        if path == "":
            self.errorMessage=""
            return
        if on:
            if os.path.isdir(path):
                try:
                    Path=path+"/"+file
                    with open(Path, "r", encoding = encoding) as f:
                        msg=f.read()
                        return msg
                    self.errorMessage="Successed"
                except:
                    self.errorMessage="Failed"
            else:
                self.errorMessage="Failed"
    
    def execute_Pickle(self,on,path,file):
        if path == "":
            self.errorMessage=""
            return
        if on:
            if os.path.isdir(path):
                try:
                    Path=path+"/"+file
                    with open(Path, "rb") as f:
                        print(f)
                        msg=pickle.load(f)
                        print(msg)
                        return msg
                    self.errorMessage="Successed"
                except:
                    self.errorMessage="Failed"
                    print("Error")
            else:
                self.errorMessage="Failed"