import bpy
from mathutils import Vector
from bpy.props import *
from ... base_types import AnimationNode

class GetFaceData(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_GetFaceData"
    bl_label = "Get Face Data"

    errorMessage = StringProperty()
    
    def create(self):
        self.newInput("Object", "Object","obj")
        self.newInput("Integer","ID","vid")
        self.newOutput("Float",'area','area')
        self.newOutput("Vector",'center','center')
        self.newOutput("Boolean",'hide','hide')
        self.newOutput("Integer", "index","index")
        self.newOutput("Integer","loop_start","loop_start")
        self.newOutput("Integer","loop_total","loop_total")
        self.newOutput("Integer","material_index","material_index")
        self.newOutput("Vector",'normal','normal')
        self.newOutput("Boolean",'select','select')
        self.newOutput("Boolean",'use_freestyle_mark','use_freestyle_mark')
        self.newOutput("Boolean",'use_smooth','use_smooth')
        self.newOutput("Boolean", "is Valid","n")
        
    def execute(self,obj,vid):
        self.errorMessage = ""
        if obj is None:
            return 0,Vector((0,0,0)),0,0,0,4,0,Vector((0,0,0)),0,0,0,False
        
        vaild=False
        if obj.mode == "EDIT":
            self.errorMessage = "Object is in edit mode"
        elif obj.type != "MESH":
            self.errorMessage = "Not Mesh"
        else:
            vaild=True
        try:
            ply=obj.data.polygons[vid]
            
            area=ply.area
            center=ply.center
            hide=ply.hide
            index=ply.index
            loop_start=ply.loop_start
            loop_total=ply.loop_total
            material_index=ply.material_index
            normal=ply.normal
            select=ply.select
            use_freestyle_mark=ply.use_freestyle_mark
            use_smooth=ply.use_smooth
            
            return area,center,hide,index,loop_start,loop_total,material_index,normal,select,use_freestyle_mark,use_smooth,vaild
        except:
            return 0,Vector((0,0,0)),0,0,0,4,0,Vector((0,0,0)),0,0,0,False

    def draw(self, layout):
        layout.prop(self, "mode", text = "")
        if self.errorMessage != "":
            layout.label(self.errorMessage, icon = "ERROR")
