'''
pandaslib usage 

csv ----> sql database
'''

import pandas as pd
import mysql.connector as mydb
from sqlalchemy import create_engine, types
from test import test4

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
        cursor.execute('''CREATE TABLE users (uid int UNIQUE auto_increment,last_name varchar(50),first_name varchar(50) NOT NULL,sex char(1) NOT NULL,email varchar(50) UNIQUE,contact int UNIQUE,PRIMARY KEY (uid))''')
        cursor.close()
        conn.close()
    except:
        pass

db_create()
table_users()

try:
    engine = create_engine('mysql://root:12345@localhost/railway_management')
    csvf = pd.read_csv("train_details.csv")
    print("creating train data")
    csvf.to_sql("train_data", con = engine, index=False)
    print("creating train data completed!")
except:
    pass
    print("initiate user")
test4.user()