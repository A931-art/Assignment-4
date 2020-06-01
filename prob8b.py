import numpy as np

def SphVol(dim, it):

    count=0

    for i in range(it):
        pt=np.random.uniform(-1.0,1.0,dim)
        dist=np.linalg.norm(pt)

        if dist<1.0:
            count+=1

    return np.power(2.0,dim)*(count/it)

print(SphVol(10,100000))
