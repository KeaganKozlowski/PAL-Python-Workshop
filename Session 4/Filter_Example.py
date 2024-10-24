#Filter
##Only select elements if they match a condition
def even(n):
  return n % 2 == 0
numbers = [1,2,3,4,5]
even_numbers = list(filter(even, numbers))
print(even_numbers) #Outpit: [2,4]
