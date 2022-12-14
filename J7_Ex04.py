import numpy as np

# ---------------------ok -----------

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
    def    __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def fit_(self, x, y):
        new_theta = self.thetas
        for i in range(self.max_iter):
            new_theta = new_theta - self.alpha * simple_gradient(x, y, new_theta)
        self.thetas = new_theta

    def    predict_(self, x):
        x_=add_intercept(x)
        return(np.matmul(x_, self.thetas))

    def    loss_elem_(self, y, y_hat):
        return((y_hat - y)**2)

    def    loss_(self, y, y_hat):
        diff = y_hat - y
        half_emq = sum((xi)**2 for xi in diff) / (2 * len(diff))
        return (half_emq)

if    __name__=="__main__":
    np.set_printoptions(suppress=True)
    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
    Y = np.array([[23.], [48.], [218.]])
    mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
    y_hat = mylr.predict_(X)
    print(y_hat)
    # np.array([[8.], [48.], [323.]])
    print(mylr.loss_elem_(Y, y_hat))
    # np.array([[225.], [0.], [11025``.]])
    print(mylr.loss_(Y, y_hat))

    mylr.alpha = 1.6e-4
    mylr.max_iter = 200000
    mylr.fit_(X, Y)
    print(mylr.thetas)
    # Output:
    # array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])
    # Example 4:
    y_hat = mylr.predict_(X)
    print(y_hat)
    # Output:
    # array([[23.417..], [47.489..], [218.065...]])
    # Example 5:
    print(mylr.loss_elem_(Y, y_hat))
    # Output:
    # array([[0.174..], [0.260..], [0.004..]])
    # Example 6:
    print(mylr.loss_(Y, y_hat))
    # Output:
    # 0.0732..