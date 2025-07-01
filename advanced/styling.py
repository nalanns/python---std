import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# style.use('ggplot')
# style.use('fivethirtyeight')
# style.use('dark_background')
# style.use('grayscale')

x = np.arange(0,30,0.2)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title("sin(x)")
plt.suptitle("sin(x) on top")
plt.xlabel("this is x label")
plt.ylabel("this is y label")


plt.plot(x,y1, label="sin(x)")
plt.plot(x,y2, label="cos(x)")

# plt.legend(loc = "upper left")
plt.legend(loc = "lower left")
# plt.legend(loc="best")

plt.show()


