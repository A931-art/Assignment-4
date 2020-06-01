import numpy as np
import matplotlib.pyplot as plt
import time as tim


t0=tim.time()
n=10000
x=np.random.rand(n)

plt.hist(x,range=(0.0,1.0),density='true',color="blue",label='histogram')
plt.legend()
plt.xlabel("Frequency")
plt.ylabel("Random numbers")
plt.grid(True)

tp=tim.time()
print(tp-t0)

x_max=1.0
x_min=0.0
diff=x_max-x_min

def f(x):
    return float(1/diff)
g=np.zeros(n,dtype=float)

for i in range(n):
    g[i]=f(x[i])
plt.plot(x,g,'r',label="uniform PDF")   
plt.legend() 
plt.grid(True)
plt.show()
