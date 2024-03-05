import math
#1 Write a Python program to convert degree to radian.
degree=(float(input("Введите градус: " )))
radian=math.radians(degree)
print("Ваш градус в радиане: " + str(radian))

#2 Write a Python program to calculate the area of a trapezoid.
def trapezoid_area(a, b, h):
    area = 0.5 * (a+b) * h
    return area

a=float(input("Введите сторону a: "))
b=float(input("Введите сторону b: "))
h=float(input("Введите высоту h: "))

area=trapezoid_area(a,b,h)

print(area)


#3 Write a Python program to calculate the area of regular polygon.
def calculate_area_of_regular_polygon(n, s):
    if n < 3:
        return "Число сторон должен быть больше 3."
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area


n = int(input("Введите число сторон: "))
s = float(input("Введите длину сторон: "))

area= calculate_area_of_regular_polygon(n,s)
print(int(area))


#4 Write a Python program to calculate the area of a parallelogram.
def calculate_area_of_parallelogram(b, h):
    area=(b*h)
    return area

b=float(input("Введите длину сторон: "))
h=float(input("Введите высоту: "))

area=calculate_area_of_parallelogram(b,h)
print(area)