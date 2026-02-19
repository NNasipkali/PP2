#1 
def square_numbers(N): 
    for i in range(1, N + 1): 
        yield i * i

N = int(input())
for value in square_numbers(N): 
    print(value)

#2 
def even_numbers(N): 
    for i in range(N+1): 
        if i % 2 == 0: 
            yield i

N = int(input())
print(", ".join(str(x) for x in even_numbers(N)))

#3 
def div_by_3_4(N): 
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0: 
            yield i
            
N = int(input())
for value in div_by_3_4(N): 
    print(value)

#4 
def squares(a, b): 
    for i in range(a, b+1): 
        yield i * i
        
a, b = map(int, input().split())
for value in squares(a, b):
    print(value)

#5 
def down(N): 
    while N >= 0:
        yield N
        N = N - 1
        
        
N = int(input())
for value in down(N): 
    print(value) 
        