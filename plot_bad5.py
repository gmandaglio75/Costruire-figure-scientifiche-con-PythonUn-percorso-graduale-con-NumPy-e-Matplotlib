import numpy as np
import matplotlib.pyplot as plt

dati = np.loadtxt("Kter.txt")
x = dati[:, 0]
y1 = dati[:, 1]
y2 = dati[:, 2]
plt.plot(x, y1, "^", label="Misure 1")
plt.plot(x, y2, "o", label="Misure 2")
plt.xlabel("Distanza (cm)")
plt.ylabel("Frequenza (Hz)")
plt.legend()
plt.show()
