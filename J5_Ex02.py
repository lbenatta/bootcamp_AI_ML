import numpy as np
from numpy.linalg import inv 


#--------------- Foe bien, ok ----------------------------------------
x = np.arange(1, 6)
#x = inv(x)
x = np.arange(1,6).reshape((5,1))
print(x)
print(x.shape)

# X=x[: , 0]

Y=x[:, -1]
X=(np.column_stack((np.ones(np.size(x)),x)))
print(X)

theta1 = np.array([[-3], [1]])


y_hat = np.matmul(X, theta1)
print("y_hat:", y_hat)



#---------------- si on veut saisir les valeurs de x a l main --------------------

# if isinstance(x, np.ndarray):
#     pass
# else:
#     print("x is not numpy.array. ")  
#     #break  
# #x = [1,2,3,4,5,6,7,8,9,10,11,12]
# def predict_(x, theta):
# #    y = theta * x
#     #y_hat = theta * x 
#     
#     print("y_hat:", y_hat)

# """Computes the vector of prediction y_hat from two non-empty numpy.array.
# Args:
# x: has to be an numpy.array, a vector of dimension m * 1."""
# # x = np.array(m, 1)
# list1 = []
# size = x.itemsize
# option = "Y"
# for x in range(size):
#     ele = input("Enter Element For List One : ")
#     list1.append(ele)
# while(option == "Y"):
#     option = input("\n***Add More Element Press Y ***: ")
#     if(option=="Y"):
#         size = size + 1
#         for x in range(size):
#             ele = input("Enter Element For List Element : ")
#             list1.append(ele)
#             size = 1
#     else:
#         print('theta is not numpy.array')
#         break
# print(list1)