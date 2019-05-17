# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:42:43 2019

@author: thewo
"""
import random

def random_walk(steps):
    x = 0
    y = 0
    directions = ['N','E','S','W']
    for i in range(1,steps):
        a = random.choice(directions)
        if a == 'N' :
            y += 1
        elif a == 'E' :
            x += 1
        elif a == 'S' :
            y -= 1 
        else:
            x -= 1
    print("Position after",steps,"steps:",(x,y))
    
    
    
t = int(input("Simulation cycles:"))
random_walk_steps = int(input("Number of steps:"))
for i in range(1,t):
    random_walk(random_walk_steps)