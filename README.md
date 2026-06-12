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

## Struktur Folder
smart-room-monitoring-mqtt-sangpimandu/

│
├── README.md
├── skenario1_basic/
│   ├── publisher_basic.py
│   └── subscriber_basic.py
├── skenario2_qos/
│   ├── publisher_qos.py
│   └── subscriber_qos.py
├── skenario3_multitopic/
│   ├── publisher_multitopic.py
│   └── subscriber_multitopic.py
├── skenario4_wildcard_plus/
│   ├── publisher_plus.py
│   └── subscriberplus.py
└── skenario5_wildcard_hash/
├── publisherhash.py
└── subscriberhash.py

---

## Menjalankan Mosquitto Broker

```bash
mosquitto -v
```

> Broker berjalan di `localhost` port `1883`

---

## Skenario 1 — Komunikasi Dasar

```bash
cd skenario1_basic
python subscriber_basic.py
python publisher_basic.py
```

---

## Skenario 2 — Variasi QoS (0, 1, 2)

```bash
cd skenario2_qos
python subscriber_qos.py
python publisher_qos.py
```

---

## Skenario 3 — Beberapa Topik

```bash
cd skenario3_multitopic
python subscriber_multitopic.py
python publisher_multitopic.py
```

---

## Skenario 4 — Wildcard `+`

```bash
cd skenario4_wildcard+
python subscriberplus.py
python publisher_plus.py
```

---

## Skenario 5 — Wildcard `#`

```bash
cd skenario5_wildcard#
python subscriberhash.py
python publisherhash.py
```

---

> **Catatan:**
> - Jalankan subscriber terlebih dahulu sebelum publisher pada setiap skenario.
> - Gunakan **Ctrl+C** untuk menghentikan program publisher maupun subscriber.
> - Buka **dua terminal terpisah** untuk menjalankan publisher dan subscriber secara bersamaan.
