import numpy as np

# ------------- ne Foe pas completement  ----------------------------

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
        #print(tmp_theta)
    return(tmp_theta) 

def predict_(x, y_hat):
    y_hat = np.matmul(x, theta)
    #y_hat = theta[0] + theta[1] * x
    return np.c_[np.ones(len(x)), x].dot(theta)
    #pred= theta[0] * x + theta[1]
    #return(pred[])

def loss_elem_(y, y_hat):
    y_hat = theta * x 
    return (y_hat - y) ** 2

def loss_(y, y_hat):
    return loss_elem_(y, y_hat).mean() / 2

if __name__== '__main__':
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]]).reshape((-1, 1))
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]]).reshape((-1, 1))
    theta = np.array([1.0, 1.0]).reshape((-1, 1))
    #simple_gradient(x, y, theta)
    fit(x, y, theta, 5e-8, 1500000)
    predict_(x, y_hat)
    loss_elem_(y, y_hat)
    loss_(y, )
    