def numerical(f,x):
    h=1e-4
    return(f(x+h)-f(x-h))/(2*h)

def func_tmp1(x):
    return x*x+4.**2.

def func_tmp2(x):
    return 3.**2.+x*x

print(numerical((func_tmp1),3.))
print(numerical((func_tmp2),4.))