from __future__ import annotations

import argparse
from pathlib import Path

from logtool.parser import parse_log_line
from logtool.analyze import analyze
from logtool.export import export_summary_csv, export_top_table_csv
from logtool.plotting import plot_status_codes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="logtool",
        description="Beginner-friendly CLI to analyze access logs, export CSV reports, and generate charts.",
    )

    parser.add_argument(
        "logfile",
        type=str,
        help="Path to the log file to analyze.",
    )

    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of top results to show/export (default: 10).",
    )

    parser.add_argument(
        "--out",
        type=str,
        default="sample_data/output",
        help="Output folder for CSV results (default: sample_data/output).",
    )

    parser.add_argument(
        "--plot",
        action="store_true",
        help="If set, generate a PNG chart of status codes.",
    )

    return parser


def main() -> None:
    args = build_parser().parse_args()

    log_path = Path(args.logfile)
    out_dir = Path(args.out)

    if not log_path.exists():
        raise SystemExit(f"ERROR: Log file not found: {log_path}")

    total_lines = 0
    entries = []

    # Read file safely
    with log_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            total_lines += 1
            entry = parse_log_line(line)
            if entry is not None:
                entries.append(entry)

    result = analyze(entries, total_lines=total_lines, top_n=args.top)

    # Print summary to terminal
    print("\n=== Summary ===")
    print(f"Total lines:  {result.total_lines}")
    print(f"Parsed lines: {result.parsed_lines}")
    print(f"Bad lines:    {result.bad_lines}")
    print(f"Total bytes:  {result.total_bytes}")

    print("\n=== Top IPs ===")
    for ip, count in result.top_ips:
        print(f"{ip:15}  {count}")

    print("\n=== Top Paths ===")
    for path, count in result.top_paths:
        print(f"{path:20}  {count}")

    print("\n=== Status Codes ===")
    for code, count in result.status_counts:
        print(f"{code}  {count}")

    # Export CSV outputs
    export_summary_csv(out_dir / "summary.csv", result)
    export_top_table_csv(out_dir / "top_ips.csv", ["ip", "count"], result.top_ips)
    export_top_table_csv(out_dir / "top_paths.csv", ["path", "count"], result.top_paths)
    export_top_table_csv(out_dir / "status_codes.csv", ["status", "count"], result.status_counts)

    print(f"\nCSV files written to: {out_dir}")

    # Optional plot output (PNG)
    if args.plot:
        fig_path = Path("reports/figures/status_codes.png")
        plot_status_codes(result.status_counts, fig_path)
        print(f"PNG chart saved to: {fig_path}")


if __name__ == "__main__":
    main()
