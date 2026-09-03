import pandas as pd
import numpy as np

data = pd.read_csv('data/dataset.csv')

feature_cols = ['studytime', 'attendance', 'age']
X = data[feature_cols].values
y = data['score'].values.reshape(-1, 1)

X = np.c_[np.ones((X.shape[0], 1)), X]

w = np.zeros((X.shape[1], 1))

L = 0.0001
epochs = 1000
n = len(X)

for epoch in range(epochs):
    y_pred = X @ w

    gradient = (2 / n) * (X.T @ (y_pred - y))

    w = w - L * gradient

b = w[0][0]
m = w[1:].flatten()

print("b:", b)
print("m:", m)