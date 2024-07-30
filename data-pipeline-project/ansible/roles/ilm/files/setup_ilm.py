import requests
import json
import subprocess

# تنظیمات Elasticsearch
ES_HOST = "http://localhost:9200"
ILM_POLICY_NAME = "my_policy"
INDEX_TEMPLATE_NAME = "my_template"
INDEX_NAME = "my_index-000001"
ROLLOVER_ALIAS = "my_index"

# تنظیمات Kafka
KAFKA_TOPIC = "mytopic"
KAFKA_BROKER = "localhost:9092"
RETENTION_MS = 3 * 60 * 60 * 1000  # سه ساعت به میلی‌ثانیه

# پالیسی ILM
ilm_policy = {
    "policy": {
        "phases": {
            "hot": {
                "actions": {
                    "rollover": {
                        "max_size": "50GB",
                        "max_age": "30d"
                    }
                }
            },
            "delete": {
                "min_age": "90d",
                "actions": {
                    "delete": {}
                }
            }
        }
    }
}

# الگوی ایندکس
index_template = {
    "index_patterns": [f"{ROLLOVER_ALIAS}-*"],
    "template": {
        "settings": {
            "index.lifecycle.name": ILM_POLICY_NAME,
            "index.lifecycle.rollover_alias": ROLLOVER_ALIAS
        }
    }
}

# ایجاد پالیسی ILM
def create_ilm_policy():
    url = f"{ES_HOST}/_ilm/policy/{ILM_POLICY_NAME}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, headers=headers, data=json.dumps(ilm_policy))
    if response.status_code == 200:
        print("ILM policy created successfully.")
    else:
        print(f"Failed to create ILM policy: {response.text}")

# ایجاد الگوی ایندکس
def create_index_template():
    url = f"{ES_HOST}/_index_template/{INDEX_TEMPLATE_NAME}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, headers=headers, data=json.dumps(index_template))
    if response.status_code == 200:
        print("Index template created successfully.")
    else:
        print(f"Failed to create index template: {response.text}")

# ایجاد ایندکس اولیه
def create_initial_index():
    url = f"{ES_HOST}/{INDEX_NAME}"
    headers = {"Content-Type": "application/json"}
    data = {
        "aliases": {
            ROLLOVER_ALIAS: {
                "is_write_index": True
            }
        }
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Initial index created successfully.")
    else:
        print(f"Failed to create initial index: {response.text}")

# تنظیم ریتنشن برای تاپیک کافکا
def set_kafka_retention():
    command = [
        "kafka-configs.sh",
        "--bootstrap-server", KAFKA_BROKER,
        "--alter",
        "--entity-type", "topics",
        "--entity-name", KAFKA_TOPIC,
        "--add-config", f"retention.ms={RETENTION_MS}"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Kafka retention policy set successfully.")
    else:
        print(f"Failed to set Kafka retention policy: {result.stderr}")

if __name__ == "__main__":
    create_ilm_policy()
    create_index_template()
    create_initial_index()
    set_kafka_retention()

