import sqlite3

connection = sqlite3.connect('fitness.db')

c = connection.cursor()

connection.commit()

connection.close()

