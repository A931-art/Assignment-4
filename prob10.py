import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner


File=open("data.txt","r")
lines=File.readlines()
File.close()

x=[]
y=[]
yerr=[]

for line in lines[0:]:	
	delimiter = "&"	    
	ls=line.split(delimiter)
	x.append(float(ls[1]))
	y.append(float(ls[2]))
	yerr.append(float(ls[3]))

x=np.transpose(np.asarray(x))
y=np.transpose(np.asarray(y))
yerr=np.asarray(yerr)

def polynomial_fitting(const,x):
	a,b,c=const
	y=a*x**2+b*x+c
	return( y)    

def log_likelihood(theta, x, y, yerr):
	a,b,c = theta
	model = a*x*x+b*x+c
	sigma_y2 = yerr**2
	return (0.5*np.sum((y - model)**2/sigma_y2 +np.log(2*np.pi*sigma_y2)))

def log_prior(theta):
	a,b,c = theta
	if (-500.0< a <500.0 and -500.0< b <500.0 and -500.< c <500.0):
		return (0.0)
	return (-np.inf)

def log_probability(theta, x, y, yerr):
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return (-np.inf)
	return (lp - log_likelihood(theta, x, y, yerr))

guess = (1.0, 1.0, 1.0)
soln = minimize(log_likelihood,guess,args=(x, y, yerr))

nchain, dim =50,3
pos = soln.x + 1e-4*np.random.randn(nchain, dim) 

sampler=emcee.EnsembleSampler(nchain,dim,log_probability,args=(x, y, yerr)) 

sampler.run_mcmc(pos, 4000)
p_data = sampler.get_chain() 
parameter_data = sampler.get_chain(discard=200,thin=30,flat=True) 

fig, axs = plt.subplots(3)
#fig.suptitle('50 Markov chains for first 200 steps for three parameters')
axs[0].plot(p_data[1:200, :, 0],'--r',linewidth='0.5')
axs[0].set_title('for parameter a')
axs[1].plot(p_data[1:200, :, 1],'--g',linewidth='0.5')	    
axs[1].set_title('for parameter b')
axs[2].plot(p_data[1:200, :, 2],'--b',linewidth='0.5')
axs[2].set_title('for parameter c')

for ax in axs.flat:
    ax.set(xlabel='Steps', ylabel='Range')
for ax in axs.flat:
    ax.label_outer()

medians = np.median(parameter_data,axis=0) 
a_true,b_true,c_true= medians

labels=["a","b","c"]
fig2=corner.corner(parameter_data,labels=labels,truths=[a_true,b_true,c_true])

x0 = np.linspace(40, 300, num=500)

points=np.random.randint(len(parameter_data), size=200)
fig3 = plt.figure()
for j in points:
	sample = parameter_data[j]  
	plt.plot(x0,polynomial_fitting(sample[:3],x0), 'skyblue')

plt.errorbar(x, y, yerr, fmt=".r", capsize=3) 
plt.plot(x0, a_true * x0**2 + b_true*x0 + c_true, "k", label="Best fit") 
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
