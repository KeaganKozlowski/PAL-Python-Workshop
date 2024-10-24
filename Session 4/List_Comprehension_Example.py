#List Comprehensions
numbers = [1,2,3,4,5,6]
##Without defining a function create a list of square numbers
squared_numbers = [x**2 for x in numbers]
print(squared_numbers(numbers)) #Output: [1,4,9,16,25,36]

##Without defining a function create a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers(numbers)) #Output: [2,4,6]
