# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:04:02 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,9,["I'm watching you......"])