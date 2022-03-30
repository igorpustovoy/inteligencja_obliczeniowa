import pygad
import math
import time

labirynth = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
             [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
             [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
             [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
             ]

#definiujemy parametry chromosomu
gene_space = [0, 1, 2, 3]

def fitness_func(solution, solution_idx):
    current_position = [1, 1]
    finish_position = [10, 10]
    for direction in solution:
        if direction == 0 and labirynth[current_position[0] - 1][current_position[1]] != 1:
            current_position = [current_position[0] - 1, current_position[1]]
        if direction == 1 and labirynth[current_position[0]][current_position[1] + 1] != 1:
            current_position = [current_position[0], current_position[1] + 1]
        if direction == 2 and labirynth[current_position[0] + 1][current_position[1]] != 1:
            current_position = [current_position[0] + 1, current_position[1]]
        if direction == 3 and labirynth[current_position[0]][current_position[1] - 1] != 1:
            current_position = [current_position[0], current_position[1] - 1]

    distance = math.sqrt((finish_position[0] - current_position[0]) ** 2 + (finish_position[1] - current_position[1]) ** 2)
    return -distance

fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 200
num_genes = 30

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 100
num_generations = 100
keep_parents = 10

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 4

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
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

#uruchomienie algorytmu
start = time.time()
ga_instance.run()
end = time.time()
print("Algorythm ran for: ", end - start)

times = [0.0989992618560791, 0.14099836349487305, 0.17300057411193848, 0.18200016021728516, 0.10799932479858398,
         0.1470189094543457, 0.10000014305114746, 0.1640026569366455, 0.1900038719177246, 0.14800047874450684]

time_sum = 0
for time in times:
    time_sum += time

print("Average algorythm execution time after 10 runs: ", time_sum / 10)

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))


#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()