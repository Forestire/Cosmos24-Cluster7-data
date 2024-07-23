import time
import board
from analogio import AnalogIn

analogin = AnalogIn(board.A5)
while True: 
    if analogin.value >= 46763: 
        print(17.288-0.00022*analogin.value)
        time.sleep(1.0)
    if analogin.value < 46763:
        print(37.864-0.00066*analogin.value)
        time.sleep(1.0)
    #else:
    #   print(analogin.value)
    #    print("error: invalid range")
    #
    # time.sleep(1.0)