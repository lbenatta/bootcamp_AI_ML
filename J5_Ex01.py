import pandas as pd
import numpy as np


# ------------- Foe bien,  ok ---------------------
#
# #def add_intercept(x)

dataset = [1,2,3,4,5,6,7,8,9,10,11,12]
dataset_df = pd.DataFrame(dataset)
data = dataset_df.to_numpy()

X=data[:,0]
Y=data[:, -1]
X=(np.column_stack((np.ones(np.size(X)),X)))

print(X)

x = np.arange(start=1, stop=10, step=1)
print(x.shape)
 
y = np.arange(1,10).reshape((3,3))
print(y)
print(y.shape)

A = np.ones((3, 1))
print(A)


z = np.column_stack((A, y))
print(z)


#