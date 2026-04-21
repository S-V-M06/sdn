# ARP Handling in SDN Networks

Complete implementation of ARP (Address Resolution Protocol) handling in Software Defined Networking. Demonstrates packet interception, ARP request/reply handling, host discovery, and communication validation.

## 📋 Files Included

1. **arp_controller.py** - Real-time ARP packet controller (monitors actual network)
2. **arp_packet_handler.py** - Standalone ARP utilities (discovery, validation, MAC lookup)
3. **mininet_topology.py** - Virtual SDN network topology for testing
4. **requirements.txt** - Python dependencies
5. **setup.sh** - Automated installation script
6. **PROJECT_REPORT.md** - Complete project report

## 🌟 Key Features

✓ **Intercept ARP packets** - Capture and analyze real ARP traffic  
✓ **Generate ARP responses** - Create and send ARP reply messages  
✓ **Enable host discovery** - Automatically learn host IP-MAC mappings  
✓ **Validate communication** - Test connectivity between hosts  
✓ **Virtual network simulation** - Test with Mininet topology  

## 📦 Installation

### Step 1: Install System Dependencies

```bash
sudo apt-get update
sudo apt-get install -y mininet openvswitch-switch
```

### Step 2: Setup Python Environment

```bash
cd /home/Downloads/sdn

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install Python packages
pip3 install scapy
```

Done! Now you're ready to run the files.

---

## 🚀 How to Run Each File

### FILE 1: ARP Controller - Real Network Monitoring

**What it does:**
- Listens to your actual network interface
- Captures real ARP packets from devices
- Shows ARP requests and replies in real-time
- Logs which devices are communicating

**How to run it:**

```bash
# Step 1: Open a terminal and navigate to project
cd /home/Downloads/sdn

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Run with sudo (needed for network access)
sudo -E python3 arp_controller.py
```

**What you'll see:**
```
2026-04-15 17:33:15,888 - INFO - ARP Controller Initialized on interface: wlo1
2026-04-15 17:33:15,888 - INFO - Starting ARP Controller on wlo1...

============================================================
ARP Controller is running on wlo1
Press Ctrl+C to stop
============================================================

[ARP REQUEST] 192.168.1.100 (aa:bb:cc:dd:ee:ff) -> 192.168.1.1
[ARP REPLY SENT] 00:11:22:33:44:55 -> aa:bb:cc:dd:ee:ff
[Learned MAP] 192.168.1.100 -> aa:bb:cc:dd:ee:ff
```

**To stop it:** Press `Ctrl+C`

**Best for:** Showing real network activity, learning how ARP works on your actual network

---

### FILE 2: ARP Packet Handler - Network Utilities

**What it does:**
- Discovers all devices on a network
- Tests if devices can reach each other
- Gets MAC addresses for IP addresses
- Performs network scans

**How to run it:**

```bash
# Step 1: Open a NEW terminal
cd /home/Downloads/sdn

# Step 2: Activate virtual environment
source venv/bin/activate

# Step 3: Run with sudo (needed for network access)
```

**OPTION 1: Discover Hosts (Find all devices on network)**

```bash
sudo python3 arp_packet_handler.py --discover 192.168.1.0/24
```

Replace `192.168.1.0/24` with your network range:
- If your IP is `192.168.1.50` → use `192.168.1.0/24`
- If your IP is `10.0.0.50` → use `10.0.0.0/24`

**Expected output:**
```
ARP Packet Handler initialized on interface: wlo1
Starting host discovery on network: 192.168.1.0/24
Host discovered: 192.168.1.1 (aa:bb:cc:dd:ee:ff)
Host discovered: 192.168.1.100 (11:22:33:44:55:66)
Discovery complete: 2 hosts found

ARP Table:
  192.168.1.1     -> aa:bb:cc:dd:ee:ff
  192.168.1.100   -> 11:22:33:44:55:66
```

---

**OPTION 2: Test Communication (Check if two IPs can reach each other)**

```bash
sudo python3 arp_packet_handler.py --validate 192.168.1.1 8.8.8.8
```

