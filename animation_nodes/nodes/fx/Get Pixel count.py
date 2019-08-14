import bpy
from bpy.props import *
from ... base_types import AnimationNode

class GetPixelsCount(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_GetPixelCount"
    bl_label = "Get Pixel Count"

    errorMessage = StringProperty()
    
    def create(self):
        self.newInput("Text", "Image","pic",value="")
        self.newOutput("Integer", "pixel count","pc")
    
    def execute(self,pic):
        if pic=="":
            self.errorMessage = ""
            return
        try:
            pc=len(bpy.data.images[pic].pixels)/4
            
            self.errorMessage = ""
            
            return pc
        except:
            self.errorMessage = "Image not Found"
            return
        
    def draw(self, layout):
        layout.prop(self, "mode", text = "")
        if self.errorMessage != "":
            layout.label(self.errorMessage, icon = "ERROR")
