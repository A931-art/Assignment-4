import matplotlib.pyplot as plt
import numpy as np
import time as tim


t0=tim.time()
a=12453756.56
b=120.345
m=1
n=10000 

x0=1.0

rand=[]
bas=[]

for i in range(n):
    x0=(a*x0+b)%m
    rand.append(x0)
    bas.append(i)
plt.hist(rand,range=(0.0,1.0),density='true',color="g",label="histogram")
plt.xlabel("Frequency")
plt.ylabel("Random numbers")
plt.legend()
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
    g[i]=f(rand[i])
plt.plot(rand,g,'k',label="uniform PDF")   
plt.legend() 
plt.grid(True)
plt.show()  
