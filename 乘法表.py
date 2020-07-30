# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:25:18 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
list1=[]
list2=[]
list3=[]
for i in range(1,4):
    list1.append(i*1)
for i in range(1,4):
    list2.append(i*2)
for i in range(1,4):
    list3.append(i*3)
x,y,z=mc.player.getTilePos()  
mc.setSign(x,y,z,63,9,str(list1),str(list2),str(list3))