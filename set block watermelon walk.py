# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:31:41 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x,y,z)
    if a==0:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,103)