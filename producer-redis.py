import redis
import json
import time

class RedisMQTTProducer:
    def __init__(self, host="localhost", port=6379):
        self.broker = redis.Redis(host=host, port=port)

    def publish(self, channel, message):
        self.broker.publish(channel, json.dumps(message))

idx = 0
broker = RedisMQTTProducer()

while True:
    try:
        # try to connect to redis when connection failed
        if not broker:
            broker = RedisMQTTProducer()
    except: pass

    # mock data
    data = {
        "idx": idx
    }

    try:
        # prevent error on connection fail
        broker.publish("test", data)
        print("sending", idx)
    except Exception as e:
        print(e)
        time.sleep(1)
        continue

    # mock delay
    time.sleep(0.5)
    if idx > 100: idx = 0
    idx += 1