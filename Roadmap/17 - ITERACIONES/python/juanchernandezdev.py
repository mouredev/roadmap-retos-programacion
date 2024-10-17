### Python Iteration ###

#! for loop
for num in range(1, 11):
  print(num)

#! while loop
num = 1

while num <= 10:
  print(num)
  num += 1
  
#! recursion
def num_printer(num = 1):
  if num > 10:
    return
  
  print(num)
  num_printer(num + 1)

num_printer()
