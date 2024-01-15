import socket
import threading

addresses = {
    'seller>buyer': ("localhost", 8000),
    'shipper>buyer': ("localhost", 8001),
    'buyer>seller1': ("localhost", 8100),
    'buyer>seller2': ("localhost", 8200),
    'seller>shipper': ("localhost", 8300),    
}

class OutputPort:
    def __init__(self, link):
        self.address = addresses[link]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
    
    def send(self, id: str, *data):
        print(f"Sending {id}({list(data)}) to {self.address}")
        contents = id.encode() + b'\x00' + b'\x00'.join([str(d).encode() for d in data])
        self.socket.sendto(contents, self.address)
        
    def close(self):
        self.socket.close()
    
    def __del__(self):
        self.close()
        
class InputPort:
    def __init__(self, link):
        self.address = addresses[link]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.address)   
        self.callbacks = dict()    
        
    def set_callback(self, id: str, callback):
        self.callbacks[id] = callback
        
    def recv(self):
        data, _ = self.socket.recvfrom(1024)
        fields = data.split(b'\x00')
        id = fields[0].decode()
        print(f"{self.address}: Received {id}({fields[1:]})")
        self.callbacks[id](*[f.decode() for f in fields[1:]])
    
    def close(self):
        self.socket.close()
        
    def __del__(self):
        self.close()
        
