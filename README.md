

# 🛡️ Omni-Sentinel X: Cyber Intelligence Engine

**Omni-Sentinel X** is a high-performance URL Security & Forensics tool designed to detect **Phishing**, **Malware**, and **Data Theft** using mathematical heuristics and real-time network analysis. Unlike standard scanners, it utilizes **Shannon Entropy** to identify DGA (Domain Generation Algorithms) and simulates visitor traffic to stress-test URL behavior.



---

## 🚀 Core Intelligence Features

* **🧠 DGA Entropy Analysis:** Calculates the mathematical "randomness" of a domain to detect botnet Command & Control (C2) servers.
* **📡 Live Network Forensics:** Performs real-time DNS resolution, IP Geolocation (via RDAP), and SSL certificate validation.
* **🔍 Triple-Threat Detection:**
    * **Phishing:** Identifies credential harvester keywords and impersonation patterns.
    * **Malware:** Scans for payload extensions (`.exe`, `.scr`) and shell injection commands.
    * **Data Theft:** Detects sensitive parameter leakage (session tokens, auth keys) in GET requests.
* **👥 Visitor Simulation:** Models how "safe" vs "malicious" URLs handle traffic, including bounce rates and blocked request tracking.
* **📊 Interactive Dashboard:** A Dark-Mode Plotly interface providing a 4-quadrant view of the threat landscape.

---

## 📂 Project Structure

```text
├── sentinel_x.py           # The Main Intelligence Engine
├── requirements.txt        # System Dependencies
├── reports/                # Auto-generated CSV security reports
└── README.md               # Project Documentation
