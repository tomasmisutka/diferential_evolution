# Evolution algorithm ( Differential Evolution - DE ) - 4 test functions
# Mutation strategy: rand 1
# Control borders by function: Periodic
# Crossover - Bionominal
# Author: Tomas Misutka
# PYTHON version required: 3.8.9 or newer

#imports
from test_functions import TestFunctionType
from general_functions import algorithm_name
from differential_evolution import differential_evolution

# 1 - 1st De Jong
# 2 - 2nd De Jong
# 3 - Schweffel
# 4 - Rastring

# --------------------------------------------------------------------------------------------
# FIRST DE JONG (1st)

differential_evolution(10, -5, 5, TestFunctionType.FIRST_DEJONG)

differential_evolution(30, -5, 5, TestFunctionType.FIRST_DEJONG)

# --------------------------------------------------------------------------------------------
# SECOND DE JONG (2nd)

differential_evolution(10, -5, 5, TestFunctionType.SECOND_DEJONG)

differential_evolution(30, -5, 5, TestFunctionType.SECOND_DEJONG)

# --------------------------------------------------------------------------------------------
# SCHWEFFEL

differential_evolution(10, -500, 500, TestFunctionType.SCHWEFFEL)

differential_evolution(30, -500, 500, TestFunctionType.SCHWEFFEL)

# --------------------------------------------------------------------------------------------
# RASTRING

differential_evolution(10, -5, 5, TestFunctionType.RASTRING)

differential_evolution(30, -5, 5, TestFunctionType.RASTRING)

# --------------------------------------------------------------------------------------------

print("\nTHE END of " + algorithm_name)

# --------------------------------------------------------------------------------------------