#input array
import numpy as np
A=[1,2,3,4,5,6]
for i in range(len(A)):
    B=[a for a in A if(a!=A[i])]
    print(np.product(B))
    
 #Output
 [6,3,2]
