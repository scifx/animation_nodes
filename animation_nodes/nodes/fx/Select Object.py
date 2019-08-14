import bpy
from ... base_types import AnimationNode

class SelectObject(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_SelectObj"
    bl_label = "Select Object"
    
    def create(self):
        self.newInput("Boolean", "On","on")
        self.newInput("Boolean",'Active','active')
        self.newInput("Object", "Object","obj")

        
    def execute(self,on,active,obj):
        if obj is None:
            return
        if on:
            obj.select_set(True)
        else:
            obj.select_set(False)
        if active:
            bpy.context.view_layer.objects.active=obj