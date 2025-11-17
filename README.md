# Simple TCP Port Scanner (Python)

This is a simple **TCP port scanner** written in Python.  
I built it to practice networking and cybersecurity concepts while learning with Python.

The script uses Python's built-in `socket` library to scan a range of ports on a target IP address and shows which ports are open and what common services usually run on those ports.

> ⚠️ **Note:** This project is for **learning and practice**.  
> Only scan systems that you **own** or **have permission** to test.

---

## How it works (in simple words)

- The program asks the user:
  - a **target** to scan (for example: `127.0.0.1`)
  - a **start port**
  - an **end port**
- Then it loops through all ports in that range.
- For each port it:
  - creates a TCP IPv4 socket
  - tries to connect to `(target, port)`
  - if the connection is successful, the port is considered **OPEN**
  - it prints the open port and the related **service name** (if it is a common port)
  - it also saves the result in a file called `scan_results.txt`.

---

## Some notes from my own comments in code

- About `127.0.0.1`:

  > `127.0.0.1` is a loopback address that always points to our own system (`localhost`).  
  > We use this for **safe testing** without the need for the Internet or an external network.

- About creating the socket:

  > The way a program or network communicates is to create a socket using the `socket` library.

  > We create a **TCP IPv4 socket** because most of the services we want to test are TCP, like:  
  > HTTP(80), HTTPS(443), SSH(22), FTP(21), SMTP(25).

- About the socket parameters:

  > First parameter:  
  > Network type (IPv4: like `127.0.0.1` or IPv6: like `2001:db8::1`)  
  > `AF_INET` for IPv4 and `AF_INET6` for IPv6.

  > Second parameter:  
  > Network connection type (`TCP` is reliable and connection-oriented, but `UDP` is unreliable and connection-less).  
  > We use `SOCK_STREAM` for TCP.

- About services on ports:

  > The port number itself is not important, what matters is the **service** running on that port.  
  > That is why we map some common ports (like 21, 22, 80, 443) to service names (FTP, SSH, HTTP, HTTPS).

---

## How to run the script

1. Make sure you have **Python 3** installed.

2. (Optional) Create and activate a virtual environment.

   ```bash
   python -m venv venv

On Windows (PowerShell):

`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
`venv\Scripts\Activate.ps1`

Run the script:
`python scanner.py`

Example input:
Target: 127.0.0.1
Start port: 20
End port: 100

Example output:
Enter target to scan (like:-->  127.0.0.1 ): 127.0.0.1
Enter start port: 20
Enter end port: 100

[*] Scanning 127.0.0.1 from port 20 to 100 ...

[+] Port 21 is OPEN  -->  FTP
[+] Port 22 is OPEN  -->  SSH

[*] Scan finished.
[*] Results saved to scan_results.txt

My experience and learning

Working on this simple TCP port scanner was a great way to understand how networks and sockets work. I learned step by step:

How to create sockets in Python and use them for communication.

The difference between TCP (reliable) and UDP (unreliable).

What common ports are and how services run on them.

How to scan a range of ports safely using 127.0.0.1 for testing.

How to write results to a file and organize code with functions.

This project helped me practice Python in a cybersecurity context and gave me confidence to explore more advanced networking and security topics.

Finally I’m Ahmadsiar Hamidi, and I’m really interested in cybersecurity. This is just the beginning of my learning journey, and I’m excited to keep exploring and building more projects.