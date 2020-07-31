# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:56:25 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i,y-1,z,155)