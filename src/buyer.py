from util import *

class ToSeller(OutputPort):
    def __init__(self, address):
        OutputPort.__init__(self, "buyer", address)
    
    def ask(self, product):
        self.send("ask", product)
    def accept(self, msg):
        self.send("accept", msg)
    def reject(self, msg):
        self.send("reject", msg)
    
class FromSeller(InputPort):
    def __init__(self):
        InputPort.__init__(self, "buyer", ('localhost', 8000))
    
    def quote(self, fn):
        self.set_callback("quote", fn)

class FromShipper(InputPort):
    def __init__(self):
        InputPort.__init__(self, "buyer", ('localhost', 8001))
    
    def details(self, fn):
        self.set_callback("details", fn)

from_shipper = FromShipper()
from_seller = FromSeller()

to_sellers = {
    "seller1": ToSeller(("localhost", 8100)),
    "seller2": ToSeller(("localhost", 8110)),
}

best_seller = None

@net_type_convert(str, int)
def from_seller_quote_callback(seller_id, price, *_):
    global best_seller
    if price < 20 and (best_seller is None or price < best_seller[0]):
        old_best = best_seller
        best_seller = (price, seller_id)
        if old_best is not None:
            to_sellers[old_best[1]].reject(f"Better price from {seller_id}")
    else:
        to_sellers[seller_id].reject(f"Not ok to buy chips for {price}")

def from_shipper_details_callback(invoice, *_):
    print(f"Received {invoice} from shipper!")

for seller in to_sellers.values():
    seller.ask("chips")
    from_seller.quote(from_seller_quote_callback)
    from_seller.recv()
    
to_sellers[best_seller[1]].accept(f"Ok to buy chips for {best_seller[0]}")
from_shipper.details(from_shipper_details_callback)
