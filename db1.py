import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='PetrolPump',
    autocommit=True
)

cursor = db.cursor()

# cursor.execute('CREATE TABLE Customer ('
#                'account_no varchar(50),'
#                'party_name varchar(500),'
#                'address varchar(50),'
#                'telephone_no varchar(50),'
#                'deposit_amount varchar(50),'
#                'gst_no varchar(50),'
#                'bill_charges varchar(50)'
#                ')')
# db.commit()


cursor.execute('SELECT * FROM Customer')
for i in cursor:
    print(i)
