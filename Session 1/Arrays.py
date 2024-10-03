#Syntax
list_name = [item1, item2, item3]
##Example
fruits = ["apple","cherry","banana","tomato","plum"]
###Operations
####Access
print(fruits[0]) #Will output "apple"
####Append
fruits.append("orange")
print(fruits) #Will output fruits with addition of orange coming after plum
####Remove
fruits.remove("banana")
print(fruits) #Will output fruits without banana
#####Pop
fruits.pop(0)
print(fruits) #Will output fruits without apple
###Loop through list
for fruit in fruits:
  print(fruit) #Will output each fruit singulary
