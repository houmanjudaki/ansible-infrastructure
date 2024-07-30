import socket
import json
import time
import random

def generate_log():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    log = {
        "myfirstlog": f"{timestamp} hello devops",
        "iran": {
            "city": "tehran",
            "population": random.randint(1000000, 10000000),
            "men": random.randint(500000, 5000000),
            "women": random.randint(500000, 5000000),
            "hOffset": 2 * random.randint(1000000, 10000000),
            "vOffset": 100,
            "weather": "sunny"
        }
    }
    return json.dumps(log)

def send_log(log, host='localhost', port=514):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(log.encode(), (host, port))

if __name__ == "__main__":
    while True:
        log = generate_log()
        send_log(log)
        time.sleep(5)

