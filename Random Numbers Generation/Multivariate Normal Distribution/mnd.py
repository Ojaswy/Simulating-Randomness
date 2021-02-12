'''
Simulate X a multivariate normal distribution
with following mean vector and variance covariance matrix.
μ = [20,30,50,35,15], Σ = [[174, 134, 83, 98, 80],[134, 202, 76, 150, 141],
[83, 76, 60, 53, 40], [98, 150, 53, 127, 114], [80, 141, 40, 114, 112]]
Generate 100 random numbers , find the mean and Variance Covariance
matrix
'''
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from scipy.stats import multivariate_normal


# set the dimension
d = 5

# Set mean vector 
m = np.array([20,30,50,35,15])

# Set covariance function
K_0 = np.array([[174, 134, 83, 98, 80],[134, 202, 76, 150, 141],[83, 76, 60, 53, 40], [98, 150, 53, 127, 114], [80, 141, 40, 114, 112]])


# Eigenvalues covariance function
np.linalg.eigvals(K_0)

# Define epsilon
epsilon = 0.0001

# Add small pertturbation
K = K_0 + epsilon*np.identity(d)

#  Cholesky decomposition
L = np.linalg.cholesky(K)

np.dot(L, np.transpose(L))

# Number of samples
n = 100

#Drawing Samples from the data
z = np.random.multivariate_normal(mean=m.reshape(d,), cov=K, size=n)
y = np.transpose(z)

mu = []
print(np.cov(y))
for l in y:
	mu.append(sum(l)/len(l))
print(mu)

#kind{ “scatter” | “kde” | “hist” | “hex” | “reg” | “resid” }

# Plot density function.
#sns.jointplot(x=y[0], y=y[1], kind="kde", space=0);
#sns.jointplot(x=y[0], y=y[1], kind="scatter", space=0);
#sns.jointplot(x=y[0], y=y[1], kind="hex", space=0);
#sns.jointplot(x=y[0], y=y[1], kind="reg", space=0);
#sns.jointplot(x=y[0], y=y[1], kind="resid", space=0);
sns.boxplot(x=y[1])
plt.show()

