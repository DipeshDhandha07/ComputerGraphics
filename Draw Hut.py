import matplotlib.pyplot as plt
import numpy as np

x=int(input("Enter X co-ordinate : "))
y=int(input("Enter Y co-ordinate : "))

#for triangle as roof
a=np.array([x,-3+x,3+x,x])
b=np.array([y,-4+y,-4+y,y])
plt.plot(a,b,'-r')

#for rectangle as hut
c=np.array([-3+x,3+x,3+x,-3+x,-3+x])
d=np.array([-4+y,-4+y,-12+y,-12+y,-4+y])
plt.plot(c,d,'-r')

#for rectangle as door
e=np.array([-1+x,-1+x,1+x,1+x,-1+x])
f=np.array([-12+y,-7+y,-7+y,-12+y,-12+y])
plt.plot(e,f,'-r')
plt.grid()
plt.show()
