# Create a class Person
#
# Requirements:

# Constructor to set age
#
# Getter method get_age() to return age
#
# Setter method set_age()
#
# Age must be greater than 0

# Private variable __age
#
class Person:
    def __init__(self,age):
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age>0:
            self.__age = new_age
        else:
            print('Input Valid age')
a = Person(5)
print(a.get_age())
a.set_age(43)
print(a.get_age())

# Create a class Employee
#
# Requirements:
#
# Private variable __salary
#
# Getter using @property
#
# Setter:
#
# Salary cannot be negative
#
# Method increase_salary(percent)
#
# Example: 10% increase

class Employee:
    def __init__(self,salary):
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary<0:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary
    def increase_salary(self,percent):
        self.__salary+=self.__salary*(percent/100)

    def display(self):
        print(self.salary)
a = Employee(340)
a.display()
a.increase_salary(10)
a.display()



