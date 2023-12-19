import numpy as np
import torch

np.random.randn(5)

np.random.seed(17)
print(np.random.randn(5))
print(np.random.randn(5))

randseed1 = np.random.RandomState(17)
randseed2 = np.random.RandomState(20210530)

print(randseed1.randn(5)) # same
print(randseed2.randn(5)) # different from previous, but same everytime
print(randseed1.randn(5)) # same as first
print(randseed2.randn(5)) # same as second
print(np.random.randn(5)) # random

# pytorch

print(torch.randn(5)),print(' ')

torch.manual_seed(17)
print(torch.randn(5))

# torch's seed doesn't spread to numpy

print(np.random.randn(5))

