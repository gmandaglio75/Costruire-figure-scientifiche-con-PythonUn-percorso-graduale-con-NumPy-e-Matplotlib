\subsection{Binning automatico}

Negli esempi precedenti il numero di bin è stato specificato
manualmente mediante:

\begin{lstlisting}[language=Python]
plt.hist(x, bins=20)
\end{lstlisting}

Questa scelta è perfettamente lecita, ma introduce una componente
arbitraria: un numero troppo piccolo di bin può nascondere dettagli
interessanti della distribuzione, mentre un numero troppo elevato può
amplificare le fluttuazioni statistiche.

Per questo motivo NumPy e Matplotlib mettono a disposizione diversi
algoritmi che determinano automaticamente il binning a partire dalle
caratteristiche del campione.

\subsubsection{La scelta automatica}

La soluzione più semplice consiste nello scrivere:

\begin{lstlisting}[language=Python]
plt.hist(
    x,
    bins="auto",
    color="skyblue",
    edgecolor="black"
)
\end{lstlisting}

In questo caso NumPy sceglie automaticamente una strategia per il
calcolo del numero e della larghezza dei bin.

Questa opzione è particolarmente utile durante l'analisi preliminare dei
dati, quando non si conosce ancora la struttura della distribuzione e si
desidera una rappresentazione ragionevole senza dover fissare
manualmente il numero di intervalli.

\subsubsection{Algoritmi disponibili}

Oltre a \texttt{"auto"}, sono disponibili diversi criteri automatici:

\begin{lstlisting}[language=Python]
plt.hist(x, bins="sturges")
plt.hist(x, bins="sqrt")
plt.hist(x, bins="rice")
plt.hist(x, bins="scott")
plt.hist(x, bins="fd")
plt.hist(x, bins="doane")
\end{lstlisting}

I principali metodi sono:

\begin{center}
\begin{tabular}{ll}
\toprule
Metodo & Caratteristiche \\
\midrule
\texttt{sturges} &
Adatto a campioni piccoli e distribuzioni semplici \\
\texttt{sqrt} &
Usa circa $\sqrt{N}$ bin \\
\texttt{rice} &
Usa circa $2N^{1/3}$ bin \\
\texttt{scott} &
Ottimizzato per distribuzioni quasi gaussiane \\
\texttt{fd} &
Metodo di Freedman--Diaconis, robusto agli outlier \\
\texttt{doane} &
Estensione di Sturges per distribuzioni asimmetriche \\
\texttt{auto} &
Selezione automatica tra diversi criteri \\
\bottomrule
\end{tabular}
\end{center}

\subsubsection{Il metodo di Freedman--Diaconis}

Uno dei criteri più utilizzati nelle analisi scientifiche è il metodo
di Freedman--Diaconis:

\begin{lstlisting}[language=Python]
plt.hist(
    x,
    bins="fd"
)
\end{lstlisting}

La larghezza dei bin viene scelta secondo

\[
\Delta x
=
2\,
\frac{\mathrm{IQR}}{N^{1/3}},
\]

dove:

\begin{itemize}
    \item $\mathrm{IQR}$ è l'intervallo interquartile
          (\emph{Inter Quartile Range});
    \item $N$ è il numero di osservazioni.
\end{itemize}

Poiché utilizza i quartili invece della deviazione standard, questo
criterio è poco sensibile alla presenza di outlier e produce spesso una
rappresentazione molto equilibrata.

\subsubsection{Il metodo di Scott}

Per distribuzioni compatibili con una gaussiana è molto diffuso anche il
criterio di Scott:

\begin{lstlisting}[language=Python]
plt.hist(
    x,
    bins="scott"
)
\end{lstlisting}

La larghezza del bin è

\[
\Delta x
=
3.5\,
\frac{\sigma}{N^{1/3}},
\]

dove $\sigma$ è la deviazione standard campionaria.

Per distribuzioni gaussiane questo metodo minimizza approssimativamente
l'errore quadratico medio nella stima della densità.

\subsubsection{Confronto tra binning fisso e automatico}

Supponiamo di avere un campione contenente alcune migliaia di eventi,
come il file \texttt{daterelli.txt}. Una scelta fissa è

\begin{lstlisting}[language=Python]
plt.hist(x, bins=20)
\end{lstlisting}

mentre una scelta adattativa è

\begin{lstlisting}[language=Python]
plt.hist(x, bins="auto")
\end{lstlisting}

Nel primo caso il numero di bin è deciso dall'utente; nel secondo caso è
determinato dal campione stesso.

L'approccio automatico è particolarmente utile per:

\begin{itemize}
    \item l'esplorazione preliminare dei dati;
    \item il confronto tra campioni con numerosità differenti;
    \item la ricerca di strutture inattese nella distribuzione.
\end{itemize}

\subsubsection{Binning automatico e fit}

Quando si esegue un fit dell'istogramma, il numero di bin influenza
direttamente:

\begin{itemize}
    \item i conteggi $N_i$;
    \item i centri dei bin;
    \item gli errori statistici;
    \item il valore del $\chi^2$.
\end{itemize}

Per questo motivo il risultato numerico del fit può cambiare leggermente
al variare del binning.

Una procedura ragionevole è:

\begin{enumerate}
    \item utilizzare inizialmente \texttt{bins="auto"} oppure
          \texttt{bins="fd"} per esplorare i dati;
    \item verificare la stabilità della forma della distribuzione;
    \item fissare successivamente un numero di bin costante quando si
          desidera confrontare quantitativamente più fit o più campioni.
\end{enumerate}

In pratica,

\begin{lstlisting}[language=Python]
# fase esplorativa
plt.hist(x, bins="auto")

# fase finale
plt.hist(x, bins=20)
\end{lstlisting}

rappresenta spesso una strategia efficace nelle applicazioni di
laboratorio e nell'analisi dati scientifica.

