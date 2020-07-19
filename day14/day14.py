"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from scipy.stats import uniform
import matplotlib.pyplot as plt

n = 1_000_000
r = 1
random_x = uniform.rvs(loc=0, scale=r, size=n)
random_y = uniform.rvs(loc=0, scale=r, size=n)

mask = (random_x**2 + random_y**2) < r**2
circle = sum(mask)




pi = (circle*4)/n
plt.plot(random_x[~mask], random_y[~mask], 'bx', alpha=0.01)
plt.plot(random_x[mask], random_y[mask], 'rx', alpha=0.01)
plt.show()
print(pi)