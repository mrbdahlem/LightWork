from machine import Pin
import neopixel

led = Pin(2, Pin.OUT)

np = neopixel.NeoPixel(Pin(14), 36)
SW1 = Pin(4, Pin.IN, Pin.PULL_UP)
SW2 = Pin(5, Pin.IN, Pin.PULL_UP)


def set_color(color):
    for n in range(35):
        np[n] = color

    np.write()


while True:
    if SW2.value() == 0:
        color = (255, 0, 0)
        led.on()
    else:
        color = (255, 255, 255)
        led.off()
    set_color(color)
