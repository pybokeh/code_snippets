
class Employee:

    raise_amount = 1.04   # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # first, last, email, and pay are instance variables: HINT is the "self" word

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
       #self.pay = int(self.pay * Employee.raise_amount) would do the same,
       #but would change the Employee's class raise amount, instead of the instance's raise amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# To get "name space" of class instances: print(emp_1.__dict__)
