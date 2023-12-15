import numpy as np
import torch

A  = torch.randn(3,4)
B  = torch.randn(4,5)
C1 = np.random.randn(4,7)
C2 = torch.tensor(C1,dtype=torch.float)

print(np.round(A@B,2)),print(' ')
# print(np.round(A@B.T,2)),print(' ')
print(np.round(A@C1,2)),print(' ')
print(np.round(A@C1,2)),print(' ')
print(np.round(A@C2,2)),print(' ')