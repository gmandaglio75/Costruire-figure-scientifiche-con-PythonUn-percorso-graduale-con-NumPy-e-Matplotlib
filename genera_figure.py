import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pathlib import Path

base = Path(__file__).resolve().parent
x = np.loadtxt(base / 'daterelli.txt')

# 1. Istogramma manuale, coerente con istogrammamimano.py
def istogrammello(data, div):
    high = max(data) + 0.01
    low = min(data) - 0.01
    delta = (high - low) / div
    hist = [0.0 for _ in range(div)]
    for a in data:
        for b in range(div):
            if a > low + b*delta and a <= low + (b+1)*delta:
                hist[b] += 1
                break
    return np.array(hist), low, high, delta

h, low, high, delta = istogrammello(x.tolist(), 10)
centri = low + (np.arange(10) + 0.5) * delta
plt.figure(figsize=(7, 5))
plt.bar(centri, h, width=0.95*delta, color='C0', edgecolor='black')
plt.xlabel('Valore')
plt.ylabel('Conteggi')
plt.tight_layout()
plt.savefig(base / 'fig_istogramma_manuale.png', dpi=200)
plt.close()

# 2. Istogramma minimo
plt.figure(figsize=(7, 5))
plt.hist(x)
plt.tight_layout()
plt.savefig(base / 'fig_istogrammami.png', dpi=200)
plt.close()

# 3. Con etichette
plt.figure(figsize=(7, 5))
plt.hist(x)
plt.xlabel('Valore')
plt.ylabel('Conteggi')
plt.tight_layout()
plt.savefig(base / 'fig_istogrammami2.png', dpi=200)
plt.close()

# 4. Personalizzato
plt.figure(figsize=(7, 5))
plt.hist(x, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Valore')
plt.ylabel('Conteggi')
plt.tight_layout()
plt.savefig(base / 'fig_istogrammami3.png', dpi=200)
plt.close()

# 5. Fit gaussiano, stesso schema dello script fornito
def gaussiana(z, A, mu, sigma):
    return A * np.exp(-(z-mu)**2/(2*sigma**2))

fig, ax = plt.subplots(figsize=(7, 5))
conteggi, edges, _ = ax.hist(x, bins=20, color='skyblue', edgecolor='black', label='Dati')
bin_centri = (edges[:-1] + edges[1:]) / 2
errori = np.sqrt(conteggi)
errori[errori == 0] = 1
p0 = [np.max(conteggi), np.mean(x), np.std(x)]
popt, pcov = curve_fit(gaussiana, bin_centri, conteggi, p0=p0, sigma=errori, absolute_sigma=True)
perr = np.sqrt(np.diag(pcov))
xfit = np.linspace(edges[0], edges[-1], 500)
ax.plot(xfit, gaussiana(xfit, *popt), 'r-', lw=2, label='Fit gaussiano')
ax.set_xlabel('Valore')
ax.set_ylabel('Conteggi')
ax.legend()
ax.text(0.97, 0.95,
        f'A = {popt[0]:.2f} +/- {perr[0]:.2f}\n'
        f'mu = {popt[1]:.3f} +/- {perr[1]:.3f}\n'
        f'sigma = {popt[2]:.3f} +/- {perr[2]:.3f}',
        transform=ax.transAxes, ha='right', va='top', fontsize=10,
        bbox=dict(facecolor='white', edgecolor='black', alpha=0.85))
fig.tight_layout()
fig.savefig(base / 'fig_istogramma_fit.png', dpi=200)
plt.close(fig)

print('popt=', popt)
print('perr=', perr)
