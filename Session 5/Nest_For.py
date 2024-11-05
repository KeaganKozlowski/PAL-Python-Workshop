my_sentence = "welcome to the party mr presdient"
my_list = my_sentence.split(" ")
#Basic for range loop
for i in range(0,11):
  print(i) #Output 0->10
#Basic for each loop
for word in my_list:
  print(word) #Output the words in my_sentence
#Nested for range loop
##Note when using range second limit will go limit - 1 
##This is for lists where index start at 0
for i in range(1,11):
  for j in range(1,6):
    print("First loop:"str(i)+" Second loop:"+str(j))
    #Output i (1->10) and j (1->5)
#Nested for each loop
for word in my_list:
  for character in word:
    print(character) #Output every character
