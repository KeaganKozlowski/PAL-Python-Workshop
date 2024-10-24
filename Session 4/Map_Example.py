#Map
##Applies a function to each element of a list
###However it doesn't return a list so you have to change it to list type
def squared(n):
  return n**2
numbers = [1,2,3,4]
squared_numbers = list(map(squared,numbers))
print(squared_numbers) #Output: 1,4,9,16
