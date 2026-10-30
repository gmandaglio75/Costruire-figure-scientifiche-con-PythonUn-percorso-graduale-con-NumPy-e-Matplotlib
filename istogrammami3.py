import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt("daterelli.txt")

plt.hist(x, 
         bins=20,
         color="skyblue",
         edgecolor="black"
         )
plt.xlabel("Valore")
plt.ylabel("Conteggi")
plt.show()

plt.savefig("grafico.pdf")
