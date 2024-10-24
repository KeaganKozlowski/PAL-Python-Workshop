def factorial_recursive(n):
  if n < 0:
    raise ValueError("No work negative numbers")
  elif n == 0:
    return 1
  else:
    return n * factorial_recursive(n - 1)
#Use
print(factorial_recursive(5)) #Should output 120
