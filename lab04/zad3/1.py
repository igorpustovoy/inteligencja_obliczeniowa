import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

# Set-up hyperparameters
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

# Call instance of GlobalBestPSO
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
                                    options=options)

# Perform optimization
stats = optimizer.optimize(fx.eggholder, iters=100)

# Obtain cost history from optimizer instance
cost_history = optimizer.cost_history

# Plot!
plot_cost_history(cost_history)
print(cost_history)
print(stats)

for i in range(0, len(cost_history)):
    if cost_history[i] == stats[0]:
        print("Wykres przyjął minimum podczas: ", i, " iteracji.")
        break

plt.show()