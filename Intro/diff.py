import numpy as np
import matplotlib.pyplot as plt

import sympy as sym
import sympy.plotting.plot as symplot

x = sym.symbols('x')

fx = 2*x**2

df = sym.diff(fx,x)

print(fx)
print(df)

symplot(fx,(x,-4,4),title='The function')
plt.show()

symplot(df,(x,-4,4),title='Its derivative')

relu = sym.Max(0,x)
sigmoid = 1 / (1+sym.exp(-x))

p = symplot(relu,(x,-4,4),label='ReLU', show=False,line_color='blue')
p.extend(symplot(sigmoid,(x,-4,4),label='Sigmoid',show=False,line_color='red'))
p.legend = True
p.title = 'The functions'
p.show()

p = symplot(sym.diff(relu),(x,-4,4),label='df(ReLU)',show=False,linecolor='blue')
p.extend(symplot(sym.diff(sigmoid),(x,-4,4),label='df(Sigmoid)',show=False,line_color='red'))
         
p.legend = True
p.title = 'The derivatives'
p.show()

