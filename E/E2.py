import collections
import string


def znajdz_pary(czest_slow):
    pary = collections.defaultdict(int)
    for word, freq in czest_slow.items():
        chars = word.split()
        char_zip = list(zip(chars, chars[1:]))
        for char in char_zip:
            pary[char] += freq
    return pary


def lacz_pary(najlepsza_para, czest_slow_slownik):
    ze_spacja = " ".join(najlepsza_para)
    bez_spacji = "".join(najlepsza_para)
    polaczone = {}
    for word in czest_slow_slownik:
        word_merged = word.replace(ze_spacja, bez_spacji)
        polaczone[word_merged] = czest_slow_slownik[word]
    return polaczone


def znajdz_podslowo(czest_slow):
    char_licz = collections.defaultdict(int)
    for word, freq in czest_slow.items():
        chars = word.split()
        for char in chars:
            char_licz[char] += freq

    return char_licz

tekst = str(input("Prosze podac tekst wejsciowy : "))
licz_wejsc = int(input("Prosze podac zadana liczbe wejsc w slowniku : "))

punctuation = string.punctuation + '“’'

text = tekst.lower()
text_clean = text.translate(str.maketrans('', '', punctuation))

tokeny = text_clean.split()
tokeny = [" ".join(tok) + ' </w>' for tok in tokeny]

licz_slow = collections.Counter(tokeny)
podslowa = znajdz_podslowo(licz_slow)

while len(podslowa) > licz_wejsc :
    pary = znajdz_pary(licz_slow)
    najlepsza_para = max(pary, key=pary.get)
    licz_slow = lacz_pary(najlepsza_para, licz_slow)
    podslowa = znajdz_podslowo(licz_slow)

print(podslowa)