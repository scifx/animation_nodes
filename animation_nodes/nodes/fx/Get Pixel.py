import bpy
from mathutils import Color
from ... base_types import AnimationNode

class GetPixel(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_GetPixel"
    bl_label = "Get Pixel"
            
    def create(self):
        self.newInput("Boolean", "On","on")
        self.newInput("Text", "Image","pic")
        self.newInput("Integer", "ID","pid")
        self.newOutput("Color", "color","c")
        self.newOutput("Boolean", "is Vaild","vaild")

    
    def execute(self,on,pic,pid):
        if pic=="":
            return [0,0,0,0],False
        if on:
            try:
                cd=[]
                ps=bpy.data.images[pic].pixels
                for i in range(4):
                    cd.append(ps[pid*4+i])
                return cd,True
            except:
                return [0,0,0,0],False
        else:
            return [0,0,0,0],False
