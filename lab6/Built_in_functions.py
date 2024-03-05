#1
l = [1, 2, 3, 4, 5]

print(eval('*'.join(str(x) for x in l)))

#1.2
product=1
def f(a):
    global product
    product *= a
    return a

l = [1, 2, 3, 4, 5]

list(map(f, l))

print(product)

#2
s = input()

upperCase, lowerCase = 0, 0
for i in s:
    if i.isupper():
        upperCase += 1
    if i.islower():
        lowerCase += 1

print(f"Upper Case letters: {upperCase}\nLower Case letters: {lowerCase}")

#3
s = input("Check if string is palindrome:")

s_reversed = reversed(s)

if list(s) == list(s_reversed):
    print(s + " is palindrome")
else:
    print(s + " is not palindrome")

#4
from time import sleep
from math import sqrt

def sqrt_after_milliseconds(num, time_ms):
    sleep(time_ms / (10 ** 3))
    print(f"Square root of {num} after {time_ms} miliseconds is {sqrt(num)}")

sqrt_after_milliseconds(int(input()), int(input()))

#5
myTuple = (0, 1, 2, 3, 4, 5)

if all(myTuple):
    print(True)
else:
    print(False)



