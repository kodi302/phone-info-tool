import socket


def port_scanner():
    print("\n========== PORT SCANNER ==========\n")

    host = input("Enter IP Address or Domain: ").strip()

    try:
        ip = socket.gethostbyname(host)
        print(f"\nScanning {host} ({ip})...\n")

        common_ports = {
            20: "FTP Data",
            21: "FTP",
            22: "SSH",
            23: "Telnet",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL",
            3389: "RDP",
            8080: "HTTP-Alt",
        }

        open_ports = []

        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                open_ports.append((port, service))

            sock.close()

        print("=" * 40)

        if open_ports:
            print("Open Ports:\n")
            for port, service in open_ports:
                print(f"✅ {port:<6} {service}")
        else:
            print("❌ No common open ports found.")

    except Exception as e:
        print("Error:", e)
