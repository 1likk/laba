#1. Generator for squares of numbers up to N:
def squares_generator(N):
    for i in range(N):
        yield i**2


N = 10
squares = squares_generator(N)
for square in squares:
    print(square)

#2. Program using generator to print even numbers between 0 and n:

def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


n = int(input("Введите число: "))

even_gen = even_numbers(n)
print(','.join(map(str, even_gen)))

#3. Function with a generator to iterate numbers divisible by 3 and 4 between 0 and n:

def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter a number: "))

divisible_gen = divisible_by_3_and_4(n)
for num in divisible_gen:
    print(num)

#4. Generator called squares to yield the square of all numbers from (a) to (b):
def squares(a, b):
    for i in range(a, b+1):
        yield i**2


a = 3
b = 7
for square in squares(a, b):
    print(square)

#5. Generator that returns all numbers from (n) down to 0:
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = 5
for number in countdown(n):
    print(number)
