# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:57:34 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
while True:
    x,y,z,=mc.player.getTilePos()
    mc.setBlocks(x-3,y,z-3,x+1,y,z+1,8)
    time.sleep(0)