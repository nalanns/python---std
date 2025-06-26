import sqlite3

class Person:
    def __init__(self, id_number, first_name, last_name, age):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
        

        
    def load_person(self, id_number):
        self.cursor.execute ("""
        SELECT * FROM people
        WHERE id = {}
        """).format(id_number)
        
        result = self.cursor.fetchone()
        self.id_number = id_number
        self.first_name = result[1]
        self.last_name = result[2]
        self.age = result[3]
    
    
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO people VALUES (?, ?, ?, ?)
        """, (self.id_number, self.first_name, self.last_name, self.age))
        self.connection.commit()
        self.connection.close()


        
p1 = Person(7, 'Alex', 'Robinson', 28)
p1.insert_person()  # Insert the new person into the database
        
connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM people")  # Query the database
results = cursor.fetchall()  # Fetch all results from the executed query
print(results)  # Print the fetched results

connection.close()  # Close the connection to the database 


        
        
        
        