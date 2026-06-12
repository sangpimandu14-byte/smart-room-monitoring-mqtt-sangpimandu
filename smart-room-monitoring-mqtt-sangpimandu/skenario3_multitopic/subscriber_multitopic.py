import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPICS = [
    ("room/temperature", 0),
    ("room/humidity", 0),
    ("room/light", 0)
]

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic

    if topic == "room/temperature":
        print(f"Suhu      : {payload} °C")
    elif topic == "room/humidity":
        print(f"Kelembaban: {payload} %")
    elif topic == "room/light":
        print(f"Cahaya    : {payload} lux")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPICS)

print("Subscriber multitopik aktif. Tekan Ctrl+C untuk berhenti.\n")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber dihentikan.")
    client.disconnect()