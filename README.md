# Animation nodes with Fx nodes For Blender 2.8

## 介绍（Introduction）

这是Animation nodes节点的疯狂版本，它基于 JacquesLucke开发的Animation nodes插件。

众所周知，Blender和Python整合得很好。而Animation nodes是一个优秀的可视化编程环境，这意味着你可以在Animation nodes里做任何Python能做的事。

想想看，你可以用blender浏览网页、发邮件、在blender程序间互通数据、做网络爬虫，控制Arduino机器人。。。

所以为什么不去做呢？

于是我尝试增加了一些好玩和疯狂的节点扩展。



This is a crazy version of the Animation nodes, which is based on the Animation nodes plugin developed by JacquesLucke.

As we all know, Blender and Python are well integrated. Animation nodes are an excellent visual programming environment, which means you can do whatever Python can do in Animation nodes.

Think about it, you can use Blender to browse the web, send emails, exchange data between Blender programs, do web crawlers, and control Arduino robots. . .

So why not do it?

So I tried to add some fun and crazy node extensions.

------

## 新增节点列表(The list of new nodes)

- Set Object Transforms	设置物体变换
- Get Face Data	获取面数据
- Get Object Normals	获取物体法线
- Set Vertex Weight	设置顶点权重
- Get Particles Data	获取粒子数据
- Set Particles Data	设置粒子数据
- Get Pixel Count	获取图片像素总数
- Get Pixel	获取像素颜色
- Select Object	选择物体
- Get/Set Clipboard	获取/设置剪切板
- File Reader	文件读取
- File Writer	文件写出
- Json Reader	Json读取
- Dictionary	字典解析
- Time	时间
- Email	邮件
- Serial	串口通信
- Server	服务器
- Client	客户端
- Web Get	网页Get
- Web Post	网页Post
- Activate	激活器
- Memory	缓存

------

## 如何安装？（How to install？）

这里有两种类型的版本,分别是普通版和极客版。它们的不同之处在于，极客版本会多一些节点，并且依赖第三方python库，若你决定要使用极客版你得先解决依赖问题，意味着得先安装相应的python库。

普通版安装方法：
你只需要下载 animation_nodes_fx.zip，然后常规方法安装。

极客版安装方法:
你需要下载两个文件：animation_nodes_fx_geek.zip 和 site-packages.zip。
然后把site-packages.zip解压出来，合并到blender程序自带的site-packages文件夹（通常路径是“blender-2.80-windows64\2.80\python\lib\site-packages“），接着按常规方法安装animation_nodes_fx_geek.zip。
（注意：你必须得这么做，不然它不会起作用。）



There are two types of versions, the regular and geek versions. The difference is that the geek version will have more nodes and rely on third-party python libraries. If you decide to use the geek version, you have to solve the dependency problem first, which means you have to install the corresponding python library first.

Regular version installation method:
You only need to download animation_nodes_fx.zip and install it in the usual way.

Geek version installation method:
You need to download two files: animation_nodes_fx_geek.zip and site-packages.zip.
Then extract the site-packages.zip and merge it into the site-packages folder that comes with the Blender program (usually the path is "blender-2.80-windows64\2.80\python\lib\site-packages"), then install it as usual. Animation_nodes_fx_geek.zip.
(Note: You have to do this or it won't work.)

------

## 其他（Last but not least）

我是一个视效艺术家，fx nodes节点的风格借鉴了3dsmax的thinking particles。因此每个节点都有On接口控制节点的启用和关闭。

目前这个只有win版本，没有linux和mac版本。

遇到bug请给我反馈，有好的idea也请联系我。

希望社区的代码高手们能帮助我改进代码，并提交给我更多疯狂的节点！！！



I am a visual effects artist, and the style of the fx nodes is based on 3dsmax's thinking particles. Therefore each node has an On interface control node enabled and disabled.

Currently this is only the win version, there is no linux and mac version.

Please give me feedback when you encounter a bug. Please contact me if you have a good idea.

I hope the code experts in the community can help me improve the code and submit me more crazy nodes! ! !

Enjoy it!
