import bpy,requests
from bpy.props import *
from ... base_types import AnimationNode


class Web_Get(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_webGet"
    bl_label = "Web Get"
    

    def create(self):

        self.newInput("Boolean", "On","on",value=False)
        
        self.newInput("Generic", "headers","headers")
        self.newInput("Generic", "params","params")
        self.newInput("Generic", "cookies","cookies")
        self.newInput("Text","encoding","encoding",value="utf8")
        self.newInput("Text",'url','url',value="")
        self.newOutput("Text", "text","text")
        self.newOutput("Generic", "headers","headers")
        self.newOutput("Text", "content","content")
        self.newOutput("Generic", "json","json")
        self.newOutput("Generic", "raw","raw")
        self.newOutput("Generic", "cookies","cookies")
        

        
    def execute(self,on,headers,params,cookies,encoding,url):
        if url=="":
            pass
        if on:
            try:
                r=requests.get(url,headers=headers,cookies=cookies,params=params)
                r.encoding = encoding
                try:
                    json=r.json()
                except:
                    json=""
                return r.text,r.headers,r.content,json,r.raw,r.cookies
            except:
                pass
        return "","","","","",""

class Post(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_webPost"
    bl_label = "Web Post"

    def create(self):

        self.newInput("Boolean", "On","on",value=False)
        
        self.newInput("Generic", "headers","headers")
        self.newInput("Generic", "data","data")
        self.newInput("Generic", "cookies","cookies")
        self.newInput("Text","encoding","encoding",value="utf8")
        self.newInput("Text",'url','url',value="")
        self.newOutput("Text", "text","text")
        self.newOutput("Generic", "headers","headers")
        self.newOutput("Text", "content","content")
        self.newOutput("Generic", "json","json")
        self.newOutput("Generic", "raw","raw")
        self.newOutput("Generic", "cookies","cookies")
        

        
    def execute(self,on,headers,data,cookies,encoding,url):
        if url=="":
            pass
        if on:
            try:
                r=requests.post(url,headers=headers,cookies=cookies,data=data)
                r.encoding = encoding
                try:
                    json=r.json()
                except:
                    json=""
                return r.text,r.headers,r.content,json,r.raw,r.cookies
            except:
                pass
        return "","","","","",""