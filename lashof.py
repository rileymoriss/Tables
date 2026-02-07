from fractions import Fraction
#Fraction(value).denominator to get the denominator of a rational number
from sympy import sieve, prime, bernoulli
#all primes less than 19, [i for i in sieve.primerange(19)]
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic_2d
import numpy as np


n = 8 #The number of primes that you want.

sieve.extend_to_no(n) #Initialise the sieve to contain the primes I want
primes = [sieve[i] for i in range(2, n + 1)]

# initialise a dictionary where the keys are the elements of the list `primes`
prime_dict = dict.fromkeys(primes)
# iterate through `primes` and assign the upper bounds for the s value.
for idx, p in enumerate(primes, start=1):
	prime_dict[p] = [2*p+2*(r-1)*(p**2-p-1)-2 for r in range(1,p-1)]

#Want a list (prime, homotopy group, dim of disc)
#this tells us that \Z_p \subseteq \pi_{homotopty group} Diff D^{dim of disc}
pairs = []
for p in primes:
    for r in prime_dict[p]:
        pairs = pairs + [(p, r - s, 2*(p**2-p-2)+s) for s in range (-2*(p**2 - p - 2), r)]

print(pairs)
#Even for only the first two primes there are hundreds of pairs so we will visualise with some different methods
#in particular just listing the table with the Zp in the i,j slots would become unreadable quickly.


'''
#Scatter plot.
x_vals = [p[0] for p in pairs]
y_vals = [p[1] for p in pairs]
z_vals = [p[2] for p in pairs]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

# Plot the scatter points
# standard syntax: ax.scatter(xs, ys, zs, c=color_values)
# We use: xs=y_vals, ys=z_vals, zs=x_vals
scatter = ax.scatter(y_vals, z_vals, x_vals, c=x_vals, cmap='viridis', s=50, alpha=0.8)

# Add labels
ax.set_xlabel('Degree of the homotopy group')
ax.set_ylabel('Dimension of the disc')
ax.set_zlabel('Contains Z_p')

# Add a color bar to show the scale of x
#plt.colorbar(scatter, label='Prime p')

plt.show()
'''

#Heatmap
# Extract the plane coordinates
# We use y and z for the spatial dimensions
y_vals = [p[1] for p in pairs]
z_vals = [p[2] for p in pairs]
# The 'values' argument is required by the function signature, 
# but for a 'count' statistic, the actual values in this list are ignored.
x_vals = [p[0] for p in pairs] 

# Calculate exact range + 1 to ensure inclusive edges
y_bins = int(max(y_vals) - min(y_vals)) + 1
z_bins = int(max(z_vals) - min(z_vals)) + 1

# Calculate the 2D binned statistic
# statistic='count' counts the number of points in each bin
# bins=50 creates a 50x50 grid
stat, y_edge, z_edge, bin_number = binned_statistic_2d(
    y_vals, z_vals, values=x_vals, statistic='count', bins=100
)

# Plot the heatmap
fig, ax = plt.subplots(figsize=(8, 6))

# We use .T (transpose) because imshow expects (rows, cols), 
# effectively mapping the first dimension to the vertical axis by default.
# origin='lower' places the (0,0) index at the bottom-left corner.
im = ax.imshow(stat.T, origin='lower',
               extent=[y_edge[0], y_edge[-1], z_edge[0], z_edge[-1]],
               aspect='auto', cmap='viridis')

ax.set_xlabel('Homotopical Degree')
ax.set_ylabel('Dimension of the Disc')
ax.set_title('Heatmap of Z_p Inclusions in $\pi_i$ Diff($D^n$)')

plt.colorbar(im, label='Count')
plt.show()