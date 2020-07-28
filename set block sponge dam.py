# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:38:20 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
a=0
x,y,z=mc.player.getTilePos()
while a<20:
    a=mc.getBlock(x,y,z)
    mc.setBlocks(x-10,y,z,x+10,y+10,z+1,19)
    a=a+1
    z=z+5