import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits as mplot3d

ax = plt.axes(projection="3d")

# z = np.linspace(0,30,100)
# x = np.sin(z)
# y = np.cos(z)

def z_func(x,y):
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-5,5, 100)
y = np.linspace(-5,5, 100)

X, Y = np.meshgrid(x,y)
Z = z_func(X,Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.jet)

plt.show()


