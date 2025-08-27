#segundo
import sqlite3
from singlenton import Singlenton

class DatabaseConnection(Singlenton):
    connection = None
    
    def __init__(self):
        if self.connection is None:
            self.connection = sqlite3.connect("users.db")
            
    def execute_query(self, query):
        
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        
    def close(self):
        self.connection.close()

db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS \
                  users(id INTEGER PRIMARY KEY, name TEXT)")
db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users(name) VALUES('Pepe')")

print(db1 is db2)
#Se puede cerra con db1 o con db2 prorque se esta hablando del mismo objeto
db2.close()