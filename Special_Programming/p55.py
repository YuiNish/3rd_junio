import numpy as np

A=np.array([[1,2],[3,4]])
print(A.shape)
B=np.array([[5,6],[7,8]])
print(B.shape)
print(np.dot(A,B))

print("\n")

AA=np.array([[1,2,3],[4,5,6]])
print(AA.shape)
BB=np.array([[1,2],[3,4],[5,6]])
print(BB.shape)
print(np.dot(AA,BB))