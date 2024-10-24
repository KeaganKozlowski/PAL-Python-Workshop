def reverse_string(mystring):
  if len(mystring) == 0:
    return mystring
  #String concatenation
  return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello")) #Output "olleh"
