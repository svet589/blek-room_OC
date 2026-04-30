import socket

def scan_ports(args):
    target = args[0] if args else "127.0.0.1"
    ports = [21, 22, 23, 80, 443, 8080]
    print(f"Сканирование {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Порт {port}: открыт")
        else:
            print(f"Порт {port}: закрыт")
        sock.close()
