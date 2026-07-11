# Network Security Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/Version-1.0-success)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Overview

The Network Security Monitoring System is a Python-based offline log analysis tool designed to analyze authentication logs and identify suspicious login activity. The application parses network log files, extracts useful security metrics, detects potential brute-force attacks, and generates a structured security report.

The project follows a modular architecture with separate components for parsing, analysis, threat detection, and reporting, making it easier to maintain, extend, and test while serving as a foundation for more advanced cybersecurity projects.

## Current Status

**Version:** 1.0

✔ Core monitoring pipeline completed

✔ Log parsing

✔ Security analysis

✔ Brute-force attack detection

✔ Report generation


## Features

- Parse authentication log files.
- Extract useful security metrics such as:
  - Total log entries
  - Failed login attempts
  - Unique IP addresses
- Detect brute-force attacks based on configurable failed login thresholds.
- Generate a structured security report.
- Modular architecture with separate components for parsing, analysis, detection, reporting, and application orchestration.

## Project Architecture
```text
               +----------------------+
               |   Authentication     |
               |      Log File        |
               +----------+-----------+
                          |
                          v
                 +----------------+
                 |    Parser      |
                 +----------------+
                          |
                          v
                 +----------------+
                 |   Analyzer     |
                 +----------------+
                          |
                          |
          +---------------+---------------+
          |                               |
          v                               v
+----------------------+        +----------------------+
| Security Statistics  |        | Threat Detection     |
+----------------------+        +----------------------+
          \                               /
           \                             /
            \                           /
             +-------------------------+
             |        Reporter         |
             +-------------------------+
                         |
                         v
              Network Security Report
```

## Project Structure
```text
network-security-monitoring-system/
│
├── data/
│   └── sample_log.txt          # Sample authentication log file
│
├── src/
│   ├── parser.py               # Parses raw log entries
│   ├── analyzer.py             # Calculates security statistics
│   ├── detector.py             # Detects suspicious login activity
│   ├── reporter.py             # Generates the security report
│   └── main.py                 # Entry point of the application
│
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── .gitignore                  # Files ignored by Git
```


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sunkencoder19/network-security-monitoring-system.git
```

### 2. Navigate to the project directory

```bash
cd network-security-monitoring-system
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```
> **Note:** Version 1 uses only Python's standard library, so `requirements.txt` is currently empty. It is included to support future versions of the project that introduce external dependencies.

## Usage

Run the application using:

```bash
python3 src/main.py
```

The application will:

1. Read the authentication log file.
2. Parse the log entries.
3. Analyze login statistics.
4. Detect suspicious login activity.
5. Generate a security report in the terminal.

## Sample Input

Example log entries:

```text
10:15:21 192.168.1.10 LOGIN_FAILED
10:15:30 192.168.1.10 LOGIN_FAILED
10:15:45 192.168.1.10 LOGIN_SUCCESS
10:16:00 192.168.1.20 LOGIN_FAILED
10:16:20 192.168.1.30 LOGIN_SUCCESS
10:16:45 192.168.1.10 LOGIN_FAILED
10:17:00 192.168.1.10 LOGIN_FAILED
10:17:15 192.168.1.10 LOGIN_FAILED
10:17:30 192.168.1.10 LOGIN_FAILED
```

## Sample Output

```text
===== Network Security Monitoring Report =====
Total Logs: 9
Failed Logins: 7
Unique IPs: 3

===== Security Alerts =====
Total Alerts: 1
Suspicious IPs:
192.168.1.10
```

## Technologies Used

- Python 3
- Git & GitHub
- Python Standard Library

## Future Improvements (Version 2)

The next version of this project aims to extend the monitoring system with more advanced cybersecurity and software engineering features, including:

- Threat intelligence integration using public IP reputation APIs.
- Multiple attack detection rules.
- Professional HTML report generation.
- Command-line interface (CLI) support.
- Configurable detection thresholds using a configuration file.
- Improved error handling and input validation.
- Unit testing for core modules.

## Author

**Fattesing Rane**

Computer Engineering Student

GitHub: [Sunkencoder19](https://github.com/Sunkencoder19)