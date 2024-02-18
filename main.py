import asyncio
from machine import Pin
import sys

import settings
import serialcom

boot_button = Pin(9, Pin.IN)
led = Pin(8, Pin.OUT)

async def halt_button(button):
    led.off()
    while button.value() != 0:
        await asyncio.sleep(0.01)

    led.on()
    print("Halt pressed")
    sys.exit(1)

async def main():
    asyncio.create_task(serialcom.commandTask())
    
    settings.load()

    print("Device configured as " + str(settings.get('type')))
    led.off()

    asyncio.create_task(halt_button(boot_button))

    if settings.get('type') == "light":
        # import MonitorLight.lightwork as lightwork
        # asyncio.create_task(lightwork.run())
        pass
    elif settings.get('type') == "controller":
        import LightController.controller as controller
        asyncio.create_task(controller.run())

    else:
        print("Device not configured. Please open setup.html in a web browser.")
        
    while True:
        await asyncio.sleep(.01)

asyncio.run(main())

