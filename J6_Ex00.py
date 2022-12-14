import numpy as np

# -----------------------∇(J) = (1 / m) * X0T(X0θ − y)
# ----------------- ok ------------------------------------------------------
#def simple_gradient(x, y, theta):
n = 5

x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
print(x)
x=x[:, -1]
x=(np.column_stack((np.ones(np.size(x)),x)))
print("x", x)
T_x = x.transpose()
print("T_X", T_x)

y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
print("y:", y)

theta1 = np.array([2, 0.7]).reshape((-1, 1))
print("theta1", theta1)
X_T = np.matmul(x, theta1) 
print("X * T", X_T)

diff = X_T - y
print("diff:", diff)

prod = np.matmul(T_x, diff) 
print("prod:", prod)

V = (prod/n) 
print("V", V)

