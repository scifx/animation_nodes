import bpy,serial,time,string
from bpy.props import *
from ... base_types import AnimationNode

class Serial(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Serial"
    bl_label = "Serial"

    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Text", "Com","com",value='com5')
        self.newInput("Integer",'bufsize','bufsize',value=9600)
        self.newInput("Float", "time out","timeout",value=0.05)
        self.newOutput("Gern", "Out", "out")

    def execute(self,on,com,bufsize,timeout):
        if com=="":
                return 
        if on:
            try:
                ser=serial.Serial(com,bufsize,timeout=timeout)
                data=ser.readline()
                try:
                    num=float(data)
                except:
                    pass
                return num
            except:
                pass