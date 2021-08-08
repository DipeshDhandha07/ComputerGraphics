import matplotlib.pyplot as plt
import numpy as np
import math
x1=np.array([0,0,5,5,0])
y1=np.array([0,5,5,0,0])
x2=np.array([0,0,0,0,0])
y2=np.array([0,0,0,0,0])
r=int(input("Enter Rotational Factor : "))
plt.plot(x1,y1,'-r')
c = math.cos(r*math.pi/180)
s = math.sin(r*math.pi/180)
for i in range(len(x1)-1):
    #print(i)
    x2[i]=x1[i]*c-y1[i]*s
    y2[i]=x1[i]*s+y1[i]*c
plt.plot(x2,y2)
plt.grid()
plt.show()



