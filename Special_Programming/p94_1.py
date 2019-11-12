import numpy as np

def cross_entropy_error(y,t):
    if y.ndim==1:
        t=t.reshape(1,t.size)
        y=y.reshape(1,y.size)
    
    batch_size=y.shape[0]
    return -np.sum(t*np.log(y+1e-7))/batch_size

t=[0,0,1,0,0,0,0,0,0,0]
y=[.1,.05,.6,.0,.05,.1,.0,.1,.0,.0]
print(cross_entropy_error(np.array(y),np.array(t)))

y=[.1,.05,.1,.0,.05,.1,.0,.6,.0,.0]
print(cross_entropy_error(np.array(y),np.array(t)))