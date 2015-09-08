import pdb

class Employee(object):
    def __init__(self, name = '', age = 1):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'name: %s age: %s' % (self.name,str(self.age))
        
    def __lt__(self,other):
        return self.age < other.age


Tom = Employee('Tom',20)
John = Employee('John',23)
Jack = Employee('Jack',18)

l = [Tom,John,Jack]

l.sort()

print l
