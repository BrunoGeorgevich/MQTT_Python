import paho.mqtt.client as mqtt_client
import time

CLIENT_ID = 'server'
BROKER_ADDRESS = 'localhost'
MQTT_TOPIC = 'robot_arm_point'


def UNUSED(x):
    return x


def on_message(client, userdata, message):
    UNUSED(client)
    UNUSED(userdata)
    print(str(message.payload.decode("utf-8")))


is_connected = False
client = mqtt_client.Client(CLIENT_ID)
client.on_message = on_message
client.connect(BROKER_ADDRESS)
client.loop_start()
client.subscribe(MQTT_TOPIC)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
# %%
