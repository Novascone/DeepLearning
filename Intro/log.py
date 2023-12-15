import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0.0001,1,200)

logx = np.log(x)


fig = plt.figure(figsize=(10,4))

plt.rcParams.update({'font.size':15})

plt.plot(x,logx,'ks-',markerfacecolor='w')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.show()