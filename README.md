# Python CLI Tool — Log Analyzer (logtool)

**Repo:** python-cli-tool  
**Project Type:** Beginner CLI application (clean code + error handling + outputs)  
**Outputs:** CSV reports + PNG chart  
**Author:** Adarsh Ravi

---

## 1. Overview

This project is a command-line tool named **logtool** that analyzes web server access logs (Apache/Nginx-style).  
It is designed to demonstrate beginner-to-intermediate Python competence through:

- reading files safely,
- parsing structured text with regex,
- handling invalid data without crashing,
- producing useful summary statistics,
- exporting results to CSV (a common workplace format),
- generating a PNG chart image for visual interpretation.

Unlike “toy calculators”, this tool solves a real-world problem: quickly understanding traffic patterns and errors from logs.

---

## 2. Key Features

### 2.1 Parse Access Logs Safely
- Uses a regex-based parser for a simplified common log format.
- Lines that don’t match are treated as “bad lines” instead of crashing.

### 2.2 Summary Statistics
The tool computes:
- total lines
- parsed lines
- bad lines
- total bytes served
- top IP addresses
- top requested paths
- HTTP status code distribution

### 2.3 Export Outputs (CSV)
Generates CSV files:
- `summary.csv`
- `top_ips.csv`
- `top_paths.csv`
- `status_codes.csv`

### 2.4 Generate Image Output (PNG)
With `--plot`, creates:
- `reports/figures/status_codes.png`

This is important for portfolio value: it proves you can produce “visible output” from code.

---

## 3. Included Dataset (So It Works Immediately)

This repo includes a sample dataset:
- `sample_data/logs/access.log`

It is generated using:
- `scripts/generate_sample_log.py`

The generator intentionally adds a small percentage of invalid lines to prove error handling works.

---

## 4. Project Structure
python-cli-tool/
├── src/logtool/
│   ├── cli.py
│   ├── parser.py
│   ├── analyze.py
│   ├── export.py
│   └── plotting.py
├── scripts/
│   └── generate_sample_log.py
├── sample_data/
│   ├── logs/access.log
│   └── output/
├── reports/figures/
│   └── status_codes.png
├── requirements.txt
├── pyproject.toml
└── README.md
---

## 5. Installation (Terminal Only)

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```
## 6. Usage
Help
```
logtool --help
```
Basic analysis
```
logtool sample_data/logs/access.log
```
Export CSV results
```
logtool sample_data/logs/access.log --out sample_data/output --top 5
```
Generate PNG chart
```
logtool sample_data/logs/access.log --plot
```
