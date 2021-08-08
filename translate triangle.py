import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,4,4,0])
y=np.array([0,0,3,0])
tx=int(input("Enter x-axis Translating Factor : "))
ty=int(input("Enter y-axis Translating Factor : "))
plt.plot(x,y,'r')
plt.plot(x+tx,y+ty)
plt.grid()
plt.show()
