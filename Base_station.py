#Author Adam Hawks, Mike Tritchler
# parse data from boat and write to database

#import libraries
import time
import pyodbc
import serial
import sqlite3
import keyboard
import sys
# initialise loop sentinels
x = 0
y = 0
data = ''
#open database connection
database = sqlite3.connect("Cosmos24.db")
# open serial port connection
radio = serial.Serial('COM16', baudrate = 57600)
#radio = serial.Serial('COM20', 9600)
# function to write data to database (written mostly by Mike)
def write_data_to_database(data, database):
    '''Parses the raw data and writes it to the database.

    :param list List of data values
    :param ~sqlite3.Connection database Connection to the sqlite database
    '''
    # Create a cursor to connect to the database
    cur = database.cursor()
    # Insert the gps data
    cur.execute("INSERT or IGNORE INTO GPS(boat_id,timestamp,lat,lon) VALUES (?, ?, ?, ?)", (data[0], data[1] + '' +data[2], data[3], data[4]))
    gps_id = cur.lastrowid
     #insert into boats data (don't think this works)
    #cur.execute("INSERT or IGNORE INTO boats(id,boat_id) VALUES (?,?)", (gps_id, data[0]))
    # Insert the temperature data
    cur.execute("INSERT or IGNORE INTO temperature(degree,id) VALUES (?, ?)", (data[5], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO ph(level,id) VALUES (?, ?)", (data[6], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO tds(ppm,id) VALUES (?, ?)", (data[7], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO do(percent,id) VALUES (?, ?)", (data[8], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO turbidity(ntu,id) VALUES (?, ?)", (data[9], gps_id))
    # Insert the ph data
    cur.execute("INSERT or IGNORE INTO orp(mvolts,id) VALUES (?, ?)", (data[10], gps_id))
    database.commit()
#check if start key is pressed (enter)
# function stops data line at end character, is also necessary to read the radio (don't know why tho)
def get_raw_data_from_serial(radio):
    '''Reads byte data stream from a serial connection and returns the data as a string.

    :param ~serial.Serial ser Serial connection to readline

    :return string raw UTF-8 encoded data
    '''
    # Flag to recognize the end of a line
    end_of_line = False
    # The initial raw data string
    raw = ''
    
    while not end_of_line:
        if radio.in_waiting:
            char = radio.read().decode('utf-8')
            if char == ';' or len(raw) > 500:
                end_of_line = True
            else:
                raw += char       
    return raw
while x==0: 
    if keyboard.is_pressed("enter"): 
        x=1
        print("starting database entries")
        # parsing and cleaning data for object initialization used in the no repeat line code
        #endcharacter()
        #print("end character found")
        #data_byte = radio.readline()
        #print("line read")
        david = get_raw_data_from_serial(radio)
        data = david.split(",")
        print("line decoded")
        # stuff to make sure that it doesn't write two lines twice
        #fetches most recent time stamp 
        n = data[2]
        #reads the ones place of the second data line was taken
        c = n[-1]
#active writing loop, loops until 'q' is pressed (you might need to hold 'q')
while not keyboard.is_pressed("q"):
    # actual parsing and cleaning of data
    #endcharacter()
    #data_byte = radio.readline()
    david = get_raw_data_from_serial(radio)
    data = david.split(",")
    data[0] = data[0].strip("b'")
    print("data parsed")
    print(data)
    
    #fetches newest timestamp 
    n = data[2]
    # ensures that data is not empty and that no repeat data is entered by checking previous timestamp against most recent timestamp
    if data != '' and c != n[-1]:
        #if you can't figure this one out you really shouldn't be trying to code
        data[10] = data[10].strip(";")
        write_data_to_database(data, database)
        print("data line written")
        #fetches newest timestamp
        n = data[2]
        #saves newest timestamp for next comparison
        c = n[-1]