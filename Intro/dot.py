import torch

tv1 = torch.tensor([1,2,3,4])
tv2 = torch.tensor([0,1,0,-1])


print(torch.dot(tv1,tv2))

print(torch.sum(tv1*tv2))