# 🔐 LogGuard – Security Log Analyzer

**A Java and Python-based security log analyzer with a Flask web dashboard for identifying suspicious login activity.**

## 📌 Project Overview

LogGuard is a cybersecurity project designed to analyze login logs, identify suspicious login patterns, classify IP addresses based on failed login attempts, and display security insights through a web dashboard.

It combines Java for log analysis, Python for data processing, and Flask for the web application.

## ✨ Features

- **Login Log Analysis:** Reads and analyzes login records.
- **Brute-Force Detection:** Java module identifies IP addresses with 5 or more failed attempts within a 10-minute window.
- **Risk Classification:** Python classifies IP addresses as HIGH, MEDIUM, or LOW risk.
- **Security Dashboard:** Displays login statistics and security reports.
- **IP-wise Analysis:** Shows successful and failed login attempts for each IP.
- **Search and Filtering:** Search IP addresses and filter by risk level.
- **Security Alerts:** Displays alerts for high-risk IP addresses.
- **CSV Export:** Download the generated security report.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Java | Login log analysis |
| Python | Threat detection and risk classification |
| Pandas | Data processing and analysis |
| Flask | Backend web framework |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Search and filtering |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
LogGuard/
│
├── java/
│   └── LogAnalyzer.java
│
├── python/
│   └── threat_detector.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── data/
│   └── login_logs.txt
│
├── output/
│   └── security_report.csv
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/aryanbabel-cell/LogGuard.git
```

### 2. Open the project folder

```bash
cd LogGuard
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Python threat detector

```bash
python python/threat_detector.py
```

This generates the security report in the `output` folder.

### 5. Run the Java log analyzer

Compile and execute from the project root:

```bash
javac java/LogAnalyzer.java
java -cp java LogAnalyzer
```

### 6. Start the Flask dashboard

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 📊 Risk Classification

| Failed Login Attempts | Risk Level |
|---|---|
| 0–1 | LOW |
| 2–4 | MEDIUM |
| 5 or more | HIGH |

The Java detection module additionally checks whether five or more failed attempts occur within a 10-minute window.

## 🔍 Sample Analysis

The sample dataset contains login records from four IP addresses.

| IP Address | Failed Attempts | Risk |
|---|---:|---|
| 192.168.1.5 | 0 | Not included in risk report |
| 192.168.1.8 | 5 | HIGH |
| 192.168.1.10 | 2 | MEDIUM |
| 192.168.1.12 | 0 | Not included in risk report |

## ⚠️ Project Limitations

- Uses sample login records rather than live system monitoring.
- Detection rules are illustrative and are not a replacement for production-grade security tools.
- Java and Python currently run as separate analysis modules.
- The dashboard reads the Python-generated CSV report.

## 🚀 Future Enhancements

- Real-time log monitoring.
- Database integration.
- Automated IP blocking.
- Advanced anomaly detection.
- User authentication and dashboard access control.
- Integration of Java and Python analysis into one automated pipeline.

## 👨‍💻 Author

**Aryan Babel**

Computer Engineering Student

GitHub: [aryanbabel-cell](https://github.com/aryanbabel-cell)

---

*LogGuard – Making login activity easier to analyze and understand.*