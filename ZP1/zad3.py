'''Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest parzysta i 
zwróci tą informację jako typ logiczny bool (True/False). 
Należy uruchomić funkcję, wynik wykonania zapisać do zmiennej, 
a następnie wykorzystując warunek logiczny 
wyświetlić prawidłowy tekst "Liczba parzysta" / "Liczba nieparzysta"'''



def is_even (a) -> bool:
    return a%2 == 0


jest_parzysta = is_even(987)

if jest_parzysta:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')

