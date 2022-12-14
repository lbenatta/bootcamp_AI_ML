import numpy as np
# --------------------------- ok ----------------------
def simple_gradient(x, y, theta):
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
    #print("V", V)
    return(V)

def fit(x, y, theta, alpha, max_iter):
    tmp_theta = theta
    for i in range (max_iter):
        tmp_theta = tmp_theta - alpha * simple_gradient(x, y, tmp_theta) 
        print(tmp_theta)
    return(tmp_theta) 

x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])

fit(x, y, theta, alpha = 0.0005, max_iter=42000)