import numpy as np

def num_grad(f,x):
    h=1e-4
    grad=np.zeros_like(x)

    for idx in range(x.size):
        tmp_val=x[idx]
        x[idx]=tmp_val+h
        fxh1=f(x)

        x[idx]=tmp_val-h
        fxh2=f(x)

        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val
    return grad

def func2(x):
    return x[0]**2+x[1]**2

print(num_grad(func2,np.array([3., 4.])))
print(num_grad(func2,np.array([.0, 2.])))
print(num_grad(func2,np.array([3., .0])))