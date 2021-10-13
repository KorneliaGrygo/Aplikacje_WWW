# zadanie1

def stworz_liste(a_list, b_list):
    nowa = list()
    dlugosc_list = len(a_list) if len(a_list) > len(b_list) else len(b_list)
    for i in range(0,dlugosc_list):
        if i % 2 == 0:
            nowa.append(a_list[i])
        else:
            nowa.append(b_list[i])
    return nowa

lista_a = [0,13,2]
lista_b = [4,5,6,7]
print(stworz_liste(lista_a,lista_b))
# zadanie2
def info_text(data_text):
    length = len(data_text)
    letters = set()
    for i in data_text:
        if i == " ":
            continue
        else:
            letters.add(i)

    big_letters = data_text.upper()
    small_letters = data_text.lower()
    return {
        "length":length,
        "letters":letters,
        "big_letters":big_letters,
        "small_letters":small_letters
    }
print(info_text("Kasia ma trzy nogi"))
# zadanie3
def ile_usuniec(text, letter):
    ilosc = 0
    for i in text:
        if i == letter:
            ilosc = ilosc + 1
    return ilosc

print(ile_usuniec("Ala ma kota","a"))

