import asyncore
import socket
 
host = ''
port = 2222
 
class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(1024)
        if data == "close":
            self.close()
            self.send(data)
    
class EchoServer(asyncore.dispatcher):
    
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(11)
        
    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print ('conn', addr)
            handler = EchoHandler(sock)

# client.send('HTTP/1.0 200 OK\r\n')
# client.send("Content-Type: text/html\r\n\r\n")
# client.send('<html><body><h1>Hello World</body></html>')
 
server = EchoServer(host, port)
asyncore.loop() 