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
    mc.setBlock(x,y-1,z,11)
    time.sleep(0)