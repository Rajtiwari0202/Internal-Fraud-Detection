import pandas as pd
import random
from datetime import datetime , timedelta

import pandas as pd
import random
from datetime import datetime, timedelta

NUM_EMPLOYEES = 50
NUM_RECORDS = 5000

actions = ["login", "transaction", "download", "logout"]

def random_timestamp():
    start = datetime.now() - timedelta(days=7)
    return start + timedelta(minutes=random.randint(0, 10000))

def generate_normal_record(emp_id):
    return {
        "employee_id": f"E{emp_id}",
        "timestamp": random_timestamp(),
        "action": random.choice(actions),
        "amount": random.randint(1000, 50000),
        "ip_address": f"192.168.1.{random.randint(1,255)}",
        "device": random.choice(["laptop", "desktop"]),
        "location": random.choice(["Mumbai", "Delhi", "Bangalore"]),
        "is_anomaly": 0
    }

def generate_anomaly_record(emp_id):
    anomaly_type = random.choice(["high_transaction", "off_hour", "bulk_download"])

    timestamp = random_timestamp()

    if anomaly_type == "off_hour":
        timestamp = timestamp.replace(hour=random.choice([1, 2, 3, 4]))

    return {
        "employee_id": f"E{emp_id}",
        "timestamp": timestamp,
        "action": random.choice(actions),
        "amount": random.randint(500000, 2000000),  # huge amount
        "ip_address": f"10.0.0.{random.randint(1,255)}",
        "device": "unknown",
        "location": "Unknown",
        "is_anomaly": 1
    }

data = []

for _ in range(NUM_RECORDS):
    emp_id = random.randint(1, NUM_EMPLOYEES)

    if random.random() < 0.1:  # 10% anomalies
        data.append(generate_anomaly_record(emp_id))
    else:
        data.append(generate_normal_record(emp_id))

df = pd.DataFrame(data)
df.to_csv("backend/app/data/raw/logs.csv", index=False)

print("✅ Fake data generated successfully!")