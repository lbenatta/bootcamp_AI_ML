import numpy as np
import matplotlib.pyplot as plt

def simple_gradient(x, y, theta):
    x=x[:, -1]
    x=(np.column_stack((np.ones(np.size(x)),x)))
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

def cost(theta,x,y):
    m = len(y)
    # Calculating Cost
    cost[0] = (1/2*m) * np.sum(np.square((np.matmul(x, theta[0]))-y))
    cost[1] = (1/2*m) * np.sum(np.square((np.matmul(x, theta[1]))-y))
    return (c[0], c[1])
# print("c:", cost)

#def loss ()
#theta = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
#theta
# # Output:
# array([[1.40709365],
# [1.1150909 ]])
# # Example 1:
# predict(x, theta1)
# # Output:
# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])

if __name__== '__main__':
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]]).reshape((-1, 1))
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]]).reshape((-1, 1))
    theta = np.array([1.0, 1.0]).reshape((-1, 1))
    #simple_gradient(x, y, theta)
    fit(x, y, theta, 5e-8, 1500000)
    cost(theta, x, y)

# def cost(theta0,x,y):
#     m = len(y)
#     # Calculating Cost
#     c = (1/2*m) * np.sum(np.square((np.matmul(x, theta0))-y))  
#     return c
# print("c:", cost)

# def gradient_descent(X,y,theta,alpha,max_iterations):
#     m = len(y)
#     # Initializing cost and theta's arrays with zeroes.
#     theta1 = np.zeros((max_iterations,2))
#     costs = np.zeros(max_iterations)
#     # Calculating theta for every iteration.
#     for i in range(max_iterations):
#             theta0 = theta0 - (1/m)*alpha*(X.T.dot((X.dot(theta0))-y))
#             theta1[i,:] = theta.T
#             costs[i] = cost(theta0,X,y)
#     print(theta0,theta1,costs)
#     return theta0,theta1,costs
# Learning Rate
#alpha = 5e-8
# Number of iterations
#max_iterations = 1500000
# Initializing a random value to give algorithm a base value.
#theta0 = 0  
#theta1 = 0                                               # or = np.random.randn(2,1)
# Adding a biasing constant of value 1 to the features array.
#X_bias = np.c_[np.ones((len(X),1)),X]
# Running Gradient Descent
#theta,thetas,costs = gradient_descent(X_bias,y,theta,alpha,max_iterations)
# printing final values.

# print('Final Theta0 value: {:0.3f}\nFinal Theta1 value: {:0.3f}'.format(theta[0][0],theta[1][0]))
# print('Final Cost/MSE(L2 Loss) Value: {:0.3f}'.format(cost[-1]))
