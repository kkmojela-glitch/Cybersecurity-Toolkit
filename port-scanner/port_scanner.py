import socket

print("=== CYBERSECURITY PORT SCANNER ===")

target = input("Enter target IP or domain: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target}...\n")

open_ports = []

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    except:
        pass

print("\nScan complete.")
print(f"Open ports found: {len(open_ports)}")
