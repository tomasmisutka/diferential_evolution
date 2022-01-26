#imports
import numpy
from general_functions import clear_console, lines_counter, FES, NP, algorithm_name
from general_functions import generate_population, get_new_generation, calculate_mutated_vector
from general_functions import get_croossed_population, get_best_fcost_from_population
from general_functions import draw_lines_graph, calculate_individuals_fcost_from_population
from general_functions import draw_avarage_of_lines_graph
from test_functions import TestFunctionType


def differential_evolution(dimension, range_start, range_end, test_function):
    clear_console()  # clear console at start
    # get test function name
    test_function_name = TestFunctionType(test_function).name
    # / 100 because in 1 iteration are 100 fcost evaluations
    iterations = (FES * dimension) / 100

    lines_matrix = numpy.zeros((lines_counter, iterations))

    print("\n\tStarting " + algorithm_name + ", TEST function=\"" +
          test_function_name + "\", D=" + str(dimension) + "...\n")

    # fill lines matrix to create graph of 30 lines
    for current_line in range(lines_counter):

        # get initial population
        initial_population = generate_population(dimension, NP, range_start,
                                                 range_end)
        # line vector to create line
        line_vector = []

        for line_count in range(iterations):
            mutated_population = numpy.zeros((NP, dimension))
            # mutation of individuals
            for actual_individual in range(len(initial_population)):
                # from actual individual will become mutated individual
                mutated_population[
                    actual_individual] = calculate_mutated_vector(
                        actual_individual, initial_population, range_start,
                        range_end)

            # cross-over
            cross_overed_population = get_croossed_population(
                initial_population, mutated_population)
            # selection for new generation
            initial_population = get_new_generation(initial_population,
                                                    cross_overed_population,
                                                    test_function)
            # append the best fcost value from population to line
            line_vector.append(
                get_best_fcost_from_population(
                    calculate_individuals_fcost_from_population(
                        initial_population, test_function)))

        # append line to matrix of lines
        lines_matrix[current_line] = line_vector
        print("\tLine " + str(current_line + 1) + " prepared")
    # draw lines in one graph and see the statistics
    draw_lines_graph(lines_matrix.transpose(),
                     "DE | " + test_function_name + " | D=" + str(dimension),
                     True)
    # draw an avarage of the best solutions for lines matrix
    draw_avarage_of_lines_graph(lines_matrix.transpose(), test_function_name,
                                dimension)
