#One Dimensional list
my_list = [1,2,3,4,5,6]
#Two Dimensional list
my_list2 = [[1,2],[3,4],[5,6]]
#Accessing specific element
outer_list = [[elephant,mouse],[watermelon,grape],[tanker,kayak]]
##Accesing first list element
inner_list = outer_list[0]
print(inner_list) #Output: [elephant,mouse]
##Accessing first element inner list
first_element = inner_list[0]
print(first_element) #Output: elephant
##Piecing the two part together
first = outer_list[0][0]
print(first) #Output: elephant

#Iterating through a nested list
for inner in range(len(outer_list)):
  for element in range(len(outer_list[inner])):
    print(outer_list[inner][element])
