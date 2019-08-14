import bpy
from bpy.props import *
from ... base_types import AnimationNode

modeItems=[
    ("Get","Get","get Clipboard","",0),
    ("Set","Set","set Clipboard","",1),
]
class Clipboard(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Clipboard"
    bl_label = "Clipboard"

    mode = EnumProperty(name = "Mode", default = "Get",items = modeItems, update = AnimationNode.refresh)
    
    def create(self):
        if self.mode=="Get":
            self.newOutput("Text",'Message','Out_Msg')
        
        if self.mode=="Set":
            self.newInput("Boolean", "On","on",value=False)
            self.newInput("Text",'Message','In_Msg')
            
    def draw(self, layout):
        layout.prop(self,"mode")

    def getExecutionFunctionName(self):
        if self.mode == "Get":
            return "execute_GetMsg"
        
        elif self.mode == "Set":
            return "execute_SetMsg"

    def execute_GetMsg(self):
        return bpy.data.window_managers["WinMan"].clipboard

    def execute_SetMsg(self,on,In_Msg):
        if on:
            bpy.data.window_managers["WinMan"].clipboard=In_Msg
