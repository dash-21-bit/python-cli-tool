from __future__ import annotations

from pathlib import Path
import random
from datetime import datetime, timedelta

random.seed(42)

OUT = Path("sample_data/logs/access.log")
OUT.parent.mkdir(parents=True, exist_ok=True)

ips = ["91.12.44.10", "91.12.44.11", "82.19.2.5", "10.0.0.2", "172.16.0.9"]
endpoints = ["/", "/home", "/login", "/products", "/products/1", "/cart", "/checkout", "/api/v1/items"]
methods = ["GET", "POST"]
statuses = [200, 200, 200, 301, 400, 401, 403, 404, 500]
agents = [
    "Mozilla/5.0",
    "curl/8.0",
    "PostmanRuntime/7.36.0",
    "python-requests/2.31.0",
]
sizes = [123, 532, 1024, 2048, 5120, 0]

base_time = datetime(2025, 12, 1, 10, 0, 0)

def random_time(i: int) -> str:
    t = base_time + timedelta(seconds=i * random.randint(1, 7))
    return t.strftime("%d/%b/%Y:%H:%M:%S +0000")

lines = []
for i in range(500):
    ip = random.choice(ips)
    method = random.choice(methods)
    path = random.choice(endpoints)
    status = random.choice(statuses)
    size = random.choice(sizes)
    agent = random.choice(agents)

    # Make some lines intentionally “bad” to test error handling
    if random.random() < 0.03:
        lines.append("BAD LINE THAT DOES NOT MATCH FORMAT\n")
        continue

    # Common Log Format (similar to Apache/Nginx)
    # Example:
    # 127.0.0.1 - - [10/Oct/2000:13:55:36 +0000] "GET / HTTP/1.1" 200 123 "-" "Mozilla/5.0"
    line = (
        f'{ip} - - [{random_time(i)}] '
        f'"{method} {path} HTTP/1.1" {status} {size} "-" "{agent}"\n'
    )
    lines.append(line)

OUT.write_text("".join(lines), encoding="utf-8")
print(f"Created sample log: {OUT} ({len(lines)} lines)")
