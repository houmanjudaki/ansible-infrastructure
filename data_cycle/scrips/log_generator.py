import socket
import json
import random
import time

def generate_log():
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    random_long = random.randint(1000, 10000)
    random_short = random.randint(1, 10)
    log_data = {
        "timestamp": timestamp,
        "message": "hello devops",
        "iran": {
            "city": "tehran",
            "population": random_long,
            "men": random_long // 2,
            "women": random_long // random_short,
            "hOffset": 2 * random_long,
            "vOffset": 100,
            "weather": "sun1.city = (sun1.city / 100) * 90;"
        }
    }
    return json.dumps(log_data)

def send_log():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        while True:
            log_message = generate_log()
            sock.sendto(log_message.encode(), ('localhost', 5140))
            time.sleep(5)

if __name__ == '__main__':
    send_log()
