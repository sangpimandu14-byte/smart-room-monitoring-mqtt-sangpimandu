# Smart Room Monitoring — MQTT dengan Python

## Prasyarat

Pastikan sudah terinstal:
- Python 3.x
- Mosquitto Broker
- Library `paho-mqtt`

Install library:
```bash
pip install paho-mqtt
```

---

## Menjalankan Mosquitto Broker

```bash
mosquitto -v
```

> Broker berjalan di `localhost` port `1883`

---

## Skenario 1 — Komunikasi Dasar

```bash
python subscriber_basic.py
python publisher_basic.py
```

---

## Skenario 2 — Variasi QoS (0, 1, 2)

```bash
python subscriber_qos.py
python publisher_qos.py
```

---

## Skenario 3 — Beberapa Topik

```bash
python subscriber_multitopic.py
python publisher_multitopic.py
```

---

## Skenario 4 — Wildcard `+`

```bash
python subscriberplus.py
python publisher_plus.py
```

---

## Skenario 5 — Wildcard `#`

```bash
python subscriberhash.py
python publisherhash.py
```

---

> **Catatan:** Jalankan subscriber terlebih dahulu sebelum publisher pada setiap skenario.