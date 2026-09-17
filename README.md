README.md

## Project Overview

This project implements a Network Intrusion Detection System (NIDS) using Suricata on Kali Linux.

The system monitors network traffic, detects suspicious activity using custom detection rules, and generates security alerts through a local monitoring dashboard.

## Technologies Used

- Kali Linux
- Suricata
- Python
- Flask
- ICMP
- TCP
- Custom IDS Rules

## Features

- Network traffic monitoring
- ICMP traffic detection
- TCP SYN detection
- Custom Suricata rules
- Security alert generation
- Log analysis
- Local web dashboard

## Installation

### Update Kali Linux

```bash
sudo apt update
```
### Install Suricata

```bash
sudo apt install suricata -y
```

### Check Suricata

```bash
suricata -V
```

### Install Flask

```bash
sudo apt install python3-flask -y
```

## Setup Project

Clone the repository:

```bash
git clone https://github.com/sainivishal47/CodeAlpha_NetworkIntrusionDetection.git
```

Go to the project directory:

```bash
cd CodeAlpha_NetworkIntrusionDetection
```

## Test Suricata Configuration

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml -S custom.rules
```

## Run Dashboard

```bash
python3 app.py
```

Dashboard:

```bash
http://127.0.0.1:5000
```

## Run Suricata IDS

Open another terminal:

```bash
cd ~/CodeAlpha_NetworkIntrusionDetection
sudo suricata -c /etc/suricata/suricata.yaml -S custom.rules -i lo -l logs
```

## Generate Test Traffic

Open another terminal:

```bash
cd ~/CodeAlpha_NetworkIntrusionDetection
ping -c 4 127.0.0.1
```

## View Security Alerts

```bash
sudo cat logs/fast.log
```

Search CodeAlpha alerts:

```bash
sudo grep -i "CODEALPHA" logs/fast.log
```

## Detection Rules

### ICMP Detection

alert icmp any any -> any any (msg:"CODEALPHA ICMP Traffic Detected"; sid:1000001; rev:1;)

### TCP SYN Detection

alert tcp any any -> any any (msg:"CODEALPHA TCP SYN Detected"; flags:S; sid:1000002; rev:1;)

## Result

Suricata successfully monitors localhost network traffic and detects matching activity using custom IDS rules.

The Flask dashboard displays detected security events through a local web interface.

## Learning Objectives

- Network traffic monitoring
- Network Intrusion Detection
- Suricata configuration
- Custom IDS rule creation
- ICMP traffic detection
- TCP SYN detection
- Security alert analysis
- Linux networking
- Log analysis
- Basic threat detection
- Flask dashboard development

## Security Notice

Testing was performed on localhost in a controlled environment.

Network monitoring and security testing should only be performed on systems or networks where you have explicit authorization.

## Conclusion

This project demonstrates the use of Suricata as a Network Intrusion Detection System for monitoring network traffic and detecting suspicious activity through custom security rules.

## Author

Vishal Saini
