# class Person:
    
    
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def __str__(self):
#         return f"name={self.name}, age={self.age}, height={self.height} "
#         # String representation of the object for easy debugging 
#     def get_older(self, years):
#         self.age += years 


# class Worker(Person) :
#     def __init__(self, name, age, height, salary):
#         super(Worker, self).__init__(name, age, height)
#         self.salary = salary
#     def __str__(self):
#         text = super(Worker, self).__str__()
#         text += " salary={}" .format(self.salary)
#         return text
#     def calc_yearly_salary(self):
#         return self.salary * 12
    
# worker1 = Worker("Charlie", 28, 180, 3000)
# print(worker1)  # Calls the __str__ method from Person
# print(f"Yearly Salary: {worker1.calc_yearly_salary()}")  # Calls the method from Worker
        

#####################################ovreloading#####################################
class Vector:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector (self.x + other.x, self.y + other. y)
    def __sub__(self, other):
        return Vector (self.x - other.x, self.y - other. y)
    def __str__ (self) :
        return "X: {}, Y: {}".format(self.x, self.y)
    
v1 = Vector (2, 5)
v2 = Vector (6,3)
print (v1)
print (v2)

v3 = v1 + v2
print(v3)  # Should print the result of the addition 