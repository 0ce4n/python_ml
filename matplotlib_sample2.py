import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#3D图形
def z(x,y):
    return x + y 

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)

x,y = np.meshgrid(X,Y)

z = z(x,y)
ax.plot_surface(x,y,z,rstride = 1, cstride = 1,cmap = plt.get_cmap('rainbow'))
ax.contourf(x,y,z,zdir = 'z',offset = -2,cmap = 'rainbow')
ax.set_zlim(-2,2)


plt.show()


