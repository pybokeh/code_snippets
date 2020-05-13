
class Employee:

    # Class variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):   # First argument of a class method is 'cls' by convention
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):      # Static methods just have no 'self' or 'cls' as first argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

##############  Another Example from dbader  ##############
# https://www.youtube.com/watch?v=PNpt7cFjGsM

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def __repr__(self):
        return f'Pizza({self.ingredients})'
        
Pizza(['cheese', 'tomatoes'])
Pizza(['cheese', 'tomatoes', 'ham'])
Pizza(['cheese', 'tomatoes', 'ham', 'mushrooms']

# From above, we're making different pizzas, but how do we make or
# instantiate different pizzas?  answer: class method as "factory" function

# Class with class method
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def __repr__(self):
        return f'Pizza({self.ingredients})'
        
    @classmethod
    def margherita(cls):
        return cls('cheese', 'tomatoes'])
        
    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', ,'mushrooms'])
        
Pizza.margherita()  # returns Pizza(['cheese', 'tomatoes'])
Pizza.prosciutto() # returns Pizza(['cheese', 'tomatoes', 'ham', 'mushrooms'])

# Class with static method
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius
        
    def __repr__(self):
        return f'Pizza({self.ingredients})'
        
    def area(self):
        return self._circle_area(self.radius)
        
    @staticmethod  # acting as a "helper" function
    def _circle_area(r):
        return r ** 2 * math.pi
        
Pizza(4.5, ['cheese']).area()  # returns 63.617...
Pizza._circle_area(12)  # returns 452.3893...

#### Summary ####
Instance Method:
    - By convention, uses "self" as first argument
    - Can modify object instance state
    - Can modify class state
    
Class Method:
    - By conventions, uses "cls" as first argument
    - Can't modify object instance state
    - Can modify class state
    
Static Method:
    - Does not use "self" or "cls" as first argument
    - Can't modify object instance state
    - Can't modify class state

