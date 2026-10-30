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

#questa volta fatto direttamente con matplotlib e con la normalizzazione pesata 

plt.figure(figsize=(8,6))


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

plt.savefig("istogramma_relativo.pdf")
plt.show()

