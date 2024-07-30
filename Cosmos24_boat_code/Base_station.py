#Author Adam Hawks, Mike Tritchler
# parse data from boat and write to database
import numpy as np
import pandas as pd
import time
import sqlalchemy as sql 
import pyodbc
import serial
import sqlite3
import keyboard
import sys
x = 0
y = 0
database = sqlite3.connect("Cosmos24.db")
radio = serial.Serial('COM16', 57600, timeout = 10)
#radio = serial.Serial('COM20', 9600, timeout = 10)
def write_data_to_database(data, database):
    '''Parses the raw data and writes it to the database.

    :param list List of data values
    :param ~sqlite3.Connection database Connection to the sqlite database
    '''
    # Create a cursor to connect to the database
    cur = database.cursor()
    # Insert the gps data
    cur.execute("INSERT or IGNORE INTO GPS(boat_id,timestamp,lat,lon) VALUES (?, ?, ?, ?)", (data[0], data[1], data[2], data[3]))
    gps_id = cur.lastrowid
     #insert into boats data
    cur.execute("INSERT or IGNORE INTO boats(id,boat_id) VALUES (?,?)", (gps_id, data[0]))
    # Insert the temperature data
    cur.execute("INSERT or IGNORE INTO temperature(degree,id) VALUES (?, ?)", (data[4], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO ph(level,id) VALUES (?, ?)", (data[5], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO tds(ppm,id) VALUES (?, ?)", (data[6], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO do(percent,id) VALUES (?, ?)", (data[7], gps_id))
    # Insert the ph data
    #cur.execute("INSERT or IGNORE INTO turbidity(ntu,gps_id) VALUES (?, ?)", (data[8], gps_id))
    # Insert the ph data
    #cur.execute("INSERT or IGNORE INTO orp(mvolts,gps_id) VALUES (?, ?)", (data[9], gps_id))
    database.commit()
while x==0: 
    if keyboard.is_pressed("enter"): 
        x=1
        print("starting database entries")
        data_byte = radio.readline()
        data = data_byte.decode("utf-8")
        data = data.split(",")
        data[0] = data[0].strip("b'")
        n = data[1]
        c = n[-1]
while not keyboard.is_pressed("q"):
    data_byte = radio.readline()
    data = data_byte.decode("utf-8")
    data = data.split(",")
    data[0] = data[0].strip("b'")
    n = data[1]
    if data != "" and c != n[-1]:
        write_data_to_database(data, database)
        print("data line written")
        n = data[1]
        c = n[-1]
    