def factorial_loop(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result = result * i
    return result
#Use
print(factorial_loop(5)) #Should output 120  
