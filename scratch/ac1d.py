import numpy as np
import matplotlib.pyplot as plt
N=100 #points along x
L=1.0 #domain length
M=1.0 #Mobility Coeff
kappa = 1e-3 #gradient energy coeff

x=np.linspace(0,L,N) #x coordinates, used to generate an array of evenly spaced numbers over a specified mathematical interval. Instead of defining the step size, you specify exactly how many elements you want in the array, and NumPy automatically calculates the required intervals.
dx=L/(N-1) #spacing between x coordinates
#print(x[1] - x[0])
rng = np.random.default_rng(0) #create a random number generator with a fixed seed for reproducibility
xi = rng.standard_normal(N)*.02+0.5 #store the generated random variables in a variable
#print(xi.min(), xi.max())
plt.plot(x, xi) #plot the generated random variables against x
plt.show()
# u = np.sin(x)
# d2=(u[2:]+u[:-2]-2*u[1:-1])/dx**2 #∇²ξ smoothing force!
# exact = -np.sin(x[1:-1])
# print(d2[:3], exact[:3])
# E = np.max(np.abs(d2 - exact)) #error between the computed second derivative and the exact second derivative
# print(E)
lap = (xi[2:]+xi[:-2]-2*xi[1:-1])/dx**2
hp = 2*xi[1:-1]*(1-xi[1:-1])*(1-2*xi[1:-1])
rate = M * (kappa * lap - hp) #righthand side of allen cahn
print(rate.min(), rate.max())
print(hp.min(), hp.max())
print(kappa*lap.min(), kappa*lap.max())