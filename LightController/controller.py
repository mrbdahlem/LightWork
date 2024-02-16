import network
import aioespnow
import asyncio
import server

# A WLAN interface must be active to send()/recv()
ap = network.WLAN(network.AP_IF)  # network.AP_IF also requires STA_IF to send/recv
sta = network.WLAN(network.STA_IF)
ap.config(ssid='Control407', hidden=True)
ap.active(True)
sta.active(True)

# ap.disconnect()      # For ESP8266
print(ap.config('ssid') + ' on channel ' + str(ap.config('channel')));
print('Server mac:' + ap.config('mac').hex())

e = espnow.ESPNow()
e.active(True)
server.serve()