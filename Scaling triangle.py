import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,4,4,0])
y=np.array([0,0,3,0])
sx=int(input("Enter x-axis Scaling Factor : "))
sy=int(input("Enter y-axis Scaling Factor : "))
plt.plot(x,y)
plt.plot(x*sx,y*sy)
plt.grid()
plt.show()
