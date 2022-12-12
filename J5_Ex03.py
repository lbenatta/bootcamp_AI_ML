import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pyplot


x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

x_1 = np.arange(1,6).reshape((5,1))
Y=x_1[:, -1]
X=(np.column_stack((np.ones(np.size(x)),x)))
theta1 = np.array([[4.5],[-0.2]])
y_hat = np.matmul(X, theta1)

plt.scatter(x, y)
plt.plot(x, y_hat, color = 'red', linestyle = 'solid')
plt.ylabel('y pred and hat')
plt.show()