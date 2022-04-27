import pygad
import time
import numpy as np

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
grid = grid_7x7

gene_space = [0, 1]

grid_height = len(grid)
grid_width = len(grid[0])


def fitness_function(solution, solution_idx):
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
                    return -len(solution)  # Numbered squares must be white
                numbers_penalty += check_number(i, j)

    # Check for wrongly placed black squares
    black_squares_penalty = 0

    for i in range(0, len(solution2d)):
        for j in range(0, len(solution2d[0])):
            if solution2d[i][j] == 1:
                black_squares_penalty += check_black_square_surroundings(i, j)

    return -(numbers_penalty + black_squares_penalty)


sol_per_pop = 600
num_genes = len(grid) * len(grid[0])

num_parents_mating = 300
num_generations = 800
keep_parents = 15

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 130 / (len(grid) * len(grid[0]))

times = []

limit = 50
for i in range(0, limit):
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           stop_criteria=["reach_0"])

    start = time.time()
    ga_instance.run()
    end = time.time()
    print("Algorythm ran for: ", end - start)
    times.append(end - start)

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    solution2D = np.reshape(solution, (len(grid), len(grid[0])))
    # print("Parameters of the best solution :\n {solution}".format(solution=solution2D))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

time_sum = 0
correct_guesses = 0
for time in times:
    if solution_fitness == 0:
        correct_guesses += 1
        time_sum += time

print(f"Average algorythm execution time after {correct_guesses}/{limit} correct guesses: ", time_sum / correct_guesses)
# ga_instance.plot_fitness()
# 3x3	0.06286500692367554	0.06770203828811645
# 5x5	3.5706164240837097	0.8856637454032898
# Average algorythm execution time after 40/100 correct guesses:  23.11241764068603 reszta około 105 sekund
