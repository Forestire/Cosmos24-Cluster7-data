import time
import board
from analogio import AnalogIn
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
from SensorCode import BoardRead
ph_probe=SensorCode(board.A0)
import busio
import adafruit_gps

ow_bus = OneWireBus(board.D5)
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
deg_C = "Temperature: {0:0.3f}C".format(ds18.temperature)
ph = BoardRead.ph
boat_id = "Skynet"
#init GPS
uart = busio.UART(board.D3, board.D2, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
lat = gps.latitude
lon = gps.longitude
month = gps.timestamp_utc.tm_mon
year = gps.timestamp_utc.tm_year
day = gps.timestamp_utc.tm_mday
hour = gps.timestamp_utc.tm_hour
minute = gps.timestamp_utc.tm_min
sec = gps.timestamp_utc.tm_sec
last_print = time.monotonic()
while True: 
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            continue
        
        boat_data = "{},{}-{}-{},{:02}:{:02}:{:02},{:.6f},{:.6f},{:.3f},{}".format(
        boat_id,
        year,
        month,
        day,
        hour,
        minute,
        sec,
        lat,
        lon,
        deg_C,
        ph,
        )

        print(boat_data)
    time.sleep(1.0)