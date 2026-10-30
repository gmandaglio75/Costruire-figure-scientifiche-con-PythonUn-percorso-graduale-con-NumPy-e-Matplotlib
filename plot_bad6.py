import numpy as np
import matplotlib.pyplot as plt

x, y1, y2 = np.loadtxt("Kter.txt", unpack=True)
plt.plot(x, y1, "^", label="Misure 1")
plt.plot(x, y2, "o", label="Misure 2")
plt.xlabel("Distanza (cm)")
plt.ylabel("Frequenza (Hz)")
plt.legend()
plt.savefig("grafico.pdf")
plt.savefig("grafico.png", dpi=300)
plt.show()
