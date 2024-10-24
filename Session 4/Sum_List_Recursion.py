def sum_list(mylist):
  if len(mylist) == 0:
    return 0
  return mylist[0] + sum_list(mylist[1:])
print(sum_list([1,2,3,4])) #Should output 10
