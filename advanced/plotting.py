import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100,101,1)
y = 0.5 * x ** 2 + 2 * x
# y2 = np.sin(x) * 2000
# y3 = np.log(x)

# plt.plot(x,y, "r--")
# plt.plot(x,y, "go")
plt.plot(x,y, "y^")
# plt.plot(x,y2)
# plt.plot(x,y3)
plt.show()

