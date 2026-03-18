# 🛡️ Internal Fraud Detection System

An AI-powered system to monitor employee behavior in banking systems and detect suspicious activities such as unusual transactions, off-hour access, bulk data downloads, and privilege misuse.

---

## 🚀 Project Overview

This system simulates a real-world banking fraud detection pipeline:

- 📊 Monitors employee activity logs
- 🧠 Detects anomalies using Machine Learning
- ⚠️ Generates risk scores and alerts
- 📈 Provides dashboards for investigation teams

---

## 🏗️ Project Structure
internal-fraud-detection/
│
├── backend/
│ └── app/
│ └── data/
│ └── raw/
│
├── scripts/
│ └── generate_fake_data.py
│
├── docs/
│ └── architecture.md
│
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Rajtiwari0202/Internal-Fraud-Detection.git
cd Internal-Fraud-Detection
```

## 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r backend/requirements.txt
📊 Generate Dataset

Run the script to generate fake employee logs:

python scripts/generate_fake_data.py

This will create:

backend/app/data/raw/logs.csv
🧠 Data Description

Each record contains:

employee_id

timestamp

action (login / transaction / download)

amount

ip_address

device

location

is_anomaly (0 = normal, 1 = suspicious)