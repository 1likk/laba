#1
Person=int
class Student(Person):



         2
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()




#1
car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

