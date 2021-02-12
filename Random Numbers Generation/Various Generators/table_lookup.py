from pylab import *
from scipy.integrate import quad;
from scipy.interpolate import interp1d

print("Using Table-Lookup method to generate random variates")

p = lambda t : exp(-t**2/2.0)/sqrt(2*pi);
# CDF of normal distribution. 
F = lambda x : (quad(p,-inf,x))[0];


# Take discrete points (x,F(x))
Ns = 40;
x = linspace(-7,7,Ns);
y = zeros(Ns)
for i in range(Ns):
	y[i] = F(x[i]);

plot(x,y,'r*')

# Interpolate F
Fint = interp1d(x,y);

plot(x,Fint(x),'g--')
legend(['(x,F(x))','Interpolation'],loc=0);

figure()

Finv = interp1d(y,x);

# Sampling from U[0,1]
N = 10000;
u = rand(N)

# Now, we need to calculate Finv(u), which will
# gives us the samples we want.
x = Finv(u);

print("Mean of samples : ", mean(x))
print("Variance of samples :", var(x))

#PLOTTING GENERATED SAMPLES vs TRUE SAMPLES
hist(x,normed=True)

# We need to compare with samples from the Standard Normal distribution. 
un = randn(N);
hist(un,normed=True,color='red',alpha=0.6)

legend(['Samples generated via Table-Lookup','Actual/Real samples'], loc=1)

show()

