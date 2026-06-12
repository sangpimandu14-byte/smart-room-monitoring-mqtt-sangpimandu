import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.loop_start()

print("Publisher multitopik aktif. Tekan Ctrl+C untuk berhenti.\n")

try:
    while True:
        suhu = round(random.uniform(24, 34), 1)
        kelembaban = round(random.uniform(55, 80), 1)
        cahaya = random.randint(100, 800)

        client.publish("room/temperature", str(suhu))
        client.publish("room/humidity", str(kelembaban))
        client.publish("room/light", str(cahaya))

        print(f"Suhu     -> room/temperature : {suhu} °C")
        print(f"Kelembaban -> room/humidity  : {kelembaban} %")
        print(f"Cahaya   -> room/light       : {cahaya} lux")
        print("-" * 40)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()