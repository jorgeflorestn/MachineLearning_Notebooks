import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

m = 150
X = 2 * np.random.rand(m, 1)
x_real = np.array([0, 0.5, 1, 1.25, 1.5, 2])
y_real = 3 + 4*x_real
y = 3 + 4*X + 1.5*np.random.randn(m, 1)

plt.plot(X, y, "b.")
plt.plot(x_real[:], y_real[:], "r-", linewidth = 2, label = "Real line")
plt.xlabel('X', fontsize = 16)
plt.ylabel('y', fontsize = 16, rotation = 0)
plt.axis([0, 2, 0, 15])
plt.legend(loc = "upper left", fontsize = 11)
plt.grid(True)
plt.show()

eta = 0.09
epochs = 1000
theta = np.random.randn(2,1)
X_b = np.c_[np.ones((m,1)), X]

J_log = np.zeros(epochs)
for i in range(epochs):
    J_log[i] = (2/m) * ((X_b@theta - y)**2).sum()
    gradients = (1/m) * (X_b.T @ (X_b@theta - y))
    theta = theta - eta*gradients
else: print(theta)

a_0 = theta[0]
a_1 = theta[1]

y_pred = a_0 + a_1 * X

plt.plot(X, y_pred, "b.")
plt.plot(x_real[:], y_real[:], "r-", linewidth = 2, label = "Real line")
plt.xlabel('X', fontsize = 16)
plt.ylabel('y', fontsize = 16, rotation = 0)
plt.axis([0, 2, 0, 15])
plt.legend(loc = "upper left", fontsize = 11)
plt.grid(True)
plt.show()


plt.plot(np.arange(epochs), J_log, "b-", linewidth=2)
plt.xlabel("iterations", fontsize=14)
plt.ylabel(r"$J(\theta)$", fontsize=14)
plt.show()