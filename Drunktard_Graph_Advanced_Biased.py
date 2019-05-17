# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:14:36 2019

@author: thewo
"""

import matplotlib.pyplot as plt 
import random
import plotly.plotly
import plotly.graph_objs as go


class directions:
    Unbiased = ['NW','N','NE','E','SE','S','SW','W']
    
    Biased_NW = ['NW','NW','NW','NW','N','N','W','W','NE','SW']
    Biased_N  = ['N','N','N','N','NW','NW','NE','NE','E','W']
    Biased_NE = ['NE','NE','NE','NE','N','N','E','E','SE','NW']
    Biased_E = ['E','E','E','E','NE','NE','SE','SE','N','S']
    Biased_SE = ['SE','SE','SE','SE','S','S','E','E','NE','SW']
    Biased_S = ['S','S','S','S','SE','SE','SW','SW','W','E']
    Biased_SW = ['SW','SW','SW','SW','S','S','W','W','NW','SE',]
    Biased_W = ['W','W','W','W','NW','NW','SW','SW','N','S']

def random_walk(steps):
    x = [0 for i in range(steps)]
    y = [0 for i in range(steps)]
    a='N'
    for i in range(1,steps):
        if a == 'NW' :
            a = random.choice(directions.Biased_NW)
            calculating_steps(a,i,x,y)
        elif a == 'N' :
            a = random.choice(directions.Biased_N)
            calculating_steps(a,i,x,y)
        elif a == 'NE' :
            a = random.choice(directions.Biased_NE)
            calculating_steps(a,i,x,y)
        elif a == 'E' :
            a = random.choice(directions.Biased_E)
            calculating_steps(a,i,x,y)
        elif a == 'SE' :
            a = random.choice(directions.Biased_SE)
            calculating_steps(a,i,x,y)
        elif a == 'S' :
            a = random.choice(directions.Biased_S)
            calculating_steps(a,i,x,y)
        elif a == 'SW' :
            a = random.choice(directions.Biased_NW)
            calculating_steps(a,i,x,y)
        else:
            a = random.choice(directions.Biased_SW)
            calculating_steps(a,i,x,y)
        return x,y 

 
def calculating_steps(a,i,x,y):
        d = random.random()

        if a == 'NW' :
            x[i] = x[i-1] - d
            y[i] = y[i-1] + d
        elif a == 'N' :
            x[i] = x[i-1]
            y[i] = y[i-1] + d
        elif a == 'NE' :
            x[i] = x[i-1] + d
            y[i] = y[i-1] + d
        elif a == 'E' :
            x[i] = x[i-1] + d
            y[i] = y[i-1] 
        elif a == 'SE' :
            x[i] = x[i-1] + d
            y[i] = y[i-1] - d
        elif a == 'S' :
            x[i] = x[i-1] 
            y[i] = y[i-1] - d
        elif a == 'SW' :
            x[i] = x[i-1] - d
            y[i] = y[i-1] - d
        else:
            x[i] = x[i-1] - d
            y[i] = y[i-1]
        
        return x[i],y[i],a
    
#Executing walk
p,q = random_walk(10) 

print(p)
print(q)
#Plot using matplot
plt.plot(p,q)


#Plot using Plotly
trace = go.Scatter(
        x = p,
        y = q)   
data = [trace]    
plotly.offline.plot(data, filename='basic-line.html')