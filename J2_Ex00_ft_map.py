


#----------------- map ------------------------
x = [1,2,3,4,5]   # x = list
print (x)

map(lambda x: 2 * x, x) 
print(map(lambda x: 2 * x, x) )

#list(map(double, x))

list(map(lambda n: n * -1, x))
print(list(map(lambda n: n * -1, x)))

list(map(lambda t: t + 1, x))
print(list(map(lambda t: t + 1, x)))

#----------------- filter ------------------------

strs = ['apple', 'and', 'a', 'donut']

list(filter(lambda s: len(s) > 3, strs))
print(list(filter(lambda s: len(s) > 3, strs)))
# ['apple', 'donut']

nums = [5, 3, 6, 1, 7, 2]
list(filter(lambda n: n % 2 == 1, nums))
print(list(filter(lambda n: n % 2 == 1, nums)))
# [5, 3, 1, 7]

filter(lambda dum: not (dum % 2), nums)
print(filter(lambda dum: not (dum % 2), nums))

list(filter(lambda dum: not (dum % 2), nums))
print(list(filter(lambda dum: not (dum % 2), nums)))

#----------------- reduce ------------------------

import functools
import operator

x = [1,2,3,4,5]   # x = list

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, x))
 
# using reduce to compute product
# using operator functions


print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, x))
 
# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["Hel", "lo", "world"]))
