from util import *

class FromSeller(InputPort):
    def __init__(self):
        InputPort.__init__(self, "shipper", ('localhost', 8200))
    
    def order(self, fn):
        self.set_callback("order", fn)

class ToBuyer(OutputPort):
    def __init__(self):
        OutputPort.__init__(self, "shipper", ('localhost', 8001))
    
    def details(self, details: str):
        self.send("details", details)

from_seller = FromSeller()
to_buyer = ToBuyer()

def from_seller_order_callback(product, *_):
    to_buyer.details(f"invoice for {product}")

from_seller.order(from_seller_order_callback)
from_seller.recv()