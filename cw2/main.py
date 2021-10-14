# zadanie_1

def lista(a_list, b_list):
    nowa = list()
    dlugosc_list = len(a_list) if len(a_list) > len(b_list) else len(b_list)
    for i in range(0,dlugosc_list):
        if i % 2 == 0:
            nowa.append(a_list[i])
        else:
            nowa.append(b_list[i])
    return nowa


lista_a = [0,2,4,6,8]
lista_b = [2,1,3,7]
print(lista(lista_a,lista_b))

# zadanie_2


def informacje(data_text):
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


print(informacje("Kasia ma trzy nogi"))

# zadanie_3


def usuwanko(text, letter):
    text = text.lower()
    ilosc = 0
    for i in text:
        if i == letter:
            ilosc = ilosc + 1
    return ilosc


print(usuwanko("Asia ma dwa koty","a"))

# zadanie_4


def przelicz(temperature_type, celsjusz):
    temperature_type = temperature_type.lower()
    if temperature_type == "fahrenheit":
        celsjusz = (celsjusz * 1.8) + 32
    elif temperature_type == "rankine":
        celsjusz = (celsjusz + 273.15) * 1.8
    elif temperature_type == "kelvin":
        celsjusz = celsjusz + 273.15
    else:
        return "błędne wartości"
    return celsjusz


print(przelicz("KELVIN", 37))

# zadanie_5


class Calculator:

    def add(self,x,y):
        return x+y

    def difference(self,x,y):
        return x-y

    def multiply(self,x,y):
        return x*y

    def divide(self,x,y):
        return x/y

# zadanie_6


class ScienceCalculator(Calculator):
    def exponentiation(self,x,y):
        return x**y

# zadanie_7


def od_tyłu(s):
    return s[::-1]


print(od_tyłu("kornelia"))

# zadanie_9

from cw2.file_manager import FileManager
menago = FileManager("kotek.txt")
print(menago.read_file())
menago.update_file(" i jeden ogonek. ")
print(menago.read_file())
