import socket

target = input("Enter target IP or website: ")

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

print("Scanning target:", target)

for port in range(20, 200):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        service = common_ports.get(port, "Unknown Service")
        print(f"Port {port} is open ({service})")

    s.close()

print("Scan finished")