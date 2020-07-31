# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:41:02 2020

@author: appedu
"""

import random,time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z,=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+20,y+20,z+20,57)
mc.setBlocks(x+1,y+1,z+1,x+19,y+19,z+19,0)