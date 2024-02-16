import network
import aioespnow
import asyncio
import hardware

# e = aioespnow.AIOESPNow()
# e.active(True)
# broadcast = b'\xFF\xFF\xFF\xFF\xFF\xFF'   # MAC address of peer's wifi interface

# e.add_peer(broadcast)      # Must add_peer() before send()

# async def main(e, peer, timeout, period):
#     asyncio.create_task(heartbeat(e, peer, period))
#     asyncio.create_task(echo_server(e))
#     await asyncio.sleep(timeout)

# asyncio.run(main(e, peer, 120, 10))

# e.send(broadcast, '{"type":"JOINREQ"}')

# while True:
#     host, msg = e.recv()
#     if msg:             # msg == None if timeout in recv()
#         print(host.hex(), msg)
#         if msg == b'end':
#             break

async def run(config):
    if not config.ssid:
        print("SSID not configured. Please open setup.html in a web browser.")
        while True:
            pass

    print("SSID configured as " + config.ssid)

    config.sta = network.WLAN(network.STA_IF)
    config.sta.active(True)
    config.sta.connect(config.ssid)

    print("Connected: " + str(config.sta.isconnected()))

    config.e = aioespnow.AIOESPNow()
    config.e.active(True)



