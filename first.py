# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:22:35 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=5
while t<14:
    mc.postToChat("哈囉"+str(t))
    t=t+2