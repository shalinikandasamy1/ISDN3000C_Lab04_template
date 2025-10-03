# RDK-X5 Network Fundamentals and Configuration Practice

## Overview

This repository contains code and documentation for the RDK-X5 Network Fundamentals and Configuration Practice lab. The lab covers:

- Setting up the RDK-X5 network environment with static IP configuration.
- Using Linux network commands to explore and diagnose network settings.
- Deploying simple Python network applications (server and client).
- Running network diagnostic tools like ping, dig, traceroute, telnet, and netcat.
- Building a simple IoT gateway server and monitoring client for network metrics collection.

---

## Contents

- `gateway_server.py` - Multi-threaded Python TCP server running on RDK-X5 that provides system info upon client request.
- `monitoring_client.py` - Python TCP client script running on a laptop that connects, requests system info, and displays received JSON data every 60 seconds.
- `.gitignore` - Ignored files for Python development.
- `requirements.txt` - Python dependencies (currently empty).
- This `README.md` - Project overview, setup, usage, and network configuration.

---

## Network Setup

- RDK-X5 Ethernet interface (`eth0`) has a static IP: `192.168.127.10`.
- Laptop Ethernet interface is configured with a static IP in the same subnet, e.g., `192.168.127.12`.
- Subnet mask for both interfaces: `255.255.255.0`.
- The connection is direct via Ethernet cable with no gateway or DNS required.
- RDK-X5 wireless interface (`wlan0`) typically connects to Wi-Fi for internet separately.
- Ensure both devices can ping each other to verify connectivity.

---

## Usage Instructions

1. **Connect via SSH to RDK-X5:**

ssh sunrise@192.168.127.10

text

2. **Run the Gateway Server on RDK-X5:** (python3 for macos)

python3 gateway_server.py

text

The server listens on all interfaces (0.0.0.0) at port `9999`. It handles multiple client requests simultaneously and sends JSON-formatted system data on valid `"GET_DATA"` requests.

3. **Run the Monitoring Client on Laptop:**

python3 monitoring_client.py

text

The client connects to the RDK-X5 server at `192.168.127.10:9999`, sends a `"GET_DATA"` request every 60 seconds, receives system info, and displays it.

---

## Additional Network Tools and Commands Covered

- `ping`: Test connectivity to routers, remote hosts, and the laptop.
- `dig`: Test domain name system (DNS) resolution.
- `traceroute`: Trace the routing path to external hosts.
- `telnet`: Test port reachability and manual HTTP requests.
- `netcat (nc)`: Port listening and simple data transfers.
- `ss`: Socket and listening port statistics.

---

## Development & Contribution

- Python 3.x is required.
- The code uses standard libraries: `socket`, `threading`, `json`, `subprocess`, `datetime`.
- No third-party dependencies currently; add to `requirements.txt` if needed later.
- Contributions and improvements welcomed via pull requests.

---

## Sample Network Description

The RDK-X5 development board uses a default static Ethernet IP address of `192.168.127.10`, configured manually or by factory settings, enabling direct LAN cable connection to a laptop also manually configured with an IP such as `192.168.127.12`. Both devices share the subnet mask `255.255.255.0`. This configuration allows private communication via socket programming and SSH without a DHCP server or gateway. The wireless interface functions separately for internet connectivity and serving as a secure management channel.


---

## Contact

For questions or issues, please contact your course instructor or project lead.
