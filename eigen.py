import numpy as np 

#this will be the x
A= np.array([[4,2],
             [1,3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues) #this is the lambda
print("Eigenvectors:\n", eigenvectors) #this is A