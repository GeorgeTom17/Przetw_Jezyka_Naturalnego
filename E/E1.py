import gzip

slownik = []

with gzip.open('PoliMorf-0.6.7.tab.gz', 'rt', encoding='utf8') as f:
    for i in f:
        slownik.append(i.split('\t')[0])
        slownik.append(i.split('\t')[1])

user_in = str(input("Prosze podac ciag znakow : "))
tokens = []
i = 0
while i < len(user_in):
    maxWord = ""
    for j in range(i, len(user_in)):
        tempWord = user_in[i:j+1]
        if tempWord in slownik and len(tempWord) > len(maxWord):
            maxWord = tempWord
    tokens.append(maxWord)
    i += len(maxWord)
print(tokens)