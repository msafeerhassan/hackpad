import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_ssd1306 import Adafruit_SSD1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.neopixel import NeoPixel

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

neopixel = NeoPixel(board.GP6, 2)
keyboard.modules.append(neopixel)

i2c = busio.I2C(board.GP27, board.GP26)
display = Adafruit_SSD1306(128, 32, i2c)

PINS = [board.GP1, board.GP2, board.GP3, board.GP4]
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.MACRO("Hello"),
        KC.MACRO("Safeer!"),
        KC.MACRO("This is"),
        KC.MACRO("working!"),
    ]
]

def oledDisplay(text="Hackpad Ready"):
    display.fill(0)
    text_area = label.Label(terminalio.FONT, text=text, x=10, y=15)
    display.append(text_area)
    display.show()

def set_led_color(index, r, g, b):
    neopixel[index] = (r, g, b)
    neopixel.show()

if __name__ == '__main__':
    oledDisplay("Hackpad Ready")
    
    for i in range(2):
        set_led_color(i, 0, 0, 255)
    
    keyboard.go()
