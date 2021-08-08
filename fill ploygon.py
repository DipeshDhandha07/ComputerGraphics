import matplotlib.pyplot as plt
import numpy as np

x=int(input("Enter X co-ordinate : "))
y=int(input("Enter Y co-ordinate : "))


a=np.array([-3+x,3+x,3+x,-3+x,-3+x])
b=np.array([-4+y,-4+y,-12+y,-12+y,-4+y])

#to make polygon
plt.plot(a,b,'-r')

#to color polygon
plt.fill(a,b,'-c')

plt.grid()
plt.show()
