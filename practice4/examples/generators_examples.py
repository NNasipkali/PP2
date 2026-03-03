# Example 1: Using iter() and next()

numbers = [10, 20, 30]

my_iter = iter(numbers)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Example 2: Custom iterator

class CountToThree:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 3:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

obj = CountToThree()

for x in obj:
    print(x)
    
# Example 3: Generator function

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for number in even_numbers(10):
    print(number)