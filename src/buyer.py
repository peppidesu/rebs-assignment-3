from util import *

class ToSeller(OutputPort):
    def __init__(self, seller_id):
        OutputPort.__init__(self, f'buyer>{seller_id}')
    
    def ask(self, product):
        self.send("ask", product)
    def accept(self, msg):
        self.send("accept", msg)
    def reject(self, msg):
        self.send("reject", msg)
    
class FromSeller(InputPort):
    def __init__(self):
        InputPort.__init__(self, 'seller>buyer')
    
    def quote(self, fn):
        self.set_callback("quote", fn)

class FromShipper(InputPort):
    def __init__(self):
        InputPort.__init__(self, 'shipper>buyer')
    
    def details(self, fn):
        self.set_callback("details", fn)

from_shipper = FromShipper()
from_seller = FromSeller()
to_sellers = {
    "seller1": ToSeller("seller1"),
    "seller2": ToSeller("seller2"),
}

best_seller = None
def from_seller_quote_callback(seller_id, price, *args):
    global best_seller
    price_int = int(price)
    if price_int < 20 and (best_seller is None or price_int < best_seller[0]):
        old_best = best_seller
        best_seller = (price_int, seller_id)
        if old_best is not None:
            to_sellers[old_best[1]].reject(f"Better price from {seller_id}")
    else:
        to_sellers[seller_id].reject(f"Not ok to buy chips for {price}")

def from_shipper_details_callback(invoice, *args):
    print(f"Received {invoice} from shipper!")

for seller in to_sellers.values():
    seller.ask("chips")
    from_seller.quote(from_seller_quote_callback)
    from_seller.recv()
    
to_sellers[best_seller[1]].accept(f"Ok to buy chips for {best_seller[0]}")
from_shipper.details(from_shipper_details_callback)
