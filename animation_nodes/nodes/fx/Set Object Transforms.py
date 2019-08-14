import bpy
from mathutils import Vector
from bpy.props import *
from ... events import propertyChanged
from ... base_types import AnimationNode

modeItems=[
    ("Loc","location","Distribute set location","",0),
    ("Rot","Rotation","set rotation","",1),
    ("Scale","Scale","Distribute Set Scale","",2)
]

class SetObjTransform(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_SetObjTrans"
    bl_label = "Set Object Transforms"

    mode = EnumProperty(name = "Mode", default = "Loc",items = modeItems, update = AnimationNode.refresh)
    
    def create(self):
        self.newInput("Boolean", "On","on",value=True)
        self.newInput("Object", "Object","obj")

        if self.mode=="Loc":
            self.newInput("Vector", "Position","p")
        
        if self.mode=="Rot":
            self.newInput("Euler", "Rotation","r")
        
        if self.mode=="Scale":
            self.newInput("Vector", "Scale","s",value=Vector((1,1,1)))

    def draw(self, layout):
        layout.prop(self,"mode")
        
    def getExecutionFunctionName(self):
        if self.mode == "Loc":
            return "execute_Loc"
        
        elif self.mode == "Rot":
            return "execute_Rot"
        
        elif self.mode == "Scale":
            return "execute_Scale"

    def execute_Loc(self,on,obj,p):
        if obj is None:
            return
        if on:
            obj.location=p
        
    def execute_Rot(self,on,obj,r):
        if obj is None:
            return
        if on:
            obj.rotation_euler=r
        
    def execute_Scale(self,on,obj,s):
        if obj is None:
            return
        if on:
            obj.scale=s
