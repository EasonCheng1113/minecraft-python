# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:54:59 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,+y+5,z+1,57) 
    mc.setBlocks(x,y,z,x,+y+4,z,41)
for i in range(0,50,5):
    Tree(x+i,y,z)
    Tree(x+i,y,z+5)
    Tree(x+i,y,z+10)
    Tree(x+i,y,z+15)
    Tree(x+i,y,z+20)