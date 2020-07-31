# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:18:37 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x,y-1,z+i,57)