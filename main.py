import settings
import asyncio

import serialcom

async def main():
    asyncio.create_task(serialcom.commandTask())
    
    settings.load()

    print("Device configured as " + settings.get('type'))

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

