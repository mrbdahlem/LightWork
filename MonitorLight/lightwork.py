import espnow
import network

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('FLights')
sta.disconnect() # for esp8266

print("Connected: " + str(sta.isconnected()))

e = espnow.ESPNow()
e.active(True)
broadcast = b'\xFF\xFF\xFF\xFF\xFF\xFF'   # MAC address of peer's wifi interface

# e.add_peer(broadcast)      # Must add_peer() before send()

e.send(broadcast, '{"type":"JOINREQ"}')

while True:
    host, msg = e.recv()
    if msg:             # msg == None if timeout in recv()
        print(host.hex(), msg)
        if msg == b'end':
            break
