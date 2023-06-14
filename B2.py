import csv
import re


poprawny = True
with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    temp = []
    for row in reader:
        for i in row:
            temp.append(i)

for i in temp:
    rowcheck = re.fullmatch('^[a-z]+;[0-9]+;[0-9]+$', i)
    if rowcheck == None:
        print("plik nie jest w poprawnym formacie")
        exit()

print("plik jest w poprawnym formacie")