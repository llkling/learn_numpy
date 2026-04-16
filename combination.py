import numpy as np

v1 = np.array([1, 2])
v2 = np.array([3, 4])

# A linear combination: 2*v1 + (-1)*v2
w = 2*v1 - v2
print(w)

#Example 2
v1 = np.array([1,0])
v2 = np.array([0,1])
#A linear combination with c1=5, c2=3
w = 5*v1 + 3*v2
print(w)
