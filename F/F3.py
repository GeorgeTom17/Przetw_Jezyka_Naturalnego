import gzip
import numpy as np

slownik = []

with gzip.open('PoliMorf-0.6.7.tab.gz', 'rt', encoding='utf8') as f:
    for i in f:
        slownik.append(i.split('\t')[0])
        slownik.append(i.split('\t')[1])

wejscie = str(input("Prosze podac slowo : "))
if wejscie in slownik:
    pos = slownik.index(wejscie)
    for i in range(pos - 20, pos + 20):
        print(slownik[i])
else:
    print("Nie znaleziono słowa")
    exit()
