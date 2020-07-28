# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:20:22 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
try:
    blockID=int(input("The ID of the block you want to put is?"))
    mc.setBlock(x,y,z,blockID)
except:
    print("Only numbers!!!")
    mc.postToChat("Only numbers!!!")