import bpy
from bpy.props import *
from ... base_types import AnimationNode

modeItems=[
    ("Time","Time","Active by time","",0),
    ("Monitor","Monitor","Active by data","",1),
]

class Clipboard(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Activator"
    bl_label = "Activate"

    foo = BoolProperty(default = True)
    old = StringProperty(default = "Generic", update = AnimationNode.refresh)

    mode = EnumProperty(name = "Mode", default = "Time",items = modeItems, update = AnimationNode.refresh)
    
    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        if self.mode=="Time":
            self.newInput("Integer", "Start","start",value=False)
            self.newInput("Integer",'End','end')
        
        if self.mode=="Monitor":
            self.newInput("Generic",'Data','data')
            # self.newOutput("Generic",'Old','old')

        self.newInput("Integer", "Time","time")
        self.newInput("Scene", "Scene", "scene",hide = True)
        self.newOutput("Boolean", "On","on",value=False)

            
    def draw(self, layout):
        layout.prop(self,"mode")

    def getExecutionFunctionName(self):
        if self.mode == "Time":
            return "execute_Time"
        
        elif self.mode == "Mointor":
            return "execute_Monitor"

    def execute_Time(self,on,start,end,time,scene):
        #自动时间
        if self.inputs["Time"].isUnlinked:
            time=scene.frame_current
        if on:
            if time>=start and time<=end:
                return True
            else:
                return False
        else:
            return False

    def execute_Monitor(self,on,data,scene):
        print(data)
        
        if data is None:
            return
        if not self.inputs["data"].isUnlinked:
            self.old=data
            print("old: ",old)
        if on:
            if data==self.old:
                return False
            else:
                self.old=data
                return True

