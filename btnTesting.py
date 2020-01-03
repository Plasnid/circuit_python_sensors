# Circuit Playground digitalio example

import time
import board
import digitalio
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.004, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0,0,0)

button = digitalio.DigitalInOut(board.BUTTON_A)
button.switch_to_input(pull=digitalio.Pull.DOWN)

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

def a_true():
    for i in range(10):
        pixels[i] = RED
    pixels.show()
    time.sleep(0.25)

def b_true():
    for i in range(10):
        pixels[i] = GREEN
    pixels.show()
    time.sleep(0.25)

def ab_true():
    for i in range(10):
        pixels[i] = PURPLE
    pixels.show()
    time.sleep(0.25)

def no_btn():
    for i in range(10):
        pixels[i] = OFF
    pixels.show()
    time.sleep(0.25)

while True:
    if (button.value==True and buttonB.value!=True):  # button is pushed
        a_true()
    elif (buttonB.value==True and button.value!=True):
        b_true()
    elif(button.value==True and buttonB.value==True):
        ab_true()
    else:
        no_btn()

    time.sleep(0.01)
