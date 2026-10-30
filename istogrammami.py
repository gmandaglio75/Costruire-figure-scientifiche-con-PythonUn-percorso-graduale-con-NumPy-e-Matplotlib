import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt("daterelli.dat")

plt.hist(x)

plt.show()
