class Person:
    amount = 0  # Class variable to keep track of the number of Person instances
    
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    def __del__(self):
    #     print(f"Deleting {self.name}")
        Person.amount -= 1 
        # Destructor to decrement the class variable when an instance is deleted 
        # Destructor to handle cleanup when the object is deleted
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, height={self.height})"
        # String representation of the object for easy debugging 
    def get_older(self ,years):
        self.age += years
        # Method to get the age after a certain number of years
# Default values for name and age
        
person1 = Person("Alice", 30, 165)
person2= Person("Bob", 25, 175)
print(f"Name: {person1.name}, Age: {person1.age}, Height: {person1.height}") 
 
print(person1)  # Calls the __str__ method

print(f"Total number of Person instances: {Person.amount}")  # Accessing class variable
del(person2)  
print(Person.amount )  # Accessing class variable after deletion



