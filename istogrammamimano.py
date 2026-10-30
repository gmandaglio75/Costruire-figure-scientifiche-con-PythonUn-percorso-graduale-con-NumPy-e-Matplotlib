def istogrammello(data,div):
    high = max(data)+0.01
    low  = min(data)-0.01
    delta = (high - low)/div
    hist =[]
    for a in range(div):
        hist.append(0.)

    for a in data:
        for b in range(div):
            if a>low+b*delta and a <= low + (b+1)*delta:
                hist[b] = hist[b] +1
    return hist

dati =list(map(float,open("daterelli.dat").read().strip().split()))
histo = istogrammello(dati, 10)
for a in histo:
    print(a)
