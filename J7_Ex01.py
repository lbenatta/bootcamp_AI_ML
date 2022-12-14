import numpy as np

# ---------------------ok -----------
def loss_elem_(X, Y):
        loss_el = (X - Y) ** 2
        print(loss_el)
        return (loss_el)

def loss_(X, Y):
    #loss_ = ((X - Y) ** 2) / len(X)
    loss_ = loss_elem_(X, Y).mean() / 2
    print(loss_)
    return (loss_)
    #return loss_elem_(y, y_hat).mean() / 2

X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((-1, 1))
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
loss_elem_(X, Y)
loss_(X, Y)
