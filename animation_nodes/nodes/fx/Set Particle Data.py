import bpy
from bpy.props import *
from ... events import propertyChanged
from mathutils import Vector,Quaternion
from ... base_types import AnimationNode

modeItems=[
    ("Birth","Birth Time","Distribute set birth time","",0),
    ("Die","Die Time","Distribute set die Time","",1),
    ("Life","Life Time","Distribute set lifeTime","",2),
    ("Location","Location","Distribute set location","",3),
    ("Rotation","Rotation","Distribute set rotation","",4),
    ("Size","Size","Distribute set size","",5),
    ("Velocity","Velocity","Distribute set velocity","",6),
    ("Angular","Angular Velocity","Distribute set angular velocity","",7),
]

class SetParticleData(bpy.types.Node, AnimationNode):
    bl_idname = "an_fx_SetParticleData"
    bl_label = "Set Particle Data"

    mode = EnumProperty(name = "Mode", default = "Location",items = modeItems, update = AnimationNode.refresh)
    
    def create(self):
        self.newInput("Boolean",'On','on')
        self.newInput("Particle System", "Source","source")
        self.newInput("Integer", "PID","pid")

        if self.mode=="Birth":
            self.newInput("Float",'birth_time','birth')
        
        if self.mode=="Die":
            self.newInput("Float",'die_time','die')
            
        if self.mode=="Life":
            self.newInput("Float",'lifetime','life')

        if self.mode=="Location":
            self.newInput("Vector",'location','loc')

        if self.mode=="Rotation":
            self.newInput("Quaternion",'rotation','rot')

        if self.mode=="Size":
            self.newInput("Float",'size','size',value=0.05)

        if self.mode=="Velocity":
            self.newInput("Vector",'velocity','vel')

        if self.mode=="Angular":
            self.newInput("Vector",'angular_velocity','ang')

    def draw(self, layout):
        layout.prop(self,"mode")

    def getExecutionFunctionName(self):
        if self.mode == "Birth":
            return "execute_Birth"
        
        elif self.mode == "Die":
            return "execute_Die"

        elif self.mode == "Life":
            return "execute_Life"

        elif self.mode == "Location":
            return "execute_Location"

        elif self.mode == "Rotation":
            return "execute_Rotation"

        elif self.mode == "Size":
            return "execute_Size"

        elif self.mode == "Velocity":
            return "execute_Velocity"

        elif self.mode == "Angular":
            return "execute_Angular"

    def execute_Birth(self,on,source,pid,birth):
        if source is None:
            return
        if on:
            source.particles[pid].birth_time=birth
    
    def execute_Die(self,on,source,pid,die):
        if source is None:
            return
        if on:
            source.particles[pid].die_time=die

    def execute_Life(self,on,source,pid,life):
        if source is None:
            return
        if on:
            source.particles[pid].lifetime=life

    def execute_Location(self,on,source,pid,loc):
        if source is None:
            return
        if on:
            source.particles[pid].location=loc
            
    def execute_Rotation(self,on,source,pid,rot):
        if source is None:
            return
        if on:
            source.particles[pid].rotation=rot

    def execute_Size(self,on,source,pid,size):
        if source is None:
            return
        if on:
            source.particles[pid].size=size
            
    def execute_Velocity(self,on,source,pid,vel):
        if source is None:
            return
        if on:
            source.particles[pid].velocity=vel
            
    def execute_Angular(self,on,source,pid,ang):
        if source is None:
            return
        if on:
            source.particles[pid].angular_velocity=ang


