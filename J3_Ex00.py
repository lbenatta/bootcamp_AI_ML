import numpy as np

#class NumPyCreator:

lst = ["1","7", "0", "6", "2", "5", "6"]
ints = []
print((lst[0]))
print("lst:", type(lst))

list = np.array(lst) 
print("list", list[0])
print(type(list))

tuple1 = ([8, 4, 6], [1, 2, 3])
tup = np.asarray(tuple1)
print("tup:",tup)
print(type(tup))

iterable = (x*x for x in range(5))
ite = [x for x in iterable]
print("ite:", ite)
print(type(ite))

#from_shape(self, shape, value): 
tuple1 = ([8, 4, 6], [1, 2, 3])
tup = np.asarray(tuple1)
sha= tup.shape
print("sha:",sha)
print(type(sha))

# from random(self, shape): 
#ran = np.random.rand(self, shape)
ran = np.random.rand(3,2)
print("ran:",ran)
print(type(ran))

#id = np.identity(self, size)
id = np.identity(3)
print("id:",id)
print(type(id))