import settings
import asyncio

config = settings.load()

if not config.device:
    print("Device not configured. Please open setup.html in a web browser.")
    while True:
        pass

print("Device configured as " + config.device)

if config.device == "light":
    import MonitorLight.lightwork as lightwork
    asyncio.create_task(lightwork.run(config))
elif config.device == "controller":
    import LightController.controller as controller
    asyncio.create_task(controller.run(config))