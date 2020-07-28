# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:33:34 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
messages=[]
a=1
while a<5:
    message = input("message?")
    messages.append(message)
    a=a+1
mc.setSign(x,y,z,63,9,messages)