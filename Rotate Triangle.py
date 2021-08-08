import matplotlib.pyplot as plt
import numpy as np
import math
x1=np.array([0,2,4,0])
y1=np.array([0,5,3,0])
x2=np.array([0,0,0,0])
y2=np.array([0,0,0,0])
r=int(input("Enter Rotational Factor : "))
plt.plot(x1,y1,'-r')
c = math.cos(r*math.pi/180)
s = math.sin(r*math.pi/180)
x2[1]=x1[1]*c-y1[1]*s
y2[1]=x1[1]*s+y1[1]*c
x2[2]=x1[2]*c-y1[2]*s
y2[2]=x1[2]*s+y1[2]*c
plt.plot(x2,y2)
plt.grid()
plt.show()

