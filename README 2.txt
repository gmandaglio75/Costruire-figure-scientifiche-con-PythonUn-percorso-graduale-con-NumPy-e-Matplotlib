Contenuto del pacchetto
- chapter_istogrammi_fit.tex: capitolo LaTeX con le figure incluse
- fig_*.png: figure prodotte dai vari script
- istogrammamimano.py, istogrammami.py, istogrammami2.py, istogrammami3.py, istogrammafit.py: script originali
- daterelli.txt: dati
- genera_figure.py: script usato per rigenerare tutte le figure
- risultati_fit.txt: parametri numerici ottenuti dal fit

Uso nel documento principale
1. Caricare almeno: graphicx, amsmath, xcolor, listings, booktabs.
2. Copiare il capitolo e le immagini nella stessa cartella del documento principale.
3. Inserire: \\input{chapter_istogrammi_fit.tex}

Per rigenerare le figure
python3 genera_figure.py
