import numpy as np
import torch
import torch.nn as nn

v = np.array([1,40,2,-3])

minval = np.min(v)
maxval = np.max(v)

print('Min,max: %g,%g' %(minval,maxval))

minidx = np.argmin(v)
maxidx = np.argmax(v)

print('Min,max indices: %g,%g' %(minidx,maxidx)), print(' ')

print(f'Min val is {v[minidx]}, max val is { v[maxidx]}')

M = np.random.randint(1,6,size=(4,4))

minvals1 = np.min(M) # minimum of entire matrix
minvals2 = np.min(M, axis=0) # minimum of each column
minvals3 = np.min(M, axis=1) # minimum of each row

print(minvals1)
print(minvals2)
print(minvals3)

minidx1 = np.argmin(M) # minimum of entire matrix
minidx2 = np.argmin(M, axis=0) # minimum of each column
minidx3 = np.argmin(M, axis=1) # minimum of each row

print(minidx1)
print(minidx2)
print(minidx3)

v = torch.tensor([1,40,2,-3])

minval = torch.min(v)
maxval = torch.max(v)

print('Min,max: %g,%g' %(minval,maxval))

minidx = torch.argmin(v)
maxidx = torch.argmax(v)

print('Min,max indices: %g,%g' %(minidx,maxidx)), print(' ')

print(f'Min val is {v[minidx]}, max val is { v[maxidx]}')

M = torch.from_numpy(M)

min1 = torch.min(M)
min2 = torch.min(M, axis=0)
min3 = torch.min(M, axis=1)

print(min1),print(' ')
print(min2.values)
print(min2.indices)