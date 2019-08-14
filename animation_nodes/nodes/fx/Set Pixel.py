import bpy
from mathutils import Vector
from ... base_types import AnimationNode

class SetPixel(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_SetPixel"
    bl_label = "Set Pixel"
    
    def create(self):
        self.newInput("Boolean", "On","on")
        self.newInput("Text", "Image","pic")
        self.newInput("Color", "color","cd")
        self.newInput("Integer", "ID","pid")

        
    def execute(self,on,pic,cd,pid):
        if pic =="":
            return
        if on:
            try:
                ps=bpy.data.images[pic].pixels
                for i in range(4):
                    ps[pid*4+i]=cd[i]
            except:
                pass
