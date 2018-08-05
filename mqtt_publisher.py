import paho.mqtt.client as mqtt_client

CLIENT_ID = 'user'
BROKER_ADDRESS = 'localhost'
MQTT_TOPIC = 'robot_arm_point'

client = mqtt_client.Client(CLIENT_ID)
client.connect(BROKER_ADDRESS)
client.publish(MQTT_TOPIC, 'Teste')
client.disconnect()
#%%