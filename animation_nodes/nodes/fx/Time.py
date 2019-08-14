import bpy
from bpy.props import *
from ... base_types import AnimationNode


class Time(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Time"
    bl_label = "Time"
    

    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Integer", "Start", "start",value=1)
        self.newInput("Integer", "End", "end",value=250)
        self.newInput("Integer", "Current", "current",value=bpy.context.scene.frame_current)
        self.newInput("Boolean", "Monitor","monitor",value=False,hide=True)
        self.newInput("Scene", "Scene", "scene",hide = True)
        self.newOutput("Integer", "Current", "current")
    


    def execute(self,on,start,end,current,monitor,scene):
        if on:
            if scene.frame_current != current:
                scene.frame_current=current
        
            if scene.frame_start != start:
                scene.frame_start=start
            
            if scene.frame_end != end:
                scene.frame_end=end
        else:
            if scene.frame_current != current and monitor:
                self.inputs["Current"].value=scene.frame_current
        return scene.frame_current