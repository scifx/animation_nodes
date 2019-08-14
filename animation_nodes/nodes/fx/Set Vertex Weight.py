import bpy
from bpy.props import *
from ... base_types import AnimationNode

class SetVertexWeight(bpy.types.Node, AnimationNode):

    bl_idname = "an_fx_SetVertexWeight"
    bl_label = "Set Vertex Weight"

    errorMessage = StringProperty()

    def create(self):
        self.newInput("Boolean", "On","on",value=True)
        self.newInput("Object","Object","obj")
        self.newInput("Integer","Group Index","vg")
        self.newInput("Integer","ID","vid")
        self.newInput("Float","Weight","wg")

    def execute(self,on,obj,vg,vid,wg):
        self.errorMessage=""
        if obj is None:
            return
        if on:
            if obj.mode == "EDIT":
                self.errorMessage = "Object is in edit mode"
            elif obj.type != "MESH":
                self.errorMessage = "Not Mesh"
            else:
                try:
                    obj.vertex_groups[vg].add([vid],wg,'REPLACE')
                except:
                    self.errorMessage = "Group not found or out of Index"
            
    def draw(self, layout):
        layout.prop(self, "mode", text = "")
        if self.errorMessage != "":
            layout.label(self.errorMessage, icon = "ERROR")
