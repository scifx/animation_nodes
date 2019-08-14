import bpy
from mathutils import Vector,Quaternion
from bpy.props import *
from ... base_types import AnimationNode

class GetParticleData(bpy.types.Node, AnimationNode):
    bl_idname = "an_fx_GetParticleData"
    bl_label = "Get Particle Data"

    def create(self):
        self.newInput("Particle System", "Source","source")
        self.newInput("Integer", "PID","pid")
        self.newInput("Scene", "Scene", "scene",hide = True)
        self.newOutput("Text",'alive_state','alive')
        self.newOutput("Float",'birth_time','birth')
        self.newOutput("Float",'age','age')
        self.newOutput("Float",'die_time','die')
        self.newOutput("Boolean",'is_visible','vis')
        self.newOutput("Float",'lifetime','life')
        self.newOutput("Vector",'location','loc')
        self.newOutput("Quaternion",'rotation','rot')
        self.newOutput("Float",'size','size')
        self.newOutput("Vector",'velocity','vel')
        self.newOutput("Vector",'angular_velocity','ang')
        pass

    def execute(self,source,pid,scene):
        if source is None:
                    return "Unborn",0,0,0,False,1,Vector((0,0,0)),Quaternion((1, 0, 0, 0)),1,Vector((0,0,0)),Vector((0,0,0))
        pt=source.particles[pid]         
        alive=pt.alive_state
        birth=pt.birth_time
        die=pt.die_time
        if alive=='ALIVE':
            age=scene.frame_current_final-birth
        elif alive=='DEAD':
            age=die
        else:
            age=0
        vis=pt.is_visible
        life=pt.lifetime
        loc=pt.location
        rot=pt.rotation
        size=pt.size
        vel=pt.velocity
        ang=pt.angular_velocity
        return alive,birth,age,die,vis,life,loc,rot,size,vel,ang
