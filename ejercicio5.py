from itertools import permutations

def permutaciones(texto):
    lista = list(texto)
    lista_a = lista.sort()

    new_list = list(permutations(lista))

    for i in new_list:
        while(new_list.count(i) > 1):
            new_list.remove(i)
    new_text = tuple(texto)
    return new_list.index(new_text) + 1

