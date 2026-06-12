import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
TOPIC = "room/temperature"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

print("Publisher aktif. Tekan Ctrl+C untuk berhenti.\n")

try:
    while True:
        suhu = round(random.uniform(24, 34), 1)
        client.publish(TOPIC, str(suhu))
        print(f"Data terkirim -> {TOPIC} : {suhu} °C")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()