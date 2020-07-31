# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:10:23 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(30):
    mc.setBlocks(x+i,y-i-1,z+i,x-i,y-i-1,z-i,24s)
for j in range(28):
    mc.setBlocks(x+j,y-j-2,z+j,x-j,y-j-2,z-j,0)