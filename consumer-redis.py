import redis
import json

class RedisMQTTConsumer:
    def __init__(self, host="localhost", port=6379):
        self.broker = redis.Redis(host=host, port=port)
        self.client = self.broker.pubsub()

    def subscribe(self, channel):
        try:
            # try to get message
            message = self.client.get_message()
        except RuntimeError:
            # automatically subscribe
            self.client.psubscribe(channel)
            return self.subscribe(channel)

        # redis returns 1 in beginning, hence skipping
        if (not message) or (message["data"] == 1): return
        return message

broker = RedisMQTTConsumer()

while True:
    message = broker.subscribe("test")

    if message:
        print(json.loads(message["data"]))