#zadanie_1

x = "Lorem Ipsum is simply dummy text of the printing and typesetting" \
    " industry. Lorem Ipsum has been the industry's standard dummy text ever" \
    " since the 1500s, when an unknown printer took a galley of type and scrambled" \
    " it to make a type specimen book. It has survived not only five centuries" \
    ", but also the leap into electronic typesetting, remaining essentially unchanged." \
    " It was popularised in the 1960s with the release of Letraset sheets containing" \
    " Lorem Ipsum passages, and more recently with desktop publishing software like" \
    " Aldus PageMaker including versions of Lorem Ipsum."

#zadanie_2

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

#zadanie_4

alicja = 'ala ma kota'
print(dir(alicja))
help(alicja.count())

#def count(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
#   S.count(sub[, start[, end]]) -> int
#
#    Return the number of non-overlapping occurrences of substring sub in
#    string S[start:end].  Optional arguments start and end are
#    interpreted as in slice notation.
#    """
#    return 0

#zadanie_5
