import re
cont = True
while cont:
    imie = str(input("Proszę podać imię :\n"))
    if imie[0].islower():
        print("imie powinno zaczynac sie z duzej litery")
        continue

    nazwisko = str(input("Proszę podać nazwisko :\n"))
    if nazwisko[0].islower():
        print("nazwisko powinno zaczynac sie z duzej litery")
        continue
    tel = str(input("Proszę podać telefon :\n"))
    telcheck = re.fullmatch('^\(\d{2}\)\d{3}-\d{2}-\d{2}', tel)
    if telcheck == None:
        print("numer nalezy podac w formacie (12)345-67-89")
        continue
    kod = str(input("Proszę podać kod pocztowy :\n"))
    kodcheck = re.fullmatch('^\d{2}-\d{3}', kod)
    if kodcheck == None:
        print("Kod pocztowy nalezy podac w formacie 12-345")
        continue
    miasto = str(input("Proszę podać miasto :\n"))
    if miasto[0].islower():
        print("nazwa miasta powinna zaczynac sie z duzej litery")
        continue
    cont = False
