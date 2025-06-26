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
        cursor.execute ("""
        SELECT * FROM people
        WHERE id = ?
        """).format(id_number)
        
        result = cursor.fetchone()
        self.id_number = id_number
        self.first_name = result[1]
        self.last_name = result[2]
        self.age = result[3]
# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()
# Create a table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY ,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

cursor.execute("""
INSERT OR IGNORE INTO people VALUES 
('1', 'John', 'Doe', 30),
('2', 'Jane', 'Smith', 25),
('3', 'Alice', 'Johnson', 28)  
""")

cursor.execute("""
SELECT * FROM people
WHERE last_name = 'Doe'
""")  # Query the database

rows = cursor.fetchall()  # Fetch all results from the executed query
print(rows)  # Print the fetched results 


connection.commit()  # Commit the changes to the database
connection.close()  # Close the connection to the database




