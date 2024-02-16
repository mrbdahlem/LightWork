import asyncio
import ujson
import sys
import time
import select
import settings
import machine

timeout = 5.0

buffer = ''
def readLine():
    global buffer
    data = None
    line = None
    
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
    
    if line is not None:
        line = line.strip()
    return line

async def commandTask():
    sys.stdout.write(">\n")

    while True:
        data = readLine()

        if data is not None:
            if len(data) == 0: # just a newline
                pass

            elif data == "loadconfig":
                await loadConfig()

            elif data == "config":
                await storeConfig()

            elif data == "reset":
                machine.reset()

            else:
                sys.stdout.write("Unknown command: " + data + "\n")
        
            sys.stdout.write(">\n")

        await asyncio.sleep(.01)


async def loadConfig():
    sys.stdout.write("$\n")
    try:
        config = settings.load()
        sys.stdout.write(ujson.dumps(config) + "\n")
    except:
        sys.stdout.write("Invalid config file\n")



async def storeConfig():
    sys.stdout.write("$\n")
    try:
        config = ''

        start = time.time()

        while True:
            if (time.time() - start > timeout):
                sys.stdout.write("Timeout\n")
                raise Exception("Timeout")

            data = readLine()

            if data is not None:
                config += data + "\n"
                if data.endswith('}'):
                    break

            await asyncio.sleep(.01)
        
        config = ujson.loads(config)

        settings.update(config)

        sys.stdout.write("OK\n")
    except:
        sys.stdout.write("Invalid config data\n" + config + "\n")