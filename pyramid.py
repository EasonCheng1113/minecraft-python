# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:41:49 2020

@author: appedu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:43:31 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(10):
    mc.setBlocks(x-i,y-i,z-i,x+i,y-i,z+i,57)
    time.sleep(0.5)