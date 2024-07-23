# PH probe 4502c
#Adam Hawks (KM/S gay man)
#Date 2024-07-12

import time
import board
from analogio import AnalogIn


class ph4502c():    

    def __init__(self, analog_pin):
        self._analog_in = AnalogIn(analog_pin)
    
    def get_ph(self):
        if analogin.value >= 46763: 
            ph= 17.288-0.00022*analogin.value
        if analogin.value < 46763:
            ph = 37.864-0.00066*analogin.value
        return ph
