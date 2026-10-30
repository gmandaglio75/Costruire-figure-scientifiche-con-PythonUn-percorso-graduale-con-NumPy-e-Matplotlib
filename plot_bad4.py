import numpy as np
import matplotlib.pyplot as plt

dati = np.loadtxt("datios.txt")
x = dati[:, 0]
y = dati[:, 1]
plt.plot(x, y, "^", label="Misure")
plt.xlabel("Tempo (s)")
plt.ylabel("Distanza (cm)")
plt.legend()
plt.show()
