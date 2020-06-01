import numpy as np
import matplotlib.pyplot as plt


n=10000
x_1=np.random.rand(n)
x_2=np.random.rand(n)

y_1=np.sqrt(-2*np.log(x_1))*np.cos(2*np.pi*x_2)
plt.hist(y_1,range=(-10,10),bins=50,density='true',color="c",label='histogram')
plt.legend()
plt.grid(True)

x=np.arange(-10,10,0.05)
gaus=(1/np.sqrt(2*np.pi))*np.exp((-x**2)/2)
plt.plot(x,gaus,'k',label='Gaussian PDF')
plt.legend()
plt.grid(True)
plt.show()
