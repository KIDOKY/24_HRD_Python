import numpy as np

X = np.array([0.0, 1.0, 2.0])
y = np.array([3.0, 3.5, 5.5])

W = 0.1
b = 0.1
lrate = 0.1
epochs = 1000
n = len(X)

for _ in range(epochs):
    y_pred = W * X + b
    dW = (2/n) * sum(X * (y_pred-y))
    db = (2/n) * sum(y_pred-y)
    W = W - lrate * dW
    b = b - lrate * db

    print(round(W))
    print(round(b))

    y_pred = W * X + b