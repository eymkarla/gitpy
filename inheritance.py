class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, year):
        Person.__init__(self,first, last)
        self.year = year

    def GetEmployee(self):
        return self.Name() + ", " +  self.year

x = Person("Kim", "Namjoon")
y = Employee("Kim", "Taehyung", "1995")

print(x.Name())
print(y.GetEmployee())

#Overriding and overloading
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, year):
        super().__init__(first, last)
        self.year = year


x = Person("Jungkook", "Jeon")
y = Employee("Rap", "Mon", "1994")

print(x)
print(y)