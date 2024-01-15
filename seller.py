class SellerProcess:
    def __init__(self):
        self.quote = None
        self.product = None
        self.order = None

    def receive_ask2sell(self, product):
        self.product = product
        print(f"Received ask2sell for {product}.")
        return self

    def quote2buy(self):
        self.quote = int(input(f"Enter the quote/price for {self.product}: "))
        print(f"Send quote2buy ({self.quote}) to the Buyer.")
        return self

    def handle_accept(self):
        self.order = f"Order for {self.product}"
        print(f"Received accept2sell from the Buyer. Order placed: {self.order}.")
        print(f"Send order2ship for {self.product} to Shipper.")
        return self

    def handle_reject(self):
        print("Received reject2sell from the Buyer. Quote rejected.")
        return self


if __name__ == "__main__":
    seller = SellerProcess()

    seller.receive_ask2sell("chips").quote2buy()

    if seller.quote < 20:
        seller.handle_accept()
    else:
        seller.handle_reject()