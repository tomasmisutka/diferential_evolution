# imports
from enum import Enum
import math


# Enum to determine, which test function will be used
class TestFunctionType(Enum):
    FIRST_DEJONG = 1
    SECOND_DEJONG = 2
    SCHWEFFEL = 3
    RASTRING = 4


# Calculate fcost based on "TestFunctionType"
def calculate_fcost(individual, function_type):
    if (function_type == TestFunctionType.FIRST_DEJONG):
        return __first_dejong_fcost_function(individual)
    elif (function_type == TestFunctionType.SECOND_DEJONG):
        return __second_dejong_fcost_function(individual)
    elif (function_type == TestFunctionType.SCHWEFFEL):
        return __schweffel_fcost_function(individual)
    else:
        return __rastring_fcost_function(individual)


# This method calculates fcost value on vector from argument
# for 1st De Jong
def __first_dejong_fcost_function(vector):
    calculated_suitability = 0

    for x in range(len(vector)):
        calculated_suitability += vector[x]**2  # 1st DeJong test function

    return round(calculated_suitability, 5)


# This method calculates fcost value on vector from argument
# for 2nd De Jong
def __second_dejong_fcost_function(vector):
    calculated_suitability = 0

    for y in range(len(vector) - 1):
        calculated_suitability += 100 * (vector[y]**2 - vector[y + 1])**2 + (
            1 - vector[y])**2  # 2nd DeJong test function

    return calculated_suitability


# This method calculates fcost value on vector from argument
# for Schweffel
def __schweffel_fcost_function(vector):
    calculated_suitability = 0

    for z in range(len(vector)):
        calculated_suitability += -vector[z] * math.sin(
            math.sqrt(abs(vector[z])))  # Schweffel test function

    return calculated_suitability


# This method calculates fcost value on vector from argument
# for Rastring
def __rastring_fcost_function(vector):
    calculated_suitability = 0

    for a in range(len(vector)):
        calculated_suitability += vector[a]**2 - 10 * math.cos(
            2 * math.pi * vector[a])

    return (2 * len(vector)) * calculated_suitability