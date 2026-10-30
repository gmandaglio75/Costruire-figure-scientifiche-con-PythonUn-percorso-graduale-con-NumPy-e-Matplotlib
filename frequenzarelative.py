import numpy as np
import matplotlib.pyplot as plt

# lettura dati
x = np.loadtxt("daterelli.txt")

# =====================================================
# ISTOGRAMMA DELLE FREQUENZE ASSOLUTE
# =====================================================

plt.figure(figsize=(8,6))

plt.hist(
    x,
    bins=20,
    color="skyblue",
    edgecolor="black"
)

plt.xlabel("Valore")
plt.ylabel("Conteggi")
plt.title("Frequenze assolute")

plt.savefig("istogramma_assoluto.pdf")
plt.show()


# =====================================================
# ISTOGRAMMA DELLE FREQUENZE RELATIVE
# =====================================================

conteggi, bin_edges = np.histogram(x, bins=20)

frequenze_relative = conteggi / len(x)

larghezze = np.diff(bin_edges)
centri = (bin_edges[:-1] + bin_edges[1:]) / 2

plt.figure(figsize=(8,6))

plt.bar(
    centri,
    frequenze_relative,
    width=larghezze,
    color="lightgreen",
    edgecolor="black"
)

plt.xlabel("Valore")
plt.ylabel("Frequenza relativa")
plt.title("Frequenze relative")

plt.savefig("istogramma_relativo.pdf")
plt.show()

