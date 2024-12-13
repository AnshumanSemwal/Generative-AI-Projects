import sqlite3

# Connect to sqlite
connection= sqlite3.connect("student.db")

# Create curson: object to insert record, create table and retrieve data
cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert record

cursor.execute('''Insert Into STUDENT values('Abc','DS','A',90)''')
cursor.execute('''Insert Into STUDENT values('Bcd','AI','B',20)''')
cursor.execute('''Insert Into STUDENT values('Cde','DS','A',25)''')
cursor.execute('''Insert Into STUDENT values('Def','CS','A',70)''')
cursor.execute('''Insert Into STUDENT values('Efg','ME','A',70)''')

print("Records")

data=cursor.execute('''Select * from STUDENT ''')

for row in data:
    print(row)

# Remember to close the connection
connection.commit()
connection.close()