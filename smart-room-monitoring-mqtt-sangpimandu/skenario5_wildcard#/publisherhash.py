import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

print("Publisher wildcard # aktif. Tekan Ctrl+C untuk berhenti.\n")

try:
    while True:
        suhu = round(random.uniform(24, 34), 1)
        kelembaban = round(random.uniform(55, 80), 1)
        cahaya = random.randint(100, 800)

        client.publish("room/sensor/temperature", str(suhu))
        client.publish("room/sensor/humidity", str(kelembaban))
        client.publish("room/sensor/light", str(cahaya))
        client.publish("room/status", "online")

        print(f"Terkirim -> room/sensor/temperature : {suhu} °C")
        print(f"Terkirim -> room/sensor/humidity    : {kelembaban} %")
        print(f"Terkirim -> room/sensor/light       : {cahaya} lux")
        print(f"Terkirim -> room/status             : online")
        print("-" * 40)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()