import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

my_cursor = db.cursor()

# Create database
# my_cursor.execute(
#     "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# View setup of database
# my_cursor.execute("DESCRIBE Person")

# for x in my_cursor:
#     print(x)

# # Insert into databse
# my_cursor.execute(
#     "INSERT INTO Person (name, age) VALUES (%s, %s)", ("joe", 22))
# db.commit()  # Commit changes

# View contents of database
my_cursor.execute("SELECT * FROM Person")
for x in my_cursor:
    print(x)
