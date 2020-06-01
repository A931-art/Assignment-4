import numpy as np
from scipy.stats import chi2

s=[2,3,4,5,6,7,8,9,10,11,12]
p=[1,2,3,4,5,6,5,4,3,2,1]
Y1=[4,10,10,13,20,18,18,11,13,14,13]
Y2=[3,7,11,15,19,24,21,17,13,9,5]

n1=0
n2=0

for i in range(11):
    n1=n1+Y1[i]
    n2=n2+Y2[i]
    p[i]=p[i]/36.0

ex1=np.zeros(11,dtype=float)
ex2=np.zeros(11,dtype=float)

for i in range(11):
    ex1[i]=n1*p[i]
    ex2[i]=n2*p[i]

v1=np.zeros(11,dtype=float)
w1=0
for i in range(11):
    v1[i]=((Y1[i]-ex1[i])**2)/ex1[i]
    w1=w1+v1[i]
print(w1)
g1=1.0-chi2.cdf(w1,10.0)
print(g1)
if g1*100<1 or g1*100>99:
    print("Our random numbers are not sufficiently random")

v2=np.zeros(11,dtype=float)
w2=0
for i in range(11):
    v2[i]=((Y2[i]-ex2[i])**2)/ex2[i]
    w2=w2+v2[i]
print(w2)
g2=1.0-chi2.cdf(w2,10.0)
print(g2)
if g2*100<1 or g2*100>99:
    print("Our random numbers are not sufficiently random")
