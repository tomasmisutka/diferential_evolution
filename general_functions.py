#imports
from test_functions import calculate_fcost
import numpy, os, random, matplotlib.pyplot as plt

# functions for cosmetics purposes
clear_console = lambda: os.system("clear")
algorithm_name = "\"Differential Evolution\""

# initial setup
FES = 5000
NP = 50
F = 0.5
CR = 0.9
lines_counter = 30


# This method generating 1 individual based on following parameters:
# 1 -  dimension, 2 - range start, 3 - range end
def __generate_individual(dimension, range_start, range_end):
    individual_vector = []

    # filing logic with random values (initial)
    for x in range(dimension):
        number_from_range = round(
            random.uniform(range_start, range_end),
            5)  # last 5 is number counter after decimal point
        # append generated number to individual vector
        individual_vector.append(number_from_range)

    return individual_vector


# This method is generating population based on following parameters:
# 1 - dimension, 2 - population size, 3 - range_start, 4 - range_end
def generate_population(dimension, population_size, range_start, range_end):
    population = numpy.zeros(
        (population_size, dimension))  # M x N (50, dimension[10 or 30])

    for actual in range(population_size):
        # generate 1 individual to variable "current_individual"
        current_individual = __generate_individual(dimension, range_start,
                                                   range_end)
        # assignment of generated individual to "actual" position in matrix
        population[actual] = current_individual

    return population


# This method calculate fcost for each individual in population and return them in vector
def calculate_individuals_fcost_from_population(population, test_function):
    individuals_fcost = []

    for individual in range(len(population)):
        fcost = calculate_fcost(population[individual], test_function)
        # append calculated fcost to vector
        individuals_fcost.append(fcost)

    return individuals_fcost


# This method return the best suitability of individual from population
# "suitability" is the same obbreviation as "fcost value"
def get_best_fcost_from_population(fcost_population):
    best_suitability = fcost_population[0]  # set first suitability as the best

    for actual_suitability in range(1, len(fcost_population), 1):
        if (fcost_population[actual_suitability] <= best_suitability):
            best_suitability = fcost_population[actual_suitability]

    return best_suitability


# This method calculate mutated vector
def calculate_mutated_vector(actual_individual_index, initial_population,
                             range_start, range_end):
    random_selected_individuals = numpy.zeros((3, len(initial_population[0])))
    exit_counter = 0
    # generating 3 individuals different from actual
    while (exit_counter != 3):
        generated_index = random.randint(0, NP - 1)
        if (generated_index != actual_individual_index):
            random_selected_individuals[exit_counter] = initial_population[
                generated_index]
            exit_counter += 1  # ++ operator
    # generating 3 different individuals done

    # calculate mutated vector
    mutated_vector = numpy.zeros((1, len(initial_population[0])))

    # calculation pattern:
    # v = x1 + F * (x2 - x3)
    mutated_vector = random_selected_individuals[0] + (numpy.multiply(
        (numpy.subtract(random_selected_individuals[1],
                        random_selected_individuals[2])), F))

    __check_borders(mutated_vector, range_start, range_end)
    return mutated_vector


# This method check borders, if parameters of individual are in the scope
# used method - "PERIODIC" - modulo operator
# range_start - low border (ex. -5), range_end - high border (ex: 5)
def __check_borders(mutated_vector, range_start, range_end):
    #check each parameter, if it's in the scope
    for parameter in range(len(mutated_vector)):
        if (mutated_vector[parameter] <
                range_start):  # parameter is lower than low border
            mutated_vector[parameter] = mutated_vector[parameter] % range_start
        elif (mutated_vector[parameter] >
              range_end):  # parameter is higher than high border
            mutated_vector[parameter] = mutated_vector[parameter] % range_end


# This method crosses the parameters of individual based on generated pseudo number
def get_croossed_population(initial_population, mutated_population):
    crossed_population = numpy.zeros((NP, len(initial_population[0])))
    # starting crossover
    for x in range(len(initial_population)):
        # original individual
        initial_individual = initial_population[x]
        # mutated individual
        mutated_individual = mutated_population[x]
        # prepare vector to create new cross-overed individual
        new_individual_u = []
        # go through each parameter in individuals
        for parameter in range(len(initial_individual)):
            # generate random value in <0,1> and compare with CR
            pseudo_number = round(random.uniform(0, 1), 2)  # 2 decimal values
            # comparing pseudo_number with CR
            if (pseudo_number <= CR):  # case when CR not equals 0
                new_individual_u.append(mutated_individual[parameter])
            else:
                new_individual_u.append(initial_individual[parameter])
        # insert cross-overed individual into new generation
        crossed_population[x] = new_individual_u

    return crossed_population


# This method return new generation with selected the best individuals from initial population
# and crossed population
def get_new_generation(initial_population, cross_overed_population,
                       test_function):
    # prepare new generation
    new_generation = numpy.zeros((NP, len(initial_population[0])))
    # provide selection
    for current_selection in range(len(initial_population)):
        initial_fcost = calculate_fcost(initial_population[current_selection],
                                        test_function)
        cross_fcost = calculate_fcost(
            cross_overed_population[current_selection], test_function)
        if (cross_fcost <= initial_fcost):
            # to new generation copy individual from crossed population
            new_generation[current_selection] = cross_overed_population[
                current_selection]
        else:
            # to new generation copy individual from initial population
            new_generation[current_selection] = initial_population[
                current_selection]

    # get back new generation
    return new_generation


# This method calculate and print basic statistics from matrix
def __get_matrix_statistics(matrix):
    print("\n\tBasic matrix statistics:\n")
    print("\tMin: \t\t" + str(round(matrix.min(), 5)))
    print("\tMax: \t\t" + str(round(matrix.max(), 5)))
    print("\tMean: \t\t" + str(round(matrix.mean(), 5)))
    print("\tMedian: \t" + str(round(numpy.median(matrix), 5)))
    print("\tStd: \t\t" + str(round(matrix.std(), 5)))


# This method draw lines in 1 graph based on matrix from argument
def draw_lines_graph(matrix_of_lines, title, print_statistics):
    # print statistics for 30 lines, not for avarage of best results for lines
    if (print_statistics == True):
        __get_matrix_statistics(matrix_of_lines)
    # draw lines with title
    plt.title(title)
    plt.xlabel("Cost Function Evaluations")
    plt.ylabel("CF Best Values")
    plt.plot(matrix_of_lines)
    plt.show()


# This method draw avarage line in graph based on matrix from argument
def draw_avarage_of_lines_graph(matrix_of_lines, title, dimension):
    # calculate avarage of best results of lines in matrix
    mean_lines_matrix = __get_avarage_best_result_matrix(matrix_of_lines)
    draw_lines_graph(
        mean_lines_matrix,
        "Avarage of all results | " + title + " | D=" + str(dimension), False)


# This method return the mean matrix of each iteration
def __get_avarage_best_result_matrix(matrix):
    mean_vector_final = []

    rows, cols = matrix.shape

    for row in range(rows):
        temporary_vector = []

        for col in range(cols):
            temporary_vector.append(matrix.item((row, col)))

        mean_vector_final.append(numpy.mean(temporary_vector))

    return mean_vector_final
