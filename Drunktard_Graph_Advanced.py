# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:25:37 2019

@author: thewo
"""
import matplotlib.pyplot as plt 
import random
import plotly.plotly
import plotly.graph_objs as go


class directions:
    Unbiased = ['NW','N','NE','E','SE','S','SW','W']
    
    
def random_walk(steps):
    x = [0 for i in range(steps)]
    y = [0 for i in range(steps)]
    
    for i in range(1,steps):
        a = random.choice(directions.Unbiased)
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
        
    return x,y 
 

#Executing walk
a,b = random_walk(10) 

print(a)
print(b)
#Plot using matplot
plt.plot(a,b)


#Plot using Plotly
trace = go.Scatter(
        x = a,
        y = b)   
data = [trace]    
plotly.offline.plot(data, filename='basic-line.html')
