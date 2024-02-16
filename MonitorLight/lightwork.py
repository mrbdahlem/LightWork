import network
import aioespnow
import asyncio
import hardware
import settings

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

async def run():
    ssid = settings.get('ssid')

    if not ssid:
        print("SSID not configured. Please open setup.html in a web browser.")
        while True:
            pass

    print("SSID configured as " + ssid)

    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(ssid)

    print("Connected: " + str(sta.isconnected()))

    e = aioespnow.AIOESPNow()
    e.active(True)



