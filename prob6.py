import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sqrt(2/np.pi)*np.exp((-x**2)/2)

x=np.random.rand(10000)
x=-np.log(x)
a=1.5*np.exp(-x)
y=np.random.rand(10000)*a
z=[]

for i in range(10000):
    if(y[i]<=f(x[i])):
        z.append(x[i])
plt.hist(z,range=(0.0,10.0),bins=50,density='true',color="green")
x=np.arange(0.0,10.0,0.05)
b=np.sqrt(2/np.pi)*np.exp((-x**2)/2)
plt.plot(x,b,'r')
plt.grid(True)
plt.show()
