import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

#Algorithm that has been implemented here is provided in 'E2_17MCME05.pdf'
def rejection(mu, sigma):
	interval = 10*sigma
	max_density = scipy.stats.norm(mu,sigma).pdf(mu)
	# Rejection loop
	while True:
		x = np.random.uniform(mu - interval, mu + interval, 1)[0]
		y = np.random.uniform(0, max_density, 1)
		if y <= scipy.stats.norm(mu, sigma).pdf(x):
			break
	return x

def sampling_dist(mu, sigma, n_samples, sample_function):
	n_bins = 100
	samples = []

	for i in range(n_samples):
		samples.append(sample_function(mu, sigma))
	print("Mean and Standard Deviation of the generated sample:")
	print("\nMean = " , np.mean(samples))   
	print("\nStandard Deviation = ", np.std(samples))
	print("\n\n")
	plt.figure()
	count, bins, ignored = plt.hist(samples, n_bins, normed=True)
	plt.plot(bins, scipy.stats.norm(mu, sigma).pdf(bins), linewidth=2, color='r')
	plt.xlim([mu - 5*sigma, mu + 5*sigma])
	plt.title("Generating Samples from Normal Distribution using Rejection Method")
	#Uncomment the below line to print the generated samples	
	print("GENERATED SAMPLES:")
	print(samples)
	

def main():
	mu = 0
	sigma = 1
	sample_functions = [rejection]
	n_samples = 1000
	print("\nTheoretical Mean and Standard Deviation")
	print("Mean: ", mu)
	print("Standard Deviation: ", sigma)
	print("No. of samples: ", n_samples)
	print("\n\n")

	for fnc in sample_functions:	
		sampling_dist(mu, sigma, n_samples, fnc)

	plt.show()

if __name__ == "__main__":
	main()
