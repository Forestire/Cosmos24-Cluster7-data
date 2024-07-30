class BoardRead(): 
    
    # PH probe 4502c
    #Adam Hawks (KM/S gay man)
    #Date 2024-07-12


    #initializing temperature sensor
    ow_bus = OneWireBus(board.D5)
    ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
    temp = "Temperature: {0:0.3f}C".format(ds18.temperature)
    def __init__(self, analog_pin):
        self._analog_in = analogIn(analog_pin)
        ph_probe=analogIn(board.A0)
    
        
    @property
    def ph(self):
        ph = 4681.14286 * self._analog_in.value
        return ph
    
    def SensorLoop(ph,temp):  
        while True:
            print(ph)
            print(temp)
            time.sleep(1.0)