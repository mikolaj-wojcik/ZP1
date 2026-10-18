'''
Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list. 
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty,
 każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.
'''


def polacz_listy(lista1: list, lista2:list) -> list:
    lista = lista1 + lista2
    lista = list(set(lista))

    lista_pow = [elem ** 3 for elem in lista]
    return lista_pow


print(polacz_listy([33,55,1], [4,3,1]))