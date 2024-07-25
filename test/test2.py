#to deposit every data into a database

import csv
import mysql.connector as mydb
import time

f = open("train_details.csv", "r")
reader = csv.reader(f)

#Setting up sql
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

try:
    cursor.execute("use trains_schedule")
except:
    cursor.execute("CREATE database if not exists trains_schedule")
    cursor.execute("use trains_schedule")

    #table creation
    cursor.execute('''Create table train_data (
                   train_no int,
                   station_code varchar(5),
                   station_name varchar(255),
                   arrival_time time,
                   departure_time time,
                   distance int,
                   source_station varchar(5),
                   source_station_name varchar(50),
                   destination_station varchar(5),
                   destination_station_name varchar(50))''')


with open ('train_details.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader) 
    query = 'insert into MyTable values ({0})'
    query = query.format(','.join('?' * len(columns)))
    cursor = conn.cursor()
    for data in reader:
        cursor.execute(query, data)
    cursor.commit()
conn.commit()
conn.close()