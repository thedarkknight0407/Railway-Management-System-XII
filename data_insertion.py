#to deposit every data into a database

import csv
import mysql.connector as mydb
import time


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


f = open("train_details.csv", "r")

with open ('train_details.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        data = (int(i[0]), i[1], i[2], i[3], i[4], int(i[5]), i[6], i[7], i[8], i[9])
        query = f"insert into train_data values{data}"
        cursor.execute(query)
        conn.commit()

print("Data inserted successfully!")
conn.commit()
conn.close()