#Dictionary to store person and their details
##Use curly brackets instead of square brackets
my_dictionary = {"name":"John","age":21,"city":"London"}
##Can access dictionary similar to list
###Using keys like indexes
print(my_dictionary["name]) #Output: John
##Can you use loops to see all values
for key in my_dictionary:
  print(key)
for value in my_dictionary.values():
  print(value)
