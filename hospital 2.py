# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:39:28 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z,=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+20,y+20,z+20,155)
mc.setBlocks(x+1,y+1,z+1,x+19,y+19,z+19,0)