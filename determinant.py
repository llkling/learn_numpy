import numpy as np

B = np.array ([[1,2],
               [10,20]])
det_B = np.linalg.det(B)

print(det_B)
#Mindful about how the result is not == 0 here.
