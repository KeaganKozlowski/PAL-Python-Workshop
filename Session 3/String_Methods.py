#There are several helpful functions in Python which can help with strings
my_string = "Python"
my_string_2 = "     Python is great    "
##Making every character in string lowercase, not changing if already lowercase
print(my_string.lower()) #Should Output "python"
##Making every character in string uppercase, not changing if already uppercase
print(my_string.upper()) #Should Output "PYTHON"
##Removing trailing and leading whitespace
print(my_string_2.strip()) # Should Output "Python is great"
##Replace elements in string, can specify how many you want to replace
new_1 = my_string_2.strip().replace("t","y",1) 
print(new_1) #Should Output "Pyyhon is great"
##Converting a string into a list by a default or predefined seperator
###Default seperator is just one space or one whitespace
print(my_string_2.strip().split()) #Should Output ["Python","is","great"]
