import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3389: "RDP",
}


def get_target_and_range():
    """
    Getting the desired target and from what interval to what interval to scan.
    If target is empty, we use 127.0.0.1 for safe local testing.
    """
    target = input("Enter target to scan (like:-->  127.0.0.1 ): ").strip()
    if not target:
        # 127.0.0.1 is a loopback address that always points to our system (localhost).
        # We use this for safe testing without the need for the Internet.
        target = "127.0.0.1"
        print("[*] No target entered. Default: 127.0.0.1")

    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    return target, start_port, end_port


def scan_port(target, port, timeout=0.5):
    """
    The way a program or network communicates is to create a socket using the socket library.

    Create TCP IPv4 socket
    because most of the services we want to test are TCP like:
    HTTP(80) / HTTPS(443) / SSH(22) / FTP(21) / SMTP(25)

    First parameter:
    Network type (IPv4: Like 127.0.0.1 or IPv6: Like 2001:db8::1)
    AF_INET for IPv4 & AF_INET6 for IPv6

    Second parameter:
    Network connection type (TCP is reliable and connection-oriented,
    but UDP is unreliable and connection-less) SOCK_STREAM for TCP.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        s.connect((target, port))
        # Get service name for this port if it exists, otherwise use "Unknown service"
        # because the port number is not important, but the service on that port is.
        service = COMMON_PORTS.get(port, "Unknown service")
        return service
    except:
        # The port is not open and we cannot connect.
        return None
    finally:
        s.close()


def scan_range(target, start_port, end_port, results_file_path="scan_results.txt"):
    """
    Scan a range of ports on the target and save open ports to a file.
    """
    print(f"\n[*] Scanning {target} from port {start_port} to {end_port} ...\n")

    # Open (or create) a text file to save scan results. "w" stands for write mode
    results_file = open(results_file_path, "w", encoding="utf-8")
    results_file.write(f"Scan results for {target} (ports {start_port}-{end_port})\n")
    results_file.write("-" * 50 + "\n")

    for port in range(start_port, end_port + 1):
        service = scan_port(target, port)

        if service is not None:
            message = f"[+] Port {port} is OPEN  -->  {service}"
            print(message)
            results_file.write(message + "\n")

    results_file.close()
    print("\n[*] Scan finished.")
    print(f"[*] Results saved to {results_file_path}")


def main():
    target, start_port, end_port = get_target_and_range()
    scan_range(target, start_port, end_port)


if __name__ == "__main__":
    main()
