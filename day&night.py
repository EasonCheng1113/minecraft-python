# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:45:37 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
while True:
    mc.executeCommand("time add 100")
    time.sleep(0.1)