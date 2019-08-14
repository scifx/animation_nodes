import bpy
import os,pickle
from bpy.props import *
from ... base_types import AnimationNode

WriterItems=[
    ("Text","Text","Read Stand Text","",0),
    ("Pickle","Pickle","Read Python Pickle","",1),
]

class FileWriter(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_FileWriter"
    bl_label = "File Writer"
    
    mode = EnumProperty(name = "Mode", default = "Text",items = WriterItems, update = AnimationNode.refresh)

    errorMessage = StringProperty()
    
    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Boolean", "Append","Append",value=False,hide=True)
        self.newInput("Text", "Path","path")
        self.newInput("Text", "File","file",value="data.txt")
        self.newInput("Generic", "Message","msg")
        if self.mode=="Text":
            self.newInput("Text", "Encoding","encoding",value="utf-8")
        if self.mode=="Pickle":
            self.newInput("Integer",'PMode','pmode',min=0,max=3)
        self.newOutput("Boolean",'isDone','isdone')

    def draw(self, layout):
        layout.prop(self,"mode")
    
    def getExecutionFunctionName(self):
        if self.mode == "Text":
            return "execute_Text"
        
        elif self.mode == "Pickle":
            self.inputs["Append"].hide=True
            return "execute_Pickle"
    

    def execute_Text(self,on,Append,path,file,msg,encoding):
        if path == "":
            self.errorMessage=""
            return
        if on:
            if os.path.isdir(path):
                try:
                    Path=path+"/"+file
                    mode="w"
                    if Append:
                        mode="a"
                    with open(Path, mode) as f:
                        f.write(msg)
                        return True
                    self.errorMessage="Successed"
                except:
                    self.errorMessage="Failed"
            else:
                self.errorMessage="Failed"
    
    def execute_Pickle(self,on,Append,path,file,msg,pmode):
        if path == "":
            self.errorMessage=""
            return
        if on:
            if os.path.isdir(path):
                try:
                    Path=path+"/"+file
                    with open(Path, "wb") as f:
                        pickle.dump(msg,f,pmode)
                        return True
                    self.errorMessage="Successed"
                except:
                    self.errorMessage="Failed"
                    print("Error")
            else:
                self.errorMessage="Failed"