import requests, pandas as pd, numpy as np, matplotlib.pyplot as plt
import tldextract, validators, hashlib, json, re, time, socket, ssl, urllib.parse, math
from datetime import datetime
from collections import Counter, defaultdict
from ipwhois import IPWhois
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings

warnings.filterwarnings("ignore")

# ── GLOBAL CONFIGURATION ─────────────────────────────────────
print("✅ Cyber Intelligence Modules Loaded")
print("=" * 60)
print("  🛡️ OMNI-SENTINEL X: ADVANCED THREAT INTELLIGENCE")
print("=" * 60)

class OmniSentinelEngine:
    """
    The World's Most Powerful URL Security Project.
    Combines Heuristic Entropy, Data Theft Detection, and Visitor Simulation.
    """

    def __init__(self):
        self.visit_log = []
        # Advanced Intelligence Signatures
        self.signatures = {
            "PHISHING": [r"login", r"verify", r"secure", r"account", r"update", r"banking", r"wp-content"],
            "MALWARE": [r"\.exe$", r"\.zip$", r"\.scr$", r"bin/", r"payload", r"dropper", r"cmd=", r"shell"],
            "DATA_THEFT": [r"token=", r"session=", r"cookie=", r"key=", r"auth=", r"passwd", r"etc/shadow"],
            "XSS_SQLI": [r"javascript:", r"<script", r"onerror=", r"union.*select", r"drop.*table"]
        }
        self.third_party_blacklist = ["ads.doubleclick.net", "malware-host.ru", "phish-site.cn", "botnet.io"]

    def calculate_entropy(self, text):
        """Detects Domain Generation Algorithms (DGA) used by Malware C2 centers."""
        if not text: return 0
        probs = [n_x/len(text) for x, n_x in Counter(text).items()]
        return -sum(p * math.log(p, 2) for p in probs)

    def analyze_url(self, url):
        print(f"\n📡 Deep Scan Initiated: {url}")
        parsed = urllib.parse.urlparse(url)
        ext = tldextract.extract(url)
        domain = f"{ext.domain}.{ext.suffix}"
        
        res = {
            "url": url, "timestamp": datetime.now().strftime("%H:%M:%S"),
            "threat_score": 0, "flags": [], "strength": "",
            "entropy": round(self.calculate_entropy(ext.domain), 2),
            "ip": "Unknown", "country": "Unknown", "org": "Unknown",
            "ssl_valid": False, "status": 0
        }

        # 1. URL FORMAT & ENTROPY (DGA DETECTION)
        if not validators.url(url):
            res["threat_score"] += 50
            res["flags"].append("❌ INVALID_URL_STRUCTURE")
        
        if res["entropy"] > 4.0:
            res["threat_score"] += 35
            res["flags"].append(f"🚩 HIGH_ENTROPY_DGA ({res['entropy']})")

        # 2. HEURISTIC SIGNATURE MATCHING
        for category, patterns in self.signatures.items():
            for p in patterns:
                if re.search(p, url.lower()):
                    weight = 40 if category == "DATA_THEFT" else 30
                    res["threat_score"] += weight
                    res["flags"].append(f"⚠️ {category}_INDICATOR: '{p}'")

        # 3. LIVE NETWORK FORENSICS
        try:
            # IP & Geolocation
            res["ip"] = socket.gethostbyname(parsed.hostname)
            try:
                obj = IPWhois(res["ip"])
                rdap = obj.lookup_rdap(depth=1)
                res["country"] = rdap.get("network", {}).get("country", "??")
                res["org"] = rdap.get("network", {}).get("name", "Unknown")
            except: pass

            # SSL Check
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=parsed.hostname) as s:
                s.settimeout(3)
                s.connect((parsed.hostname, 443))
                res["ssl_valid"] = True
            
            # Request Validation
            resp = requests.get(url, timeout=5, headers={"User-Agent": "Sentinel-X/2.0"})
            res["status"] = resp.status_code
            if any(tp in resp.text for tp in self.third_party_blacklist):
                res["threat_score"] += 25
                res["flags"].append("🚨 MALICIOUS_THIRD_PARTY_CONTENT")

        except Exception as e:
            res["flags"].append(f"🔌 CONNECTION_ERR: {str(e)[:20]}")

        # 4. VISITOR SIMULATION ENGINE
        import random
        random.seed(hash(url))
        res["visitors"] = random.randint(100, 1000)
        res["entered"] = int(res["visitors"] * (0.2 if res["threat_score"] > 50 else 0.8))
        res["blocked"] = random.randint(0, 50) if res["threat_score"] < 40 else random.randint(50, 200)

        # FINAL RATING
        s = res["threat_score"]
        res["strength"] = "🔴 CRITICAL" if s >= 60 else "🟠 WEAK" if s >= 30 else "🟢 STRONG"
        
        print(f"   [Result] Score: {res['threat_score']} | Strength: {res['strength']}")
        self.visit_log.append(res)
        return res

    def generate_dashboard(self):
        df = pd.DataFrame(self.visit_log)
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=("🎯 Threat Severity Matrix", "👥 Visitor Engagement", 
                            "🧠 Domain Entropy (DGA)", "🌍 Geographic Distribution"),
            specs=[[{"type": "bar"}, {"type": "bar"}], [{"type": "scatter"}, {"type": "pie"}]]
        )

        # Chart 1: Threat Score
        fig.add_trace(go.Bar(x=df['url'], y=df['threat_score'], marker_color='red', name="Threat Score"), row=1, col=1)
        
        # Chart 2: Visitors
        fig.add_trace(go.Bar(x=df['url'], y=df['visitors'], name="Total Hits"), row=1, col=2)
        fig.add_trace(go.Bar(x=df['url'], y=df['entered'], name="Safe Entry"), row=1, col=2)

        # Chart 3: Entropy
        fig.add_trace(go.Scatter(x=df['url'], y=df['entropy'], mode='lines+markers', name="DGA Entropy"), row=2, col=1)

        # Chart 4: Countries
        country_counts = df['country'].value_counts()
        fig.add_trace(go.Pie(labels=country_counts.index, values=country_counts.values), row=2, col=2)

        fig.update_layout(height=800, template="plotly_dark", title="🔐 OMNI-SENTINEL X: CYBER INTELLIGENCE DASHBOARD")
        fig.show()

# ── EXECUTION ────────────────────────────────────────────────
if __name__ == "__main__":
    engine = OmniSentinelEngine()
    
    # Powerful Test Suite: Phishing, Data Theft, Malware, and Safe URLs
    test_urls = [
        "https://www.google.com",
        "http://paypal-login-security-update.com/verify?token=hidden123", # Phishing + Theft
        "https://vznqxc-c2-malware.ru/payload.exe",                     # Malware + DGA
        "http://example.com/api/get_creds?session=88234-js92",          # Data Theft
        "https://github.com/trending"
    ]

    for u in test_urls:
        engine.analyze_url(u)

    engine.generate_dashboard()
