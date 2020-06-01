import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if(x>3 and x<7):
        return 1.0
    else:
        return 1e-19
def g():
    return np.random.standard_normal()

n=5000
x=3.0
array=[]
chain=[]
narray=np.zeros(n)

for i in range(n):
    X=x+g()
    ran=np.random.rand()
    chain.append(X)
    narray[i]=i
    if (f(X)/f(x)) > ran:
        x=X
    if(x>3 and x<7):
        array.append(x)

nbins=10
fig1=plt.subplots()
plt.hist(array,nbins,histtype='bar',color='green',ec='white')
plt.grid(True)



#--------------------------------------------------------------#



print(np.amax(chain))
fig2=plt.subplots()
plt.scatter(narray,chain)
axes = plt.gca()
axes.set_ylim([np.amin(chain),np.amax(chain)])
plt.plot(array,color='red')
plt.grid(True)
plt.show()
