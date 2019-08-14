import bpy
import os,copy
from bpy.props import *
from ... base_types import AnimationNode

class Memeory(bpy.types.Node, AnimationNode):
    
    bl_idname = "an_fx_Memory"
    bl_label = "Memory"
    li=[]
    Time=[]
    Count=[]
    errorMessage = StringProperty()

    def create(self):
        self.newInput("Boolean", "Clear","clear",value=False)
        self.newInput("Boolean", "On","on",value=False)
        self.newInput("Boolean", "Add","Append",value=False,hide=True)
        self.newInput("Boolean", "Subtract","Pop",value=False,hide=True)
        self.newInput("Integer", "Index","n",hide=False)
        self.newInput("Generic", "Data","data")
        self.newInput("Integer", "Start","start",value=1)
        self.newInput("Integer", "End","end",value=250)
        self.newInput("Integer", "Time","time")
        self.newInput("Scene", "Scene", "scene",hide = True)
        self.newOutput("Generic List",'List','out')
    
    def getaddr(self,List,n):
        addr=[id(i) for i in List]
        return addr.index(n)

    def execute(self,clear,on,Append,Pop,n,data,start,end,time,scene):
        
        #自动时间
        if self.inputs["Time"].hide==True:
            time=scene.frame_current

        #打开文件时建立存储区
        li=self.li
        try:
            m=self.getaddr(li,n)
        except:
            li=self.li
            li.append([])
            self.Time.append(0)
            self.Count.append(1)
            index=len(li)-1
            n=id(li[index])
            m=self.getaddr(li,n)
            self.inputs["Index"].value=n
            print(n)
        
        #清理存储
        if clear:
            li[m].clear()
            self.Time[m]=start-1
            scene.frame_current=start
        else:
            #如果数据为空
            if data is None:
                return li[m]

            #如果开启
            if on:
                #如果追加
                if Append:
                        li[m].append(copy.deepcopy(data))
                
                #如果移除
                elif Pop and len(li[m])>=2:
                    li[m].pop()
                
                else:
                    old=self.Time[m]
                    if time<start:
                        li[m].clear()
                        self.Time[m]=start
                    if time>end:
                        pass
                    else:
                        if old+1==time:
                            li[m].append(copy.deepcopy(data))
                            self.Time[m]=time
                        elif old-1==time:
                            if len(li[m])>=1:
                                li[m].pop(-1)
                                self.Time[m]=time
                        else:
                            pass
                self.errorMessage="Successed"
        out=li[m]
        return out
    
    def duplicate(self, sourceNode):
        key=self.inputs.get("Index").values()[0]
        m=self.getaddr(self.li,key)
        self.Count[m]+=1

    def delete(self):
        key=self.inputs.get("Index").values()[0]
        m=self.getaddr(self.li,key)

        if self.Count[m]==1:
            self.Time.pop(m)
            self.li.pop(m)
            self.Count.pop(m)
        else:
            self.Count[m]-=1
        print("List Count: ",len(self.li))
        print("Used Count: ",self.Count)
# import bpy
# import os
# from bpy.props import *
# from ... base_types import AnimationNode
# import copy

# class Memeory(bpy.types.Node, AnimationNode):
    
#     bl_idname = "an_fx_Memory"
#     bl_label = "Memory"
#     li=[]
#     Time=[]
#     Count=[]
#     errorMessage = StringProperty()


#     def create(self):
#         li=self.li
#         li.append([])
#         self.Time.append(0)
#         self.Count.append(1)
#         index=len(li)-1
#         addr=id(li[index])
#         self.newInput("Boolean", "Clear","clear",value=False)
#         self.newInput("Boolean", "On","on",value=False)
#         self.newInput("Boolean", "Add","Append",value=False,hide=True)
#         self.newInput("Boolean", "Subtract","Pop",value=False,hide=True)
#         a=self.newInput("Integer", "Index","n",value=addr,hide=False)
#         self.newInput("Generic", "Data","data")
#         self.newInput("Integer", "Start","start",value=1)
#         self.newInput("Integer", "End","end",value=250)
#         self.newInput("Integer", "Time","time")
#         self.newInput("Scene", "Scene", "scene",hide = True)
#         self.newOutput("Generic List",'List','out')
    
#     def getaddr(self,List,n):
#         addr=[id(i) for i in List]
#         return addr.index(n)

#     def execute(self,clear,on,Append,Pop,n,data,start,end,time,scene):
#         li=self.li
#         try:
#             m=self.getaddr(li,n)
#         except:
#             li=self.li
#             index=len(li)-1
#             n=id(li[index])
#             m=self.getaddr(li,n)
#             self.inputs["Index"].value=n
#             print(n)

#         if clear:
#             li[m].clear()
#             self.Time[m]=start-1
#             scene.frame_current=start
#         else:
#             if data is None:
#                 self.errorMessage=""
#                 return

#             if on:
#                 if Append:
#                         li[m].append(copy.deepcopy(data))

#                 elif Pop and len(li[m])>=2:
#                     li[m].pop()

#                 else:
#                     old=self.Time[m]
#                     if time<start:
#                         li[m].clear()
#                         self.Time[m]=start
#                     if time>end:
#                         pass
#                     else:
#                         if old+1==time:
#                             li[m].append(copy.deepcopy(data))
#                             self.Time[m]=time
#                         elif old-1==time:
#                             if len(li[m])>=1:
#                                 li[m].pop(-1)
#                                 self.Time[m]=time
#                         else:
#                             pass
#                 self.errorMessage="Successed"
#         out=li[m]
#         return out
    
#     def duplicate(self, sourceNode):
#         key=self.inputs.get("Index").values()[0]
#         m=self.getaddr(self.li,key)
#         self.Count[m]+=1

#     def delete(self):
#         key=self.inputs.get("Index").values()[0]
#         m=self.getaddr(self.li,key)

#         if self.Count[m]==1:
#             self.Time.pop(m)
#             self.li.pop(m)
#             self.Count.pop(m)
#         else:
#             self.Count[m]-=1
#         print("List Count: ",len(self.li))
#         print("Used Count: ",self.Count)