def find_max(mylist):
  maximum = mylist[0]
  for number in mylist[1:]:
    if number > maximum:
      maximum = number
  return maximum

print(find_max([1,5,9,2,12,97,3,0])) #Outputs: 97
    
