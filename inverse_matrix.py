import numpy as np

A = ([[3,1],
      [4,2]])

A_inv = np.linalg.inv(A)
print(A_inv)
print(A@A_inv) #we got the Indentity Matrix