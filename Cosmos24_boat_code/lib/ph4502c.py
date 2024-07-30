# PH probe 4502c
#Adam Hawks (KM/S gay man)
#Date 2024-07-12

import time
import board
from analogio import AnalogIn
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

#initializing temperature


class ph4502c():    
    ow_bus = OneWireBus(board.D0) 
    ds18 = DS18X20(ow_bus, ow_bus.scan()[0])

    def __init__(self, analog_pin):
        self._analog_in = analogIn(analog_pin)
        ph_in=analogIn(board.A0)
        print(ph_in)
        
    
    def get_ph(self):
        ph = 4681.14286 * self._analog_in.value
        return ph
