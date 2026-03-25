import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, port))
        return True
    except:
        return False
    finally:
        sock.close()

ip = input("Введите IP-адрес для сканирования: ")
start_port = int(input("Введите начальный порт: "))
end_port = int(input("Введите конечный порт: "))

for port in range(start_port, end_port + 1):
    if scan_port(ip, port):
        print(f"Порт {port} открыт.")
    else:
        print(f"Порт {port} закрыт.")


