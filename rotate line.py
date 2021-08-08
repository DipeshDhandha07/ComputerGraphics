import matplotlib.pyplot as plt
import numpy as np
import math

x1=np.array([0,5])
y1=np.array([0,5])
x2=np.array([0,0])
y2=np.array([0,0])
r=int(input("Enter Rotational Factor : "))
plt.plot(x1,y1)
c=math.cos(r*math.pi/180)
s=math.sin(r*math.pi/180)
x2[1]=x1[1]*c-y1[1]*s
y2[1]=x1[1]*s+y1[1]*c
plt.plot(x2,y2)
print(x2)
print(y2)
plt.grid()
plt.show()
