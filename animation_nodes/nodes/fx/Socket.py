import bpy
from bpy.props import *
from ... base_types import AnimationNode

import socket as st
import math as m  


class Server(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Server"
    bl_label = "Server"
    
    st.setdefaulttimeout(0)
    s=st.socket(st.AF_INET,st.SOCK_STREAM)

    binded: BoolProperty(default = False)
    sended: BoolProperty(default = False)

    def create(self):
        
        self.s.setsockopt(st.SOL_SOCKET,st.SO_REUSEADDR,1)

        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Text", "host","host",value='localhost')
        self.newInput("Integer", "port","port",value=5000)
        # self.newInput("Float", "time out","timeout",value=0.01)
        self.newInput("Text",'Message','msg',value="hello world")
        self.newOutput("Boolean", "Connected","connected",value=False)
        self.newOutput("Boolean", "Sended","sended",value=False)
        

        
    def execute(self,on,host,port,msg):
        s=self.s
        if on:
            try:
                try:
                    clientsock,clientaddr=s.accept()
                    clientsock.send(msg.encode())
                    clientsock.settimeout(timeout)
                    clientsock.close()
                    self.sended=True
                except:
                    s.setsockopt(st.SOL_SOCKET,st.SO_REUSEADDR,1)
                    s.bind((host,port))
                    s.listen(0)
                    self.binded=True
            except:
                pass

        return self.binded,self.sended
    
    def delete(self,source):
        try:
            self.s.close()
        except:
            pass
        self.binded=False
        self.sended=False


class Client(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Client"
    bl_label = "Client"

    def create(self):
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Text", "host","host",value='localhost')
        self.newInput("Integer", "port","port",value=5000)
        self.newInput("Integer",'bufsize','bufsize',value=1024)
        self.newInput("Float", "time out","timeout",value=0.05)
        self.newOutput("Text", "Message","out",value=False)
        self.s.setsockopt(st.SOL_SOCKET,st.SO_REUSEADDR,1)
        

        
    def execute(self,on,host,port,bufsize,timeout):
        if on:
            try:
                st.setdefaulttimeout(timeout)
                c=st.socket(st.AF_INET,st.SOCK_STREAM)
                server=(host,port)
                c.connect(server)
                out=c.recv(bufsize).decode()
                c.close()
                return out
            except:
                pass