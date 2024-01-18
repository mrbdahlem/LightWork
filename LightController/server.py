import espnow
import machine
import json

enow = espnow.ESPNow()

def serve():
    peers = []
    for peer, msg in enow:
        # print(msg.decode('UTF-8') + " received from ", peer.hex())
        if peer is None:
            return
        if peer not in peers:
            peers.append(peer)
            try:
                enow.add_peer(peer)
            except OSError:
                pass

        #  Echo the MAC and message back to the sender
        if not enow.send(peer, msg):
            print("ERROR: send() failed to", peer.hex())
            return

        try:
            msg = json.loads(msg.decode('UTF-8'));
            msg['from_addr'] = peer
            print(str(msg))
        except ValueError as e:
            print(e)