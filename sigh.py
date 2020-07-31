# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:30:49 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,4,["出口"])