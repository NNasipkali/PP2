#1 while loop continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
#2
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    
#3 
numbers = [3, -1, 5, -7, 8]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1

#4
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#5
i = 0

while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)



