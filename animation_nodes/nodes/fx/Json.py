import bpy
import os
from bpy.props import *
from ... base_types import AnimationNode
import json

class JsonReader(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_JsonReader"
    bl_label = "Json Reader"

    errorMessage = StringProperty()
    
    def create(self):
        self.newInput("Boolean", "On","on",hide=True)
        self.newInput("Boolean", "Dictionary","Dict")
        self.newInput("Generic",'Message','msg')
        self.newInput("Integer",'Index','ids')
        self.newInput("Text",'Key','key')
        self.newOutput("Generic",'Message','msg')

        
    def execute(self,on,Dict,msg,ids,key):
        if msg is None or msg == "":
                return
        try:
            msg=json.loads(msg)
        except:
            pass
        if on:
            if Dict:
                return msg
            else:
                if key !="":
                    try:
                        return msg[ids][key]
                    except:
                        return
                else:
                    return msg[ids]
            
        out=msg
        return out


class Dictionary(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Dictionary"
    bl_label = "Dictionary"

    errorMessage = StringProperty()
    
    def create(self):
        self.newInput("Boolean", "On","on",hide=True)
        self.newInput("Generic",'Dict','Dict')
        self.newInput("Integer",'Index','ids')
        self.newInput("Text",'Key','key')
        self.newOutput("Generic",'Element','out')

        
    def execute(self,on,Dict,ids,key):
        if on:
            if Dict is None:
                return
            
            if key is not None:
                try:
                    if self.inputs.get("Index").hide:
                        out=Dict[key]
                    out=Dict[ids][key]
                except:
                    return
            return out
