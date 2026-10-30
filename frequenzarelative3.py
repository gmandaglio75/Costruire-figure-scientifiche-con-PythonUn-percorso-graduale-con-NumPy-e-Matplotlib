import numpy as np
import matplotlib.pyplot as plt

# lettura dati
x = np.loadtxt("daterelli.txt")

# crea una figura con due canvas (subplot)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# =====================================================
# FREQUENZE ASSOLUTE
# =====================================================

ax[0].hist(
    x,
    bins=20,
    color="skyblue",
    edgecolor="black"
)

ax[0].set_xlabel("Valore")
ax[0].set_ylabel("Conteggi")
ax[0].set_title("Frequenze assolute")

# =====================================================
# FREQUENZE RELATIVE
# =====================================================

ax[1].hist(
    x,
    bins=20,
    weights=np.ones_like(x) / len(x),
    color="lightgreen",
    edgecolor="black"
)

ax[1].set_xlabel("Valore")
ax[1].set_ylabel("Frequenza relativa")
ax[1].set_title("Frequenze relative")

# aggiusta automaticamente gli spazi
fig.tight_layout()

# salva tutta la figura
plt.savefig("istogrammi_confronto.pdf")
plt.savefig("istogrammi_confronto.png", dpi=300)

plt.show()
