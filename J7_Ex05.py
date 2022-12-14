import pandas as pd
import numpy as np
# ------------------ ne foe [as, a terminer ----------------------]
def    add_intercept(x):
    ones = np.ones(len(x))
    return (np.c_[ones, x])

def    simple_gradient(x, y, theta):
    m = len(x)
    X = add_intercept(x)
    X_T = X.transpose()
    X = np.matmul(X, theta)
    return (1/m) * np.matmul(X_T, X - y)

class    MyLinearRegression():
    def    __init__(self, theta, alpha, max_iter):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = theta

    def fit_(self, x, y):
        new_theta = self.theta
        for i in range(self.max_iter):
            new_theta = new_theta - self.alpha * simple_gradient(x, y, new_theta)
        self.thetas = new_theta

    def    predict_(self, x):
        x_=add_intercept(x)
        return(np.matmul(x_, self.theta))

    def    loss_elem_(self, y, y_hat):
        return((y_hat - y)**2)

    def    loss_(self, y, y_hat):
        diff = y_hat - y
        half_emq = sum((xi)**2 for xi in diff) / (2 * len(diff))
        return (half_emq)
#### mse = loss ? lomg et non par  2 x la longeur 
#rom mylinearregression import MyLinearRegression as MyLR

if    __name__=="__main__":
    np.set_printoptions(suppress=True)
    data = pd.read_csv("spacecraft_data.csv")
    X = np.array(data[['Age']])
    Y = np.array(data[['Sell_price']])
    myLR_age = MyLinearRegression(theta = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 100000)
    myLR_age.fit_(X[:,0].reshape(-1,1), Y)
    y_pred = myLR_age.predict_(X[:,0].reshape(-1,1))
    myLR_age.mse_(y_pred,Y)