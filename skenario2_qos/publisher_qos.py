import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
TOPIC = "room/temperature"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

print("Publisher QoS aktif. Tekan Ctrl+C untuk berhenti.\n")

try:
    while True:
        suhu = round(random.uniform(24, 34), 1)

        client.publish(TOPIC, f"[QoS 0] Suhu: {suhu} °C", qos=0)
        print(f"Terkirim QoS 0 -> {suhu} °C")
        time.sleep(0.5)

        client.publish(TOPIC, f"[QoS 1] Suhu: {suhu} °C", qos=1)
        print(f"Terkirim QoS 1 -> {suhu} °C")
        time.sleep(0.5)

        client.publish(TOPIC, f"[QoS 2] Suhu: {suhu} °C", qos=2)
        print(f"Terkirim QoS 2 -> {suhu} °C")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()