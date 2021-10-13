# zadanie_1

x = "Lorem Ipsum is simply dummy text of the printing and typesetting" \
    " industry. Lorem Ipsum has been the industry's standard dummy text ever" \
    " since the 1500s, when an unknown printer took a galley of type and scrambled" \
    " it to make a type specimen book. It has survived not only five centuries" \
    ", but also the leap into electronic typesetting, remaining essentially unchanged." \
    " It was popularised in the 1960s with the release of Letraset sheets containing" \
    " Lorem Ipsum passages, and more recently with desktop publishing software like" \
    " Aldus PageMaker including versions of Lorem Ipsum."

# zadanie_2

imie = "Kornelia"
nazwisko = "Grygo"

litera_naziwska = nazwisko[3]
litera_imienia = imie[2]
ilosc_nazwiska = 0
ilosc_imienia = 0

for literka in range(0, len(x)):
    if x[literka] == litera_naziwska:
        ilosc_nazwiska = ilosc_nazwiska + 1
    if x[literka] == litera_imienia:
        ilosc_imienia = ilosc_imienia + 1

print(
    f"W tekście jest {ilosc_nazwiska} liter {litera_naziwska} oraz {ilosc_imienia} liter {litera_imienia}")

# zadanie_4

alicja = 'ala ma kota'
print(dir(alicja))
help(alicja.upper())

# def count(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
#   S.count(sub[, start[, end]]) -> int
#
#    Return the number of non-overlapping occurrences of substring sub in
#    string S[start:end].  Optional arguments start and end are
#    interpreted as in slice notation.
#    """
#    return 0

# zadanie_5

imie = "Kornelia"
nazwisko = "Grygo"

odw_imie = imie[::-1].lower()
odw_nazwisko = nazwisko[::-1].lower()

print(
    f"{odw_imie[0].upper() + odw_imie[1:]} {odw_nazwisko[0].upper() + odw_nazwisko[1:]}")

# zadanie_6

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = lista[5:]

for x in range(0, 5):
    lista.pop()

print(lista)
print(lista_2)

# zadanie_7

lista.extend(lista_2)
lista.insert(0, 0)
lista_kopia = lista.copy()
lista_kopia.reverse()

print(lista_kopia)

# zadanie_8

student_1 = (145012, "Andrzej Piaseczny")
student_2 = (145514, "Michał Wiśniewski")
student_3 = (146016, "Dorota Rabczewska")
lista_studentow = [student_1, student_2, student_3]
print(lista_studentow)

# zadanie_9

student_11 = (145012, ["Andrzej Piaseczny", "lat 21",
              "andrzej@gmail.com", 2000, "ul. Wesoła 99 40-222 Biskupiec"])
student_12 = (145514, ["Michał Wiśniewski", "lat 23",
              "michal@gmail.com", 1998, "ul. Słoneczna 77 10-089 Olsztyn"])
student_13 = (146016, ["Dorota Rabczewska", "lat 25",
              "dorota@gmail.com", 1996, "ul. Kolorowa 66 16-400 Suwałki"])
lista_studentow = [student_11, student_12, student_13]

slownik = dict(lista_studentow)
print(slownik)

# zadanie_10

numery = [500200200, 510777444, 500200200, 505234234, 501222333, 510777444]
numery_2 = set(numery)
print(numery_2)

# zadanie_11

for element in range(1, 11):
    print(element)

# zadanie_12

for element_2 in range(100, 19, -5):
    print(element_2)

# zadanie_13

slownik_1 = {
    1: "ala",
    2: "ma",
    3: "kota"
}
slownik_2 = {
    1: "asia",
    2: "lubi",
    3: "frytki"
}
slownik_3 = {
    1: "andrzej",
    2: "pływa",
    3: "wolno"
}

lista_slownikow = [slownik_1, slownik_2, slownik_3]

pusty_string = ""
for slowniczek in lista_slownikow:
    for wartosc in slowniczek.values():
        pusty_string = pusty_string + wartosc + ", "

print(pusty_string.rstrip(", "))
