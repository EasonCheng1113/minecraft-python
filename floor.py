# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:39:36 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z,=mc.player.getTilePos()
mc.setBlocks(x,y-1,z,x+5,y-1,z+5,7)