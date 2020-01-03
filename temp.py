# Circuit Playground Temperature
# Reads the on-board temperature sensor and prints the value

import time

import adafruit_thermistor
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.004, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)    

while True:
    temp_c = thermistor.temperature
    temp_f = thermistor.temperature * 9 / 5 + 32
    print("Temperature is: %f C and %f F" % (temp_c, temp_f))
    
    if(temp_c<=29):
        colVal = BLUE
    elif(temp_c>29 and temp_c<29.2):
        colVal = GREEN
    elif(temp_c>29.2 and temp_c<29.4):
        colVal = YELLOW
    elif(temp_c>29.4 and temp_c<29.6):
        colVal = RED
    elif(temp_c>29.6 and temp_c<29.8):
        colVal = PURPLE
    elif(temp_c>29.8):
        colVal = CYAN
        
    print(colVal)
    for i in range(10):
        pixels[i] = colVal
    pixels.show()
    
    time.sleep(0.25)
