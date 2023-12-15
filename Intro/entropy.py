import numpy as np
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt 

x = [0.25, 0.75]

H = 0
for p in x:
    H += -p*np.log(p)
    
print('Entropy: ' + str(H))

# binary entropy
# H = -( p*np.log(p) + (1-p)*np.log(1-p))

# cross entropy 

cp = [1,0]
q = [0.25,0.75]

cH = 0
for i in range(len(cp)):
    cH += -cp[i]*np.log(q[i])

print('Cross entropy: ' + str(cH))

q_tensor = torch.Tensor(q)
p_tensor = torch.Tensor(cp)

torchce = F.binary_cross_entropy(q_tensor,p_tensor)

print(torchce)