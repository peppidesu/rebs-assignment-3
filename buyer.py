class BuyerProcess:
    def ask2sell(self, product):
        print(f"Send ask2sell for {product} to the Seller.")
        return self

    def quote2buy_seller1(self, price):
        print(f"Received quote2buy ({price}) from the Seller 1.")
        return price
    
    def quote2buy_seller2(self, price):
        print(f"Received quote2buy ({price}) from the Seller 2.")
        return price


    def accept_or_reject(self, price, seller, cap = 20):
        if price < cap:
            print(f"Accept2sell the quote from {seller}. Price is lower than {cap}.")
            return True
        else:
            print(f"Reject2sell the quote from {seller}. Price is not lower than {cap}.")
            return False

    def details2buy(self, invoice):
        print(f"Received details2buy {invoice} from the Shipper.")

if __name__ == "__main__":
    buyer = BuyerProcess()

    buyer.ask2sell("chips")
    price_1, price_2 = buyer.quote2buy_seller1(24), buyer.quote2buy_seller2(16)
    buyer_response_1 = buyer.accept_or_reject(price_1, "seller 1")
    buyer_response_2 = buyer.accept_or_reject(price_2, "seller 2", cap = min(20, price_1))
    if (buyer_response_1 and buyer_response_2):
        print(f"Reject2sell the quote from seller 1. Price is not lower than {price_2}.")
        buyer_response_1 = False

    buyer_response = False

    if (buyer_response_1 or buyer_response_2):
        buyer_response = True

    if buyer_response:
        buyer.details2buy("chips")