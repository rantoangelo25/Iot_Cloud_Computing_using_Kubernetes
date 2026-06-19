# Iot_Cloud_Computing_using_Kubernetes
Design and deployment of a cloud-native IoT platform using Kubernetes (k3s), MQTT, InfluxDB and Grafana for real-time sensor data monitoring.


## 📌 Description
This project implements a Cloud-native IoT monitoring platform using Kubernetes (k3s), MQTT, InfluxDB, and Grafana.

It simulates IoT sensors that generate real-time data, which is transmitted through MQTT, processed by a Python bridge, stored in a time-series database, and visualized using Grafana dashboards.

---

## 🏗️ Architecture

Sensors → MQTT Broker → Python Bridge → InfluxDB → Grafana

---

## ⚙️ Technologies used

- Python
- MQTT (Mosquitto)
- InfluxDB
- Grafana
- Kubernetes (k3s)
- YAML Deployments

---

## ☁️ Features

- Real-time IoT data simulation
- Message-based communication (MQTT)
- Data processing pipeline
- Time-series database storage
- Real-time dashboards

---

## 📊 Dashboard

Grafana is used to visualize:
- Temperature
- Humidity
- Distance
- Voltage

---

## ☸️ Deployment

All services are deployed using Kubernetes YAML configuration files.

---

## 🚀 Future improvements

- Cloud deployment (AWS / Azure)
- Auto-scaling Kubernetes
- AI-based anomaly detection

---

## 👨‍💻 Author

Student project - Cloud Computing & IoT
