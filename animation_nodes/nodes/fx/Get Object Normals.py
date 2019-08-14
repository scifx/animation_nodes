import bpy
from mathutils import Vector
from bpy.props import *
from ... events import propertyChanged
from ... base_types import AnimationNode

modeItems=[
    ("Fn","Face","Distribute Get face normal","",0),
    ("Pn","Point","Distribute Get point normal","",1),
]

class GetObjNoramls(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_GetNormals"
    bl_label = "Get Object Normals"

    errorMessage = StringProperty()
    
    mode = EnumProperty(name = "Mode", default = "Fn",items = modeItems, update = AnimationNode.refresh)

    def check(self,obj):
        self.errorMessage = ""
        if obj is None:
            return Vector((0,0,0)),False
        
        vaild=False
        if obj.type != "MESH":
            self.errorMessage = "Not Mesh"
        else:
            vaild=True
        return vaild
    
    def create(self):
        self.newInput("Object", "Object","obj")
        self.newInput("Integer", "ID","vid")

        if self.mode=="Fn":
            self.newOutput("Vector", "Face normal","fn")
        else:
            self.newOutput("Vector", "Point normal","pn")

        self.newOutput("Boolean", "is Valid","n")
            
    def draw(self, layout):
        layout.prop(self,"mode")

    def getExecutionFunctionName(self):
        if self.mode == "Fn":
            return "execute_Fn"
        
        elif self.mode == "Pn":
            return "execute_Pn"

    def execute_Fn(self,obj,vid):
        foo=self.check(obj)
        try:
            fn=obj.data.polygons[vid].normal
            return fn,foo
        except:
            return Vector((0,0,0)),False
        
    def execute_Pn(self,obj,vid):
        foo=self.check(obj)
        #name=obj.name
        try:
            #pn=bpy.data.meshes[name].vertices[vid].normal
            pn=obj.data.vertices[vid].normal
            
            return pn,foo
        except:
            return Vector((0,0,0)),False
        
        
    def draw(self, layout):
        layout.prop(self, "mode", text = "")
        if self.errorMessage != "":
            layout.label(self.errorMessage, icon = "ERROR")
