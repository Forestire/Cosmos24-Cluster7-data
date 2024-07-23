# Author: Adam Hawks
# code for Cosmos 2024 cluster 7 (R4US)
# Materials used: adafruit metro microcontroller, DS18x20 temperature sensor, ph sensor (4502c) dissolved oxygen sensor (model pending), Dissolved Solids sensor (KS0429 keyestudio TDS Meter V1.0), GPS (model pending), Holybro Telemetry 
# radio, wiring materials not included
# Analog sensors will require unique calibration, and modifications to the code will have to be made for proper calibration. Other possible changes include: Baud rate, used pins and libraries imported (in case of sensor model change)
# The main code (code.py on the microcontroller) is the Send data file, however, Send data uses code from other files in the folder
# radio communication and data transmission is done using Holybro Telemetry radios (please ensure radios are calibrated properly and set to raw data instead of Mavlink) 
# data is taken from boat and transmitted to base station which stores it in a database (in SQL)
# database code is currently not included, and all code shown is only for the boat
