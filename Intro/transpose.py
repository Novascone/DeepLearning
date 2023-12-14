import numpy as np
import torch

v = np.array([[1,2,3,4]])
print(v),print(' ')

print(v.T), print(' ')

A = np.array([[1,2,3,4],[5,6,7,8]])
print(A),print(' ')

print(A.T), print(' ')


# pytorch

tv = torch.tensor([1,2,3,4])
print(tv), print(' ')

print(tv.T), print(' ')

tA = torch.tensor([[1,2,3,4],[5,6,7,8]])

print(tA), print(' ')

print(tA.T), print(' ')