import bpy,yagmail
from bpy.props import *
from ... base_types import AnimationNode

class EMail(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_email"
    bl_label = "Email"
    
    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Text", "user","user")
        self.newInput("Text", "password","password")
        self.newInput("Text", "to","to")
        self.newInput("Text", "subject","subject")
        self.newInput("Text", "contents","contents")
        self.newOutput("Boolean", "sended", "sended",value=False)
    

    def execute(self,on,user,password,to,subject,contents):
        if on:
            try:
                yag = yagmail.SMTP(user=user,password=password)
                yag.send(to = to,subject = subject ,contents = contents )
                return True
            except:
                return False
        return False
    