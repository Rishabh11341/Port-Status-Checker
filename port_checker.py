import socket
import time

target = input("Enter Target IP or Hostname: ")

start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print("\nScanning...")
print("-" * 40)
print(f"{'Port':<10}{'Status'}")
print("-" * 40)

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"{port:<10}Open")
    else:
        print(f"{port:<10}Closed")

    sock.close()

    start = time.time()

    end = time.time()

print("-" * 40)
print(f"Scan completed in {end-start:.2f} seconds")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()
