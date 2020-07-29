# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:42:07 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i,y-1,z+i,57)
    mc.setBlock(x+i,y-1,z+i+1,57)
    mc.setBlock(x+i,y-1,z+i+2,57)