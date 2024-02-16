import network
import espnow
import server

# A WLAN interface must be active to send()/recv()
ap = network.WLAN(network.AP_IF)  # Or network.AP_IF
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