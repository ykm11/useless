import socket

class remote:

    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        #print(f"\u001b[32m[+] HOST:{HOST}, PORT:{PORT} Connected\u001b[0m")
        print("\u001b[32m[+] HOST:{0}, PORT:{1} Connected\u001b[0m".format(HOST, PORT))

    def recv(self, bytes_num=1024):
        return self.client.recv(bytes_num)

    def recvline(self):
        buf = b''
        while buf.find(b'\n') == -1:
            buf += self.recv(1)
        return buf

    def recvuntil(self, serach_text):
        buf = b''
        while buf.find(serach_text) == -1:
            buf += self.recv(1)
        return buf

    def send(self, msg):
        self.client.send(msg)
        return len(msg)
    
    def sendline(self, msg):
        self.send(msg + b"\n")
        return len(msg)+1

    def sendafter(self, msg):
        _ = self.recvuntil(msg)
        self.send(msg)

    def close(self):
        self.client.close()
        print("\u001b[32m[+] Connection Closed\u001b[0m")
