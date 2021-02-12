### ``` Problem Statement```

Take a list containing all values between 1 and a positive integer ’N’. For all
possible permutations of this list, compute the number of runs. Runs, here, are
defined as the number of continuously increasing or decreasing sub lists in each
and every permutation. Find the distribution based on the frequency of number
of runs.

For Example: If N = 3

Possible Lists:[{1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}]

For (i): 1 - Only 1 sub-list and that is increasing

For (ii): 2 - 1,3 is increasing and 3,2 is decreasing

For (iii): 2 - 2,1 is decreasing and 1,3 is increasing

For (iv): 2 - 2,3 is increasing and 3,1 is decreasing

For (v): 2 - 3,1 is decreasing and 1,2 is increasing

For (vi): 1 - Only 1 sub-list and that is decreasing

Therefore, the frequency of 1 is 2 and the frequency of 2 is 4 or {1:2, 2:6}
