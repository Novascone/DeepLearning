import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

Z = [1,2,3]

# softmax

num = np.exp(Z)
den = np.sum(np.exp(Z))
sigma = num / den

print(sigma)
print(np.sum(sigma))


Z = np.random.randint(-5,high=15,size=25)
print(Z)

num = np.exp(Z)
den = np.sum(num)
sigma = num / den

plt.plot(Z,sigma,'ko')
plt.xlabel('Original number (z)')
plt.ylabel('Softmax $\sigma$')
# plt.yscale('log')
plt.show()

soft = nn.Softmax(dim=0)

sigmaT = soft(torch.Tensor(Z))

print(sigmaT)

plt.plot(Z,sigmaT,'ko')
plt.xlabel('Original number (z)')
plt.ylabel('Softmax $\sigma$')
# plt.yscale('log')
plt.show()