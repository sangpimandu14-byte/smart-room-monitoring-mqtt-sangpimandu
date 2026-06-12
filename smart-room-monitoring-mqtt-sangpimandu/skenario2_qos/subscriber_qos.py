import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "room/temperature"

def on_message(client, userdata, msg):
    print(f"Data diterima -> {msg.topic} : {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC, qos=2)

print("Subscriber QoS aktif. Tekan Ctrl+C untuk berhenti.\n")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber dihentikan.")
    client.disconnect()