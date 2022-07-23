import stomp
import time
import json

user = 'xyz'
pwd = 'xyz123'
host = 'localhost'
port = '61616'
dest = 'UPLOAD.RAMESH'


class QueueListener(stomp.ConnectionListener):
    def on_error(self, payload):
        print("received an error")

    def on_message(self, payload):
        msg_body = payload.body.strip()
        print("received = %s" % msg_body)
        body_as_dist = json.loads(msg_body)
        print("first name = %s, last name = %s" % (body_as_dist['firstName'], body_as_dist['lastName']))


conn = stomp.Connection(host_and_ports=[(host, port)])
conn.set_listener('ListenerFromPython', QueueListener())
conn.connect(login=user, passcode=pwd, wait=True)
conn.subscribe(destination=dest, id=1, ack='auto')

print("Waiting for messages...")
while 1:
    time.sleep(10)
