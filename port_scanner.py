import socket

host = input("Enter host (e.g., google.com): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {host}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")

    sock.close()
