import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,4,4,0])
y=np.array([0,0,3,0])
axis=input("Enter Axis to Reflect : ")
plt.plot(x,y)
if axis=='x':
    plt.plot(x,y*-1)
elif axis=='xy' :
    plt.plot(x*-1,y*-1)
else :
    plt.plot(x*-1,y)
plt.grid()
plt.show()
