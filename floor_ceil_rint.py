import numpy as np 

np.set_printoptions(legacy='1.13')

arr=np.array(input().split(),dtype=float)

print(np.floor(arr))  # greatest integer <= x
print(np.ceil(arr))   # smallest integer >= x
print(np.rint(arr))  # round off to nearest int 
