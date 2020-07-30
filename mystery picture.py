# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:00:02 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random
mc=Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(50):
    r=random.randrange(1,7)
    if r==1:
        mc.setBlocks(x,y,z,x,y,z+5,57)
        z=z+5
    if r==2:
        mc.setBlocks(x,y,z,x,y,z-5,41)
        z=z-5
    if r==3:
        mc.setBlocks(x,y,z,x+5,y,z,133)
        x=x+5
    if r==4:
        mc.setBlocks(x,y,z,x-5,y,z,152)
        x=x-5

   