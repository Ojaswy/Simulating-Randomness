# ```Simulating Random Numbers```

This README file contains the graphs and plots of the above code files

## Generating Random Numbers

#### Plotting the RSS values of various distributions to find out the best one
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Best%20Fit/m2b.png?raw=true)

#### Plotting the empirical distribution against theoretical distribution
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Best%20Fit/m2a.png?raw=true)

### Using Acceptance-Rejection Method to draw samples
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Acceptance-Rejection%20Method/normal2.png?raw=true)

### Using Table-Lookup Method to draw samples
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Various%20Generators/generated_sample.png?raw=true)

## Multivariate Normal Distribution
On simulating X a multivariate normal distribution with following mean vector and variance covariance matrix.
μ = [20,30,50,35,15], Σ = [[174, 134, 83, 98, 80],[134, 202, 76, 150, 141],[83, 76, 60, 53, 40], [98, 150, 53, 127, 114], [80, 141, 40, 114, 112]]

Generated 100 random numbers and plotted these:

KDE plot, described as Kernel Density Estimate is used for visualizing the Probability Density of a continuous variable. This shows that the generated sample does indeed follow Multivariate Normal Distribution.
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Multivariate%20Normal%20Distribution/kde.png?raw=true)

The Hexbin plot is  used to depict the probability density at different values in a continuous variable. 
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Multivariate%20Normal%20Distribution/hex.png?raw=true)


From the scatter plot it is clear that the data has outliers. I have filtered those outliers and have plotted the Linear Regression Graph. The Linear Regression has a good fit considering this was done on only 100 samples.
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Multivariate%20Normal%20Distribution/scatter.png?raw=true)
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Multivariate%20Normal%20Distribution/regress.png?raw=true)


The residual plot graph that shows the residuals on the vertical axis and the independent variable on the horizontal axis. If the points in a residual plot are randomly dispersed around the horizontal axis, a linear regression model is appropriate for the data; otherwise, a nonlinear model is more appropriate. Since as seen in the Residual Plot the points are actually randomly disperesed, it confirms that the linear regression is appropriate and has a good fit.
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Random%20Numbers%20Generation/Multivariate%20Normal%20Distribution/residual.png?raw=true)

## Simulating COVID-19 using SIR model

Italy:
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/SIR_model/Italy.png?raw=true)

Japan:
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/SIR_model/Japan.png?raw=true)

USA:
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/SIR_model/US.png?raw=true)

## Simulating Supermarkets based on actual data

Basic Analysis

![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Supermarket%20Simulation/1.png?raw=true)
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Supermarket%20Simulation/2.png?raw=true)
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Supermarket%20Simulation/3.png?raw=true)

Calculating Transition Probabilitites by MCMC
![](https://github.com/Ojaswy/Simulation-and-Modelling/blob/main/Supermarket%20Simulation/transition.png?raw=true)


