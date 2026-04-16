import numpy as np

#inner or dot product of two n-vectors
x = np.array([-10,0,10])
p = np.array([0.1,0.4,0.5])
resutl=np.inner(x,p)
print(resutl)

resutl = x@x
print(resutl)
print(p.shape)

#euclidean norm of an n-vector
e = np.array([-3,2,1,-1,1])
print(np.linalg.norm(e))

#rms
print(np.linalg.norm(e)/np.sqrt(len(e)))
