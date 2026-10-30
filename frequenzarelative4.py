import numpy as np
import matplotlib.pyplot as plt

# lettura dati
x = np.loadtxt("daterelli.txt")

# ==========================================
# finestra 1 : frequenze assolute
# ==========================================

plt.figure("Frequenze assolute", figsize=(8,6))

plt.hist(
    x,
    bins=20,
    color="skyblue",
    edgecolor="black"
)

plt.xlabel("Valore")
plt.ylabel("Conteggi")
plt.title("Frequenze assolute")

# ==========================================
# finestra 2 : frequenze relative
# ==========================================

plt.figure("Frequenze relative", figsize=(8,6))

plt.hist(
    x,
    bins=20,
    weights=np.ones_like(x)/len(x),
    color="lightgreen",
    edgecolor="black"
)

plt.xlabel("Valore")
plt.ylabel("Frequenza relativa")
plt.title("Frequenze relative")

# visualizza entrambe
plt.show()

