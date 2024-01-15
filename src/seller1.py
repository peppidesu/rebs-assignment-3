from util import *

class FromBuyer(InputPort):
    def __init__(self):
        InputPort.__init__(self, 'buyer>seller1')
    
    def ask(self, fn):
        self.set_callback("ask", fn)
    
    def accept(self, fn):
        self.set_callback("accept", fn)
    
    def reject(self, fn):
        self.set_callback("reject", fn)

class ToBuyer(OutputPort):
    def __init__(self):
        OutputPort.__init__(self, 'seller>buyer')
    
    def quote(self, price: int):
        self.send("quote", "seller1", price)
        
class ToShipper(OutputPort):
    def __init__(self):
        OutputPort.__init__(self, 'seller>shipper')
    
    def order(self, product: str):
        self.send("order", product)
        
from_buyer = FromBuyer()
to_buyer = ToBuyer()
to_shipper = ToShipper()

def from_buyer_ask_callback(product, *args):    
    if product == "chips":
        to_buyer.quote(15)
        from_buyer.accept(from_buyer_accept_callback)
        from_buyer.reject(from_buyer_reject_callback)
        from_buyer.recv() 
    else:
        
        pass

def from_buyer_accept_callback(msg):
    print(msg)
    to_shipper.order("chips")

def from_buyer_reject_callback(msg):
    print(msg)
    pass

from_buyer.ask(from_buyer_ask_callback)
from_buyer.recv()