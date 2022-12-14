import numpy as np

# --------------------------- ok ----------------------

def simple_gradient(x, y, theta):
    #print(x)
    #print(x.shape)
    x = np.c_[np.ones(x.shape[0]),x]
    #print("x", x)
    T_x = x.transpose()
    #print("T_X", T_x)
    m = len(y)
    #print("y", y)

    x_T = np.matmul(x, theta) 
    #print("X * T", x_T)

    diff = x_T - y
    #print("diff:", diff)

    delta = np.matmul(T_x, diff) 
    #print("delta:", delta)

    V = (delta/m) 
    print("V", V)
    return(V)

x = np.array([
[ -6, -7, -9],
[ 13, -2, 14],
[ -7, 14, -1],
[ -8, -4, 6],
[ -5, -9, 6],
[ 1, -5, 11],
[ 9, -11, 8]])
y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
theta = np.array([0.0,3,0.5,-6]).reshape((-1, 1))

simple_gradient(x, y, theta)
