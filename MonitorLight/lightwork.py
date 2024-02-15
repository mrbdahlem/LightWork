import network
import aioespnow
import asyncio

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('FLights')
sta.disconnect() # for esp8266

print("Connected: " + str(sta.isconnected()))

e = aioespnow.AIOESPNow()
e.active(True)
broadcast = b'\xFF\xFF\xFF\xFF\xFF\xFF'   # MAC address of peer's wifi interface

e.add_peer(broadcast)      # Must add_peer() before send()


# async def main(e, peer, timeout, period):
#     asyncio.create_task(heartbeat(e, peer, period))
#     asyncio.create_task(echo_server(e))
#     await asyncio.sleep(timeout)

# asyncio.run(main(e, peer, 120, 10))

e.send(broadcast, '{"type":"JOINREQ"}')

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(host.hex(), msg)
        if msg == b'end':
            break
