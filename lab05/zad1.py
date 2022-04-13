import math
import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt



def endurance(params):
    x, y, z, u, v, w = params
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


def f(x):
    """
    x: numpy.ndarray of shape (n_particles, dimensions)
        The swarm that will perform the search

    """
    n_particles = x.shape[0]
    j = [-endurance(x[i]) for i in range(n_particles)]
    return np.array(j)


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

# c
# x_max = [2, 2]
# x_min = [1, 1]
# my_bounds = (x_min, x_max)
# Optimization finished | best cost: 2.0282442667053933, best pos: [1.01288672 1.00115171]

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)


optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=my_bounds)
stats = optimizer.optimize(f, iters=1000)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
print(stats)
plt.show()


