#Accessing elements in string and how they can be used
my_string = "Python"
my_string_2 = "Hello World!"
##First element is index 0
print(my_string[0]) #Should Output 'P'
print(my_string_2[0]) #Should Output 'H'
##Last element is index length of string - 1
print(my_string[len(my_string)-1]) #Should Output 'n'
print(my_string_2[len(my_string_2)-1]) #Should Output '!'
###You can also access last element by using minus indexes
####The last element being -1 all the way to -(n) being first element
print(my_string[-1]) #Should Output 'n'
print(my_string_2[-2]) #Should Output 'd'
