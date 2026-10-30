import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# funzione gaussiana
def gaussiana(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))


# lettura dati
x = np.loadtxt("daterelli.txt")

# istogramma
conteggi, bin_edges, _ = plt.hist(
    x,
    bins=20,
    color="skyblue",
    edgecolor="black",
    label="Dati"
)

# centri dei bin
bin_centri = (bin_edges[:-1] + bin_edges[1:]) / 2

# errori poissoniani
errori = np.sqrt(conteggi)
errori[errori == 0] = 1

# parametri iniziali
A0 = np.max(conteggi)
mu0 = np.mean(x)
sigma0 = np.std(x)

# fit gaussiano
popt, pcov = curve_fit(
    gaussiana,
    bin_centri,
    conteggi,
    p0=[A0, mu0, sigma0],
    sigma=errori,
    absolute_sigma=True
)

# errori sui parametri
perr = np.sqrt(np.diag(pcov))

# curva liscia
xfit = np.linspace(
    bin_edges[0],
    bin_edges[-1],
    500
)

yfit = gaussiana(xfit, *popt)

# disegno del fit
plt.plot(
    xfit,
    yfit,
    "r-",
    lw=2,
    label="Fit gaussiano"
)

plt.xlabel("Valore")
plt.ylabel("Conteggi")

plt.legend()

# stampa risultati
print("\nFit gaussiano")
print(f"A     = {popt[0]:.5g} ± {perr[0]:.2g}")
print(f"mu    = {popt[1]:.5g} ± {perr[1]:.2g}")
print(f"sigma = {popt[2]:.5g} ± {perr[2]:.2g}")

plt.savefig("grafico.pdf")
plt.savefig("grafico.png", dpi=300)

plt.show()
