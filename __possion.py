

import numpy as np
from scipy.stats import poisson 
import matplotlib.pyplot as plt

mu = 1.3
input = range(1, 1000)
normalized = [x / 1000 for x in input]
x = np.arange(0.01, 1, 0.01)
fig, ax = plt.subplots(1, 1)
ax.plot(x, poisson.ppf(x, mu), 'bo', ms=8, label='poisson pmf')
plt.show()
