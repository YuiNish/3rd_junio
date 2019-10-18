#トラヒックとスループットの関係

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x*np.exp(-x)/(3*x+np.exp(-x))

x=np.arange(0.,25.,0.01)
y=function(x)
plt.plot(x,y)
plt.show()