from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt


def plot_status_codes(status_counts: list[tuple[int, int]], out_path: Path) -> None:
    """
    Create a bar chart of HTTP status code distribution and save to PNG.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    codes = [str(code) for code, _ in status_counts]
    counts = [count for _, count in status_counts]

    plt.figure()
    plt.bar(codes, counts)
    plt.title("HTTP Status Code Distribution")
    plt.xlabel("Status Code")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
