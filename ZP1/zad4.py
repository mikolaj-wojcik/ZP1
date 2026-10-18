'''Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch 
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację jako typ logiczny bool'''


def sum_and_compare(a: int, b: int, c: int) -> bool:
    return (a + b) >= c



print (sum_and_compare(1,4,6))