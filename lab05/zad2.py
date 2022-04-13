import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]


def f(x):
    """
    x: numpy.ndarray of shape (n_particles, dimensions)
        The swarm that will perform the search

    """
    n_particles = x.shape[0]
    j = [fitness_func(x[i]) for i in range(n_particles)]
    return np.array(j)


def fitness_func(solution):
    sum1 = np.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = np.sum(solution_invert * S)
    fitness = np.abs(sum1 - sum2)
    return fitness


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 2, 'p': 1}

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)

optimizer = ps.discrete.BinaryPSO(n_particles=10, dimensions=15, options=options)
optimizer.optimize(f, iters=30, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()
