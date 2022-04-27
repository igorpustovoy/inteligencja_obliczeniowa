import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters.plotters import plot_contour
from pyswarms.utils.plotters.formatters import Mesher
import time

grid_11x11 = [[0, 0, 9, 0, 0, 0, 0, 0, 8, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
              [0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 16],
              [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 12, 0, 8, 0, 11, 0, 3, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
              [7, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
              [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 0]]

grid_7x7 = [[0, 2, 6, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 5, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 7, 4, 0]]

grid_5x5 = [[0, 0, 3, 0, 0],
            [9, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 2, 0, 0, 2],
            [0, 0, 0, 0, 0]]

grid_3x3 = [[0, 3, 0],
            [0, 0, 0],
            [3, 0, 0]]

# Choosing a grid
grid = grid_3x3

grid_height = len(grid)
grid_width = len(grid[0])


def f(x):
    """
    x: numpy.ndarray of shape (n_particles, dimensions)
        The swarm that will perform the search

    """
    n_particles = x.shape[0]
    j = [fitness_func(x[i]) for i in range(n_particles)]
    return np.array(j)


def fitness_func(solution):
    def check_black_square_surroundings(x, y):
        penalty = 0
        if x > 0 and solution2d[x - 1][y] == 1:
            penalty += 1
        if x < grid_height - 1 and solution2d[x + 1][y] == 1:
            penalty += 1
        if y > 0 and solution2d[x][y - 1] == 1:
            penalty += 1
        if y < grid_width - 1 and solution2d[x][y + 1] == 1:
            penalty += 1
        return penalty

    def check_number(x, y):

        def check_left(x1, y1):
            white_fields = 0
            y1 -= 1  # We don't want to count the starting square multiple times
            while 0 <= y1 < grid_width and solution2d[x1][y1] == 0:
                white_fields += 1
                y1 -= 1
            return white_fields

        def check_right(x1, y1):
            white_fields = 0
            y1 += 1
            while 0 <= y1 < grid_width and solution2d[x1][y1] == 0:
                white_fields += 1
                y1 += 1
            return white_fields

        def check_up(x1, y1):
            white_fields = 0
            x1 -= 1
            while 0 <= x1 < grid_height and solution2d[x1][y1] == 0:
                white_fields += 1
                x1 -= 1
            return white_fields

        def check_down(x1, y1):
            white_fields = 0
            x1 += 1
            while 0 <= x1 < grid_height and solution2d[x1][y1] == 0:
                white_fields += 1
                x1 += 1
            return white_fields

        number = grid[x][y]
        white_fields_sum = 1  # Number square already gives us one

        directions = [check_left, check_right, check_up, check_down]
        for direction in directions:
            white_fields_sum += direction(x, y)

        return abs(number - white_fields_sum)

    # Reshaping a 1D chromosome array into a 2D one.
    solution2d = np.reshape(solution, (len(grid), len(grid[0])))

    # Check if numbered squares have correct values
    numbers_penalty = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] != 0:
                if solution2d[i][j] == 1:
                    return len(solution)  # Numbered squares must be white
                numbers_penalty += check_number(i, j)

    # Check for wrongly placed black squares
    black_squares_penalty = 0

    for i in range(0, len(solution2d)):
        for j in range(0, len(solution2d[0])):
            if solution2d[i][j] == 1:
                black_squares_penalty += check_black_square_surroundings(i, j)

    # print(numbers_penalty + black_squares_penalty)
    return numbers_penalty + black_squares_penalty


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 2, 'p': 1}

optimizer = ps.discrete.BinaryPSO(n_particles=500, dimensions=grid_height * grid_width, options=options)

start = time.time()
optimizer.optimize(f, iters=100, verbose=True)
end = time.time()
print("Algorythm ran for: ", end - start)

cost_history = optimizer.cost_history
print(min(cost_history))
plot_cost_history(cost_history)
plt.show()

# m = Mesher(func=fx.sphere)
# animation = plot_contour(pos_history=optimizer.pos_history,
#                          mesher=m,
#                          mark=(0, 0))
# animation.save('3x3_2.gif', writer='imagemagick', fps=10)

