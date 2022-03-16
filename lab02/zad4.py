import pygad
import numpy

S = [
{
         "przedmiot": "zegar",
         "wartość": 100,
         "waga": 7
        },
{
         "przedmiot": "obraz-pejzaż",
         "wartość": 300,
         "waga": 7
        },
{
         "przedmiot": "obraz-portret",
         "wartość": 200,
         "waga": 6
        },
{
         "przedmiot": "radio",
         "wartość": 40,
         "waga": 2
        },
{
         "przedmiot": "laptop",
         "wartość": 500,
         "waga": 5
        },
{
         "przedmiot": "lampka nocna",
         "wartość": 70,
         "waga": 6
        },
{
         "przedmiot": "srebrne sztućce",
         "wartość": 100,
         "waga": 1
        },
{
         "przedmiot": "porcelana",
         "wartość": 250,
         "waga": 3
        },
{
         "przedmiot": "figura z brązu",
         "wartość": 300,
         "waga": 10
        },
{
         "przedmiot": "skórzana torebka",
         "wartość": 280,
         "waga": 3
        },
{
         "przedmiot": "odkurzacz",
         "wartość": 300,
         "waga": 15
        },
]


#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcjÄ fitness
def fitness_func(solution, solution_idx):
    sum_weight = 0
    for i in range(0, len(S)):
        if solution[i] == 1:
            sum_weight += S[i]['waga']
    if sum_weight > 25:
        return 0
    else:
        sum_worth = 0
        for i in range(0, len(S)):
            if solution[i] == 1:
                sum_worth += S[i]['wartość']
        return sum_worth


fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 10

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
                       mutation_percent_genes=mutation_percent_genes)

#uruchomienie algorytmu
ga_instance.run()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
prediction = 0
for i in range(0, len(S)):
    if solution[i] == 1:
        prediction += S[i]['wartość']

print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()