from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from logtool.parser import LogEntry


@dataclass
class AnalysisResult:
    total_lines: int
    parsed_lines: int
    bad_lines: int
    top_ips: list[tuple[str, int]]
    top_paths: list[tuple[str, int]]
    status_counts: list[tuple[int, int]]
    total_bytes: int


def analyze(entries: list[LogEntry], total_lines: int, top_n: int = 10) -> AnalysisResult:
    """
    Analyze parsed log entries and return summary statistics.
    """
    ip_counter: Counter[str] = Counter()
    path_counter: Counter[str] = Counter()
    status_counter: Counter[int] = Counter()
    total_bytes = 0

    for e in entries:
        ip_counter[e.ip] += 1
        path_counter[e.path] += 1
        status_counter[e.status] += 1
        total_bytes += e.size

    parsed_lines = len(entries)
    bad_lines = total_lines - parsed_lines

    return AnalysisResult(
        total_lines=total_lines,
        parsed_lines=parsed_lines,
        bad_lines=bad_lines,
        top_ips=ip_counter.most_common(top_n),
        top_paths=path_counter.most_common(top_n),
        status_counts=status_counter.most_common(),
        total_bytes=total_bytes,
    )
