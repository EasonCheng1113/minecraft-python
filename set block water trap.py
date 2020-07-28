# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:57:34 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x,y,z)
    print (a)
    if a==(8 and 9):
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)