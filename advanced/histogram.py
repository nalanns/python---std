import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 172, 8

x = mu + sigma * np.random.randn(1000)
plt.hist(x, 100, facecolor = "blue", alpha=0.5, density=True)
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.title("Heights")
plt.text( 150, 0.04, "mu = 172, sigma = 8" )
plt.grid(True)

plt.show()


