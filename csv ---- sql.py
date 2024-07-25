'''
pandaslib usage 

csv ----> sql database
'''

import mysql.connector as mydb
import user

def db_create():
    #tabel creation
    connection : bool = False
    conn = mydb.connect(
        host = "localhost",
        user = "root",
        password = "12345"
    )
    if conn.is_connected():
        cursor = conn.cursor()
        connection = True

    #database creation
    cursor.execute("CREATE database if not exists railway_management")
    conn.close()

def table_users():
    connection : bool = False
    conn = mydb.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database = "railway_management"
    )

    if conn.is_connected():
        cursor = conn.cursor()
        connection = True
    else:
        print("Error in connecting to server!")

    try:
        cursor.execute('''CREATE TABLE users (uid int UNIQUE auto_increment,last_name varchar(50),first_name varchar(50) NOT NULL,sex char(1) NOT NULL,email varchar(50) UNIQUE,contact bigint UNIQUE,PRIMARY KEY (uid))''')
        cursor.close()
        conn.close()
    except:
        pass

db_create()
table_users()


print("Initiate User")

user.user()