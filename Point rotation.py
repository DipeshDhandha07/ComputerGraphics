import matplotlib.pyplot as plt
import numpy as np
import math
x=int(input("Enter the x-coordinate of point : "))
y=int(input("Enter the y-coordinate of point : "))
plt.plot(x,y,'.')
h=int(input("Enter the x-coordinate of point around which rotation is done : "))
k=int(input("Enter the y-coordinate of point around which rotation is done : "))
plt.plot(h,k,'.')
t=int(input("Enter angle of rotation : "))
x1=(h*math.cos(t))-(k*math.sin(t));
y1=(h*math.sin(t))+(k*math.cos(t));
x3=x1+x-h;
y3=y1+y-k;
plt.plot(x3,y3,'.')
plt.grid()
plt.show()
