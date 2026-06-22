
numbers = [1,2,3,4,5]


addN= lambda x, n=0: x+n
map(addN, numbers)

result = map(addN, numbers)
print(result)  # returns map object
print(type(result))
from _collections_abc import Iterable

# map is Iterable

for i in result:
    print(f'{i}')





















