from __future__ import annotations

import csv
from pathlib import Path

from logtool.analyze import AnalysisResult


def export_top_table_csv(path: Path, header: list[str], rows: list[tuple[object, object]]) -> None:
    """
    Export a simple (key, count) style table to CSV.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for r in rows:
            writer.writerow(list(r))


def export_summary_csv(path: Path, result: AnalysisResult) -> None:
    """
    Export high-level summary stats to CSV.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value"])
        writer.writerow(["total_lines", result.total_lines])
        writer.writerow(["parsed_lines", result.parsed_lines])
        writer.writerow(["bad_lines", result.bad_lines])
        writer.writerow(["total_bytes", result.total_bytes])
