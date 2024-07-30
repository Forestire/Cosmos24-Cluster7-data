# code for Cosmos 2024 cluster 7 (R4US)
# Materials used: adafruit metro microcontroller, DS18x20 temperature sensor, ph sensor (4502c) dissolved oxygen sensor (model pending), Dissolved Solids sensor (KS0429 keyestudio TDS Meter
# V1.0), GPS (model pending), Holybro Telemetry 
# Radio, and wiring materials not included
# Analog sensors will require unique calibration, and modifications to the code will have to be made for proper calibration. Other possible changes include: Baud rate, used pins, and 
# libraries imported (in case of sensor model change)
# The main code (code.py on the microcontroller) is the Send data file, however, Send data uses code from other files in the folder
# Radio communication and data transmission is done using Holybro Telemetry radios (please ensure radios are calibrated properly and set to raw data instead of Mavlink) 
# Data is taken from the boat and transmitted to the base station which stores it in a database (in SQL)
# Database code is now included (hype)
# Note that tables and rows may need to be changed in the base_station.py file to get it written in your database. Other changes might need to be made like the com port as well as the data
# base name in order to ensure the code actually works.
# WILL ADD DATABASE ONCE VALID DATA IS GATHERED
