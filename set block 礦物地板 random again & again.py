# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:57:34 2020

@author: appedu
"""

import random,time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z,=mc.player.getTilePos()
while True:
    color=random.randrange(0,16)
    mc.setBlocks(x-25,y-1,z-25,x+25,y-1,z+25,95,color)
    time.sleep(1)