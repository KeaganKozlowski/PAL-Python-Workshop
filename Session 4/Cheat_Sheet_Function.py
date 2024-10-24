#RECURSION:
def recursive_function(parameters):
    if base_case_condition:
        return base_case_value
    else:
        return recursive_function(modified_parameters)

#Example: Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

#ADVANCED LIST FUNCTIONS:
#map() - Apply a function to each item in a list
map(function, iterable)
#Example: Squaring each number
numbers = [1, 2, 3]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9]

#filter() - Filter items based on a condition
filter(function, iterable)
#Example: Filter even numbers
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

#List Comprehensions:
#[expression for item in iterable]
#Example: Create a list of squares
squares = [x**2 for x in range(1, 5)]  # [1, 4, 9, 16]
#Add a condition
evens = [x for x in range(1, 10) if x % 2 == 0]  # [2, 4, 6, 8]

#Lambda functions - Anonymous functions (used in map/filter)
lambda arguments: expression
#Example: Add two numbers
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
