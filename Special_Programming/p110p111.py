import sys,os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax,cross_entropy_error
from common.gradient import numerical_gradient

class simNet:
    def __init__(self):
        self.W=np.random.randn(2,3)

    def pred(self,x):
        return np.dot(x,self.W)
    
    def loss(self,x,t):
        z=self.pred(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)
        return loss
    
net=simNet()
print(net.W)
x=np.array([.6, .9])
p=net.pred(x)
print(p)
t=np.array([0,0,1])
print(net.loss(x,t))

def f(W):
    return net.loss(x,t)

dW=numerical_gradient(f,net.W)
print(dW)