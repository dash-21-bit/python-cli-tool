from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Optional


# Regex for a simplified common log format:
# IP - - [date] "METHOD PATH HTTP/1.1" STATUS SIZE "-" "AGENT"
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+-\s+-\s+\[(?P<time>[^\]]+)\]\s+'
    r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+HTTP/[^"]+"\s+'
    r'(?P<status>\d{3})\s+(?P<size>\d+)\s+".*?"\s+"(?P<agent>[^"]*)"'
)


@dataclass(frozen=True)
class LogEntry:
    ip: str
    time: str
    method: str
    path: str
    status: int
    size: int
    agent: str


def parse_log_line(line: str) -> Optional[LogEntry]:
    """
    Parse a single log line.
    Returns a LogEntry if the line matches, otherwise returns None.
    """
    line = line.strip()
    if not line:
        return None

    m = LOG_PATTERN.match(line)
    if not m:
        return None

    return LogEntry(
        ip=m.group("ip"),
        time=m.group("time"),
        method=m.group("method"),
        path=m.group("path"),
        status=int(m.group("status")),
        size=int(m.group("size")),
        agent=m.group("agent"),
    )
