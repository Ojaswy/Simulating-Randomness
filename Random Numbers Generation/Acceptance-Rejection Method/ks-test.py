import numpy as np
import math
import scipy.stats
from pylab import *
from scipy.integrate import quad;

# KS GOODNESS OF FIT TEST with level of significance Alpha = 0.05
# Please refer to the attached PDF file('E2_17MCME05.pdf') for the algorithm used here.

print("\nH0 : No  significant  difference  between  the  sample  distribution  and  the  theoretical distribution.")
print("\nH1 : Significant difference exists between the sample distribution and the theo-retical distribution.\n")
def ks(arr):
	arr.sort()
	# PDF of normal distribution
	p = lambda t : exp(-t**2/2.0)/sqrt(2*pi);
	# CDF of normal distribution. 
	F = lambda x : (quad(p,-inf,x))[0];
	dplus = []
	dminus = []
	N = len(arr)
	for i in range(N):
		y = arr[i]
		dp = float(float((i+1)/N) - float(F(y)))
		dm = float(float(F(y)) - float(i/N))
		dplus.append(dp)
		dminus.append(dm)
	#print(dplus, dminus)
	Dplus = max(dplus)
	Dminus = max(dminus)
	D = max(Dplus, Dminus)
	# For N over 35 and level of significance being 0.05, the critical value can be calculated by 1.36/squareroot(N) | Reference : Discrete Event System SImulation - Jerry Banks
	Dcritical = float(1.36/(math.sqrt(N)))
	print("\nD: ",D)
	print("Dcritical: ", Dcritical)
	print("\nKolmogorov-Smirnov Test Result: ")
	if D <= Dcritical:
		print("No significant difference detected between the sample distribution and theoretical Normal distribution. H0 is accepted.")

	else:
		print("Significant difference exists between the sample distribution and theoretical Normal distribution. H0 is rejected.")		
	
			
# GENERATING A SAMPLE USING REJECTION METHOD
# We will run the Kolmogorov-Smirnov Test on this generated sample
def sample_normal_rejection(mu, sigma):

	# Length of interval from wich samples are drawn
	interval = 10*sigma
	# Maximum value of the pdf of the desired normal distribution
	max_density = scipy.stats.norm(mu,sigma).pdf(mu)
	# Rejection loop
	while True:
		x = np.random.uniform(mu - interval, mu + interval, 1)[0]
		y = np.random.uniform(0, max_density, 1)
		if y <= scipy.stats.norm(mu, sigma).pdf(x):
			break
	return x

def evaluate_sampling_dist(mu, sigma, n_samples, sample_function):
	n_bins = 100
	samples = []

	for i in range(n_samples):
		samples.append(sample_function(mu, sigma))
	#Running KS test on the generated samples	
	ks(samples)	

mu = 0
sigma = 1
n_samples = 1000
evaluate_sampling_dist(mu, sigma, n_samples, sample_normal_rejection)

