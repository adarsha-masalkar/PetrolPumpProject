import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='PetrolPump',
    autocommit=True
)

cursor = db.cursor()

# cursor.execute('CREATE TABLE A1 (name varchar(50), value varchar(50))')

# a = input('ENTER NAME: ')
# b = 500

# cursor.execute('INSERT A1 (name, value) VALUES (%s, %s)', (a, b))

items = []

cursor.execute('SELECT * FROM Customer')
for i in cursor:
    items.append(i)

print(items)