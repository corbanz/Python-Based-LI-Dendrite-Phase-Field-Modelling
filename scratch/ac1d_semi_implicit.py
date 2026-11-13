import numpy as np
import matplotlib.pyplot as plt
N=100 #points along x
L=1.0 #domain length
M=1.0 #Mobility Coeff
kappa = 1e-3 #gradient energy coeff

x=np.linspace(0,L,N) #x coordinates, used to generate an array of evenly spaced numbers over a specified mathematical interval. Instead of defining the step size, you specify exactly how many elements you want in the array, and NumPy automatically calculates the required intervals.
dx=L/(N-1) #spacing between x coordinates
rng = np.random.default_rng(0) #create a random number generator with a fixed seed for reproducibility
xi = rng.standard_normal(N)*.02+0.5 #store the generated random variables in a variable
steps = 2000
count = 1
xi0=xi.copy()
r = 0.1  # smoothing parameter
dt = r * dx**2 / (M * kappa) 
# NOTE TO SELF: a point moves by ξ_new = ξ + 2r·(average of its neighbors − ξ)
# If r is small, each step moves the point a fraction of the way toward its neighbors’ average, which is smoothing.
# At r = 0.5, one step carries the point exactly to that average.
# Above 0.5, it overshoots past the average.
Lmat = np.zeros((N, N))
for i in range(1, N-1):
        Lmat[i, i-1] = 1.0
        Lmat[i, i] = -2.0
        Lmat[i, i+1] = 1.0
Lmat[0, 0] = -2.0
Lmat[0, 1] = 2.0
Lmat[-1, -1] = -2.0
Lmat[-1, -2] = 2.0
DivLap = Lmat / dx**2 # DivLap verified against lap: mismatch ~1e-12
A=np.eye(N)-dt*M*kappa*DivLap #semi-implicit matrix
while count <= steps:
        count += 1
        lap = np.zeros(N)
        lap[1:-1] = (xi[2:] + xi[:-2] - 2*xi[1:-1]) / dx**2 #smooths throughout
        lap[0]  = (2*(xi[1] - xi[0])) / dx**2 #smooths beginning
        lap[-1] = (2*(xi[-2] - xi[-1])) / dx**2 #smooths end
        hp=2*xi*(1-xi)*(1-2*xi)
        rate=M * (kappa * lap - hp)
        xi_new = xi + dt * rate
        xi = xi_new

plt.plot(x, xi0)
plt.plot(x, xi_new)
plt.show()
print(xi.min(), xi.max())