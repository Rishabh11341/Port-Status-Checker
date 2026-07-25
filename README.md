# Port Status Checker

Port Status Checker is a Python-based network utility that scans a target host to determine the status of TCP ports. It uses Python's built-in socket library to establish TCP connection attempts within a specified port range and reports whether each port is open or closed. The tool also measures the total scan time, making it useful for learning basic networking concepts and socket programming.

## Features

- Scan a target IP address or hostname
- Accept a custom port range
- Uses TCP socket connections
- Configurable timeout for faster scanning
- Displays port status in a tabular format
- Measures total execution time
- Simple command-line interface

## Technologies Used

- Python 3
- Socket Programming
- TCP Networking

## Project Structure

```
Port-Status-Checker/
│── port_checker.py
└── README.md
```

## How to Run

```bash
python port_checker.py
```

Enter the target hostname/IP and the port range when prompted.

## Example

```
Target: scanme.nmap.org
Start Port: 20
End Port: 100

Port      Status
22        Open
80        Open
```

## Author

Rishabh Singh Tomar
