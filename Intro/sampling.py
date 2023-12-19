import numpy as np
import matplotlib.pyplot as plt

x = [1,2,4,6,5,4,0,-4,5,-2,6,10,-9,1,3,-6]
n = len(x)

popmean = np.mean(x)

sample = np.random.choice(x, size=5,replace=True)
samplemean = np.mean(sample)

print(popmean)
print(samplemean)

experiments = 10000

sampleMeans = np.zeros(experiments)
for i in range (experiments):
    
    sample = np.random.choice(x, size=5, replace=True)
    sampleMeans[i] = np.mean(sample)
    
plt.hist(sampleMeans,bins=40,density=True)
plt.plot([popmean,popmean],[0,.3],'m--')
plt.ylabel('Count')
plt.xlabel('Sample mean')
plt.show()
