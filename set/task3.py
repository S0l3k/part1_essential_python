#На основании 3 исходных множеств (передаются в качестве аргументов функции diff()) 
# требуется написать функцию, которая будет возвращать либо симметричную разность, 
# либо просто разность (если дополнительный аргумент функции symmetric имеет значение False) 
# приведенных объектов в порядке: 1-ое множество, 2-ое множество, 3-е множество.


set1 = {3, 4, 5, 6, 20}
set2 = {4, 6, 7, 8, 9}
set3 = {5, 3, 8, 1}

def diffOfSets(firstSet, secondSet, thirdSet, symmetric=True):
    """14.10.2025"""

    if symmetric:
        return firstSet ^ secondSet ^ thirdSet
    return firstSet - secondSet - thirdSet

print(diffOfSets(set1, set2, set3))
print(diffOfSets(set1, set2, set3, symmetric=False))