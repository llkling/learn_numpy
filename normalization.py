import numpy as np 

v=np.array([3,4])

mag=np.linalg.norm(v)
unit_v = v/mag

print(f"Magnitude: {mag}")
print(f"Unit Vector: {unit_v}")
print(f"New Magnitude check: {np.linalg.norm(unit_v)}")