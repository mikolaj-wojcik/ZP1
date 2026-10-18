'''Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list, a drugi typu int . 
Funkcja ma sprawdzić (zwracając typ logiczny bool), 
czy lista z parametru pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.'''


def nalezy_do_zbioru(lista: list, num: int) -> bool:
    return num in lista


if nalezy_do_zbioru([8,9,10,4,1],1):
    print('Zawiera się w liście')
else:
    print('Nie zawiera się w liście')