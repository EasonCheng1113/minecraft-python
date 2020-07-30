# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:49:07 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(100):
    r=random.randrange(1,7)
    if r==1:
        mc.setBlocks(x,y,z,x,y,z+5,57)
        z=z+5
    elif r==2:
        mc.setBlocks(x,y,z,x,y,z-5,41)
        z=z-5
    elif r==3:
        mc.setBlocks(x,y,z,x+5,y,z,133)
        x=x+5
    elif r==4:
        mc.setBlocks(x,y,z,x-5,y,z,152)
        x=x-5
    elif r==5:
        mc.setBlocks(x,y,z,x,y+5,z,42)
        y=y+5
    else:
        mc.setBlocks(x,y,z,x,y-5,z,49)
        y=y-5