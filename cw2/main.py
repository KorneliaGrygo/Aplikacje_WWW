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

