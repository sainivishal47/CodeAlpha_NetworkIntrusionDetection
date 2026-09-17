from flask import Flask, jsonify
import os
import webbrowser
import threading

app = Flask(__name__)

LOG_FILE = "logs/fast.log"


@app.route("/")
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>CodeAlpha NIDS Dashboard</title>
    <meta http-equiv="refresh" content="5">

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b1220;
            color: white;
        }

        header {
            padding: 25px 50px;
            background: #111c31;
            border-bottom: 1px solid #263653;
        }

        h1 {
            margin: 0;
            font-size: 30px;
        }

        .subtitle {
            color: #9aa8bd;
            margin-top: 8px;
        }

        .container {
            padding: 35px 50px;
        }

        .cards {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }

        .card {
            background: #111c31;
            padding: 25px;
            border-radius: 12px;
            min-width: 220px;
            border: 1px solid #263653;
        }

        .number {
            font-size: 32px;
            font-weight: bold;
            margin-top: 10px;
        }

        .green {
            color: #35d07f;
        }

        .red {
            color: #ff5c5c;
        }

        .blue {
            color: #55aaff;
        }

        .panel {
            margin-top: 30px;
            background: #111c31;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #263653;
        }

        .alert {
            padding: 15px;
            margin-top: 10px;
            background: #1a2538;
            border-left: 4px solid #ff5c5c;
            border-radius: 5px;
        }

        footer {
            color: #7f8da3;
            margin-top: 30px;
        }
    </style>
</head>

<body>

<header>
    <h1>🛡️ CodeAlpha Network Intrusion Detection System</h1>
    <div class="subtitle">Suricata Security Monitoring Dashboard</div>
</header>

<div class="container">

    <div class="cards">

        <div class="card">
            <div>System Status</div>
            <div class="number green">● ACTIVE</div>
        </div>

        <div class="card">
            <div>Detection Engine</div>
            <div class="number blue">SURICATA</div>
        </div>

        <div class="card">
            <div>Interface</div>
            <div class="number">LO</div>
        </div>

        <div class="card">
            <div>Alerts</div>
            <div id="alertCount" class="number red">0</div>
        </div>

    </div>

    <div class="panel">
        <h2>🚨 Security Alerts</h2>
        <div id="alerts">Loading alerts...</div>
    </div>

    <footer>
        CodeAlpha Cyber Security Internship — Task 4
    </footer>

</div>

<script>
async function loadAlerts() {
    const response = await fetch('/alerts');
    const data = await response.json();

    document.getElementById("alertCount").innerText = data.count;

    if (data.alerts.length === 0) {
        document.getElementById("alerts").innerHTML =
            "<p>No security alerts detected yet.</p>";
        return;
    }

    document.getElementById("alerts").innerHTML =
        data.alerts.map(alert =>
            `<div class="alert">${alert}</div>`
        ).join("");
}

loadAlerts();
setInterval(loadAlerts, 2000);
</script>

</body>
</html>
"""


@app.route("/alerts")
def alerts():
    alerts = []

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", errors="ignore") as file:
            for line in file:
                if "CODEALPHA" in line:
                    alerts.append(line.strip())

    return jsonify({
        "count": len(alerts),
        "alerts": alerts[-10:]
    })


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(host="127.0.0.1", port=5000)
