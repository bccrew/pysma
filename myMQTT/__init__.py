import paho.mqtt.client as mqtt
import queue


class myMQTT(mqtt.Client):
    def on_connect(self, mqttc, obj, flags, rc):
        for i in self.subscriptions:
            self.subscribe(i)

    def on_message(self, mqttc, obj, msg):
        self.messages.put((msg.topic, msg.payload))

    '''
        use run(addr="URL", subscriptions=<string or list of strings>)
    '''

    def run(self, **kwargs):
        self.subscriptions = kwargs.get('subscriptions', [])
        self.messages = queue.Queue()

        self.connect(kwargs.get('addr'), 1883, 60)
        self.loop_start()

    def getMessages(self):
        while not self.messages.empty():
            yield self.messages.get()
