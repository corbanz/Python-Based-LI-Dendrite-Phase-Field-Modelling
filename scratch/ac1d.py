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
# plt.plot(x, xi) #plot the generated random variables against x
# plt.show()
# u = np.sin(x)
# d2=(u[2:]+u[:-2]-2*u[1:-1])/dx**2 #∇²ξ smoothing force!
# exact = -np.sin(x[1:-1])
# print(d2[:3], exact[:3])
# E = np.max(np.abs(d2 - exact)) #error between the computed second derivative and the exact second derivative
# print(E)
# lap = (xi[2:]+xi[:-2]-2*xi[1:-1])/dx**2
# hp = 2*xi[1:-1]*(1-xi[1:-1])*(1-2*xi[1:-1])
# rate = M * (kappa * lap - hp) #righthand side of allen cahn
# # print(rate.min(), rate.max())
# # print(hp.min(), hp.max())
# # print(kappa*lap.min(), kappa*lap.max())
# dt = 0.1 * dx**2 / (M * kappa)
# # r*dx^2/(M*kappa), r=0.1 chosen. Stable only if r<=0.5: a zigzag mode is multiplied by (1-4r) each step, need |1-4r|<=1
# xi_new = xi.copy()
# xi_new[1:-1] = xi[1:-1] + dt * rate
steps = 2000
count = 1
xi0=xi.copy()
dt = 0.1 * dx**2 / (M * kappa)
while count <= steps:
        count += 1
        lap=(xi[2:]+xi[:-2]-2*xi[1:-1])/dx**2
        hp=2*xi[1:-1]*(1-xi[1:-1])*(1-2*xi[1:-1])
        rate=M * (kappa * lap - hp)
        xi_new = xi.copy()
        xi_new[1:-1] = xi[1:-1] + dt * rate
        xi = xi_new


plt.plot(x, xi0)
plt.plot(x, xi_new)
plt.show()