Replace the IPs with ones you want to test:
- `192.168.1.1` = first device (your router usually)
- `8.8.8.8` = second device (Google's DNS)

**Expected output:**
```
Validating ARP communication: 192.168.1.1 <-> 8.8.8.8
✓ Communication validated: 192.168.1.1 can reach 8.8.8.8 (aa:bb:cc:dd:ee:ff)
```

---

**OPTION 3: Get MAC Address (Find MAC for an IP)**

```bash
sudo python3 arp_packet_handler.py --get-mac 192.168.1.1
```

Replace `192.168.1.1` with the IP you want to look up

**Expected output:**
```
Validating ARP communication: 192.168.1.1 <-> 192.168.1.1
MAC found: 192.168.1.1 -> aa:bb:cc:dd:ee:ff
MAC Address: aa:bb:cc:dd:ee:ff
```

**Best for:** Network scanning, finding devices, testing connectivity

---

### FILE 3: Mininet Virtual Network (BEST FOR DEMO)

**What it does:**
- Creates a fake network with virtual devices
- Sets up a virtual switch
- Creates 3 virtual hosts (h1, h2, h3)
- Lets you test ARP in a controlled environment
- Perfect for teacher demo - no real network needed!

**How to run it:**

```bash
# Step 1: Open a terminal
cd /home/Downloads/sdn

# Step 2: Run with sudo
sudo python3 mininet_topology.py
```

**What you'll see:**
```
★ Creating SDN Network Topology for ARP Testing
✓ Added Switch s1
✓ Added Hosts h1, h2, h3
✓ Connected hosts to switch

============================================================
★ MININET TOPOLOGY READY FOR ARP TESTING
============================================================

Network Details:
  Switch: s1 (OpenFlow 1.3 enabled)
  Hosts: h1 (10.0.0.1), h2 (10.0.0.2), h3 (10.0.0.3)
  Controller: RemoteController on 127.0.0.1:6633

AVAILABLE COMMANDS IN CLI:
  h1 ping h2              - Test ARP with ping
  h1 arp -n               - View ARP table
  h1 arping 10.0.0.2      - Send ARP request
  h1 tcpdump -i h1-eth0 -n arp  - Capture ARP packets
  dump                    - Show topology
  links                   - Show all links
  exit                    - Exit Mininet

mininet> _
```

Now you're inside the Mininet CLI. Type commands here:

---

## 🎯 Mininet Commands (Type These at `mininet>` prompt)

```
# TEST 1: Ping from h1 to h2 (generates ARP request)
mininet> h1 ping h2
PING 10.0.0.2 from 10.0.0.1
64 bytes from 10.0.0.2: seq=0 ttl=64 time=1.234 ms
64 bytes from 10.0.0.2: seq=1 ttl=64 time=0.987 ms

# TEST 2: Check ARP table on h1
mininet> h1 arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.0.2                 ether   00:00:00:00:00:02   C                     h1-eth0
10.0.0.3                 ether   00:00:00:00:00:03   C                     h1-eth0

# TEST 3: Send explicit ARP request
mininet> h1 arping 10.0.0.3
ARPING 10.0.0.3 from 10.0.0.1 h1-eth0
60 bytes from 00:00:00:00:00:03 (10.0.0.3): index=0 time=1.234 msec

# TEST 4: Capture ARP packets in real-time
mininet> h1 tcpdump -i h1-eth0 -n arp
tcpdump: verbose output suppressed
listening on h1-eth0, link-type EN10MB (Ethernet)
12:34:56.789 arp who-has 10.0.0.3 tell 10.0.0.1
12:34:56.790 arp reply 10.0.0.3 is-at 00:00:00:00:00:03

# TEST 5: Show network topology
mininet> dump
<Host h1: h1-eth0:10.0.0.1>
<Host h2: h2-eth0:10.0.0.2>
<Host h3: h3-eth0:10.0.0.3>
<OVSSwitch s1: ...>

# TEST 6: Show all connections
mininet> links
h1-eth0<->s1-eth1 (OK OK)
h2-eth0<->s1-eth2 (OK OK)
h3-eth0<->s1-eth3 (OK OK)

# EXIT MININET
mininet> exit
```

---

## 🎓 Complete Demo for Your Teacher

**This shows everything working together:**

### Terminal 1: Start Virtual Network
```bash
cd /home/Downloads/sdn
sudo python3 mininet_topology.py

# Wait for "mininet>" prompt to appear
```

### Terminal 2: Run ARP Controller (shows it intercepting packets)
```bash
cd /home/Downloads/sdn
source venv/bin/activate
sudo -E python3 arp_controller.py

# This will show ARP requests/replies as they happen
```

### Terminal 1: Run Tests in Mininet
```
mininet> h1 ping h2
mininet> h1 arping 10.0.0.3
mininet> h1 arp -n
mininet> exit
```

**What your teacher sees:**
- Terminal 1: Mininet showing ping and ARP results
- Terminal 2: ARP Controller showing it's intercepting all the traffic in real-time
- This proves your ARP controller is working!

---

## 📊 Quick Reference Table

| File | Command | What It Shows | Run Time |
|---|---|---|---|
| ARP Controller | `sudo -E python3 arp_controller.py` | Real ARP traffic | Until Ctrl+C |
| Host Discovery | `sudo python3 arp_packet_handler.py --discover 192.168.1.0/24` | All devices on network | 5-10 seconds |
| Validate Connection | `sudo python3 arp_packet_handler.py --validate 10.0.0.1 8.8.8.8` | If two IPs can reach each other | 5 seconds |
| Get MAC Address | `sudo python3 arp_packet_handler.py --get-mac 192.168.1.1` | MAC address for an IP | 3-5 seconds |
| Virtual Network | `sudo python3 mininet_topology.py` | Interactive virtual network | Until you type exit |

---

## ⚙️ Requirements

- Linux (Ubuntu/Debian)
- Python 3.6+
- Internet (for first setup only)
- Ability to run `sudo` commands

## 🔧 Troubleshooting

**Problem:** "ModuleNotFoundError: No module named 'scapy'"
- **Solution:** Make sure you activated the virtual environment: `source venv/bin/activate`

**Problem:** "Permission denied" or "This program requires root/sudo privileges"
- **Solution:** Always use `sudo` for these scripts

**Problem:** Mininet won't start or says "Cannot find controller"
- **Solution:** This is expected - just run the mininet commands anyway, they still work

**Problem:** "Command not found: mininet"
- **Solution:** Install mininet first: `sudo apt-get install mininet`

---

All files ready to use! Good luck with your presentation! 👍

