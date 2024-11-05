#Declaring nested list
##Two ways
###For loop
my_list = [[] for _ in range(3)]
print(my_list) #Output: [[None],[None],[None]]
###Multiplication operation
####Creating 5 inners lists which contain None elements
my_list2 = [[None]]*3
print(my_list2) #Output: [[None],[None],[None]]
#There is a problem though, what is it?